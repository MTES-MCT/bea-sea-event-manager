from django.urls import path

from . import views

app_name = "entry_helper"

urlpatterns = [
    path("", views.index, name="index"),
    path("reports/", views.ReportTodoListView.as_view(), name="reports"),
]
