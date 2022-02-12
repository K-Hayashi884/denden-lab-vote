from django.urls import path

from .views import LabListView, VoteFormView

urlpatterns = [
    path("", LabListView.as_view(), name="list"),
    path("form/", VoteFormView.as_view(), name="form"),
]
