from django.urls import path

from .views import EmailSentView, LabListView, PolicyView, VoteCompleteView, VoteFormView

urlpatterns = [
    path("", LabListView.as_view(), name="list"),
    path("form/", VoteFormView.as_view(), name="form"),
    path("email-sent/", EmailSentView.as_view(), name="email_sent"),
    path("vote-complete/<str:token>", VoteCompleteView.as_view(), name="vote_complete"),
    path("policy/", PolicyView.as_view(), name="policy"),
]
