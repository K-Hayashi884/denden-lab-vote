from django.core.mail import send_mail
from django.core.signing import dumps
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView

from .forms import VoteForm
from .models import Lab


class LabListView(ListView):
    template_name = "lab_list.html"
    model = Lab

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        # keyword = self.request.GET.get('keyword')
        # if keyword is not None:
        #     queryset = queryset.filter(title__contains=keyword)

        queryset = queryset.order_by("belongs_to", "id")

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
            recipient_list=[email],
        )

        return super().form_valid(form)


class EmailSentView(TemplateView):
    template_name = "email_sent.html"
