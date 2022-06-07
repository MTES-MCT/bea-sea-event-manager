from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from entry_helper.models import Report
from entry_helper.core import (
    switch_report_to_done,
    switch_report_to_ignored,
    switch_report_to_todo,
)

from data_scripts.setup_bea_fake_data import task_load_fake_bea_data_into_django


class ReportListView(LoginRequiredMixin, ListView):
    model = Report

    ordering = ["-event_datetime"]

    login_url = 'admin:login'


class ReportTodoListView(ReportListView):
    queryset = Report.objects.filter(status="todo")

    template_name: str = "entry_helper/reports.html"
    extra_context={
        'title_content': "Rapports à traiter",
        'report_list_status_type': "todo",
    }
    def get(self, request):
        task_load_fake_bea_data_into_django()
        return super().get(request)

    def post(self, request):
        current_view = "entry_helper:reports"
        match report_target_status := request.POST.get("report_target_status", None):
            case "done":
                return _post_with_push_to_emcip(request, current_view)
            case "ignored":
                return _post_with_ignored(request, current_view)
            case _:
                raise Exception(f"Unknown target status {report_target_status}")


class ReportDoneListView(ReportListView):
    queryset = Report.objects.filter(status="done")

    template_name: str = "entry_helper/reports.html"
    extra_context={
        'title_content': "Rapports investigués",
        'report_list_status_type': "done",
    }


class ReportIgnoredListView(ReportTodoListView):
    queryset = Report.objects.filter(status="ignored")

    template_name: str = "entry_helper/reports.html"
    extra_context={
        'title_content': "Rapports ignorés",
        'report_list_status_type': "ignored",
    }

    def post(self, request):
        current_view = "entry_helper:reports_ignored"
        match report_target_status := request.POST.get("report_target_status", None):
            case "done":
                return _post_with_push_to_emcip(request, current_view)
            case "todo":
                return _post_with_todo(request, current_view)
            case _:
                raise Exception(f"Unknown target status {report_target_status}")


def _post_with_push_to_emcip(request, django_redirect_url: str):
    if report_uuid := request.POST.get("report_uuid", None):
        report = Report.objects.get(uuid=report_uuid)
        switch_report_to_done(report)

    return redirect(django_redirect_url)


def _post_with_ignored(request, django_redirect_url: str):
    if report_uuid := request.POST.get("report_uuid", None):
        report = Report.objects.get(uuid=report_uuid)
        switch_report_to_ignored(report)

    return redirect(django_redirect_url)


def _post_with_todo(request, django_redirect_url: str):
    if report_uuid := request.POST.get("report_uuid", None):
        report = Report.objects.get(uuid=report_uuid)
        switch_report_to_todo(report)

    return redirect(django_redirect_url)