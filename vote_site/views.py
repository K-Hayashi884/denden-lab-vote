from django.core.mail import send_mail
from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.db.models import Count, F, Q
from django.http import Http404, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView

from .forms import VoteForm
from .models import Lab, Vote


class LabListView(ListView):
    template_name = "lab_list.html"
    model = Lab

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["years"] = Vote.objects.distinct().values_list("year", flat=True)
        context["selected_year"] = int(self.request.GET.get("year", max(context["years"])))
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        year = self.request.GET.get(
            "year", max(Vote.objects.distinct().values_list("year", flat=True))
        )

        order_by = self.request.GET.get("orderby", "belongs_to")

        queryset = queryset.annotate(
            vote1_cnt=Count("vote1", filter=Q(vote1__is_active=True, vote1__year=year)),
            vote2_cnt=Count("vote2", filter=Q(vote2__is_active=True, vote2__year=year)),
            vote3_cnt=Count("vote3", filter=Q(vote3__is_active=True, vote3__year=year)),
            vote4_cnt=Count("vote4", filter=Q(vote4__is_active=True, vote4__year=year)),
            vote5_cnt=Count("vote5", filter=Q(vote5__is_active=True, vote5__year=year)),
            vote6_cnt=Count("vote6", filter=Q(vote6__is_active=True, vote6__year=year)),
            vote7_cnt=Count("vote7", filter=Q(vote7__is_active=True, vote7__year=year)),
            total_cnt=F("vote1_cnt")
            + F("vote2_cnt")  # noqa: W503
            + F("vote3_cnt")  # noqa: W503
            + F("vote4_cnt")  # noqa: W503
            + F("vote5_cnt")  # noqa: W503
            + F("vote6_cnt")  # noqa: W503
            + F("vote7_cnt"),  # noqa: W503
        ).order_by(order_by, "id")

        return queryset


class VoteFormView(FormView):
    template_name = "form.html"
    form_class = VoteForm
    success_url = reverse_lazy("email_sent")

    def form_valid(self, form):
        vote = form.save()
        email = form.cleaned_data["email"]
        activate_url = reverse_lazy("vote_complete", args=[dumps(vote.pk)])
        send_mail(
            subject="研究室以降投票の確認",
            message=f"まだ投票は完了していません。以下のURLにアクセスして投票を有効にしてください。\n{activate_url}",
            from_email="denden.lab.vote@gmail.com",
            recipient_list=[email],
        )

        return super().form_valid(form)


class EmailSentView(TemplateView):
    template_name = "email_sent.html"


class VoteCompleteView(TemplateView):
    template_name = "vote_complete.html"

    def get(self, request, **kwargs):
        token = kwargs.get("token")
        try:
            pk = loads(token, max_age=60 * 60 * 24)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                vote = Vote.objects.get(pk=pk)
            except Vote.DoesNotExist:
                return Http404("Vote doesn't exist")
            else:
                if not vote.is_active:
                    # 既に同一メールアドレスのものが存在していれば削除して上書き
                    Vote.objects.filter(email=vote.email).exclude(pk=pk).delete()
                    vote.is_active = True
                    vote.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class PolicyView(TemplateView):
    template_name = "policy.html"
