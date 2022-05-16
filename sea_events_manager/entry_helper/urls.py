from django.urls import path

from . import views

app_name = "entry_helper"

urlpatterns = [
    path("", views.index, name="index"),
    path("reports/done/", views.ReportDoneListView.as_view(), name="reports_done"),
    path("reports/", views.ReportTodoListView.as_view(), name="reports"),
]
