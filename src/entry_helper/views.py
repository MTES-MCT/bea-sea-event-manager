from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings

from entry_helper.models import Report
from entry_helper.core import (
    switch_report_to_done,
    switch_report_to_ignored,
    switch_report_to_todo,
)
from entry_helper.exceptions import FailedPushToEmcip

from entry_helper.import_service import RawReportsClient

raw_reports_client = RawReportsClient.from_engine(engine=settings.RAW_REPORTS_ENGINE)


class ReportListView(LoginRequiredMixin, ListView):
    model = Report

    ordering = ["-event_datetime"]

    login_url = "admin:login"


class ReportTodoListView(ReportListView):
    queryset = Report.objects.filter(status="todo")

    template_name: str = "entry_helper/reports.html"
    extra_context = {
        "title_content": "Rapports à traiter",
        "report_list_status_type": "todo",
    }

    def get(self, request):
        raw_reports_client.update_refresh_list_based_on_last_update_datetime()
        return super().get(request)

    def post(self, request):
        current_view = "entry_helper:reports"
        match report_target_status := request.POST.get("report_target_status", None):
            case "done":
                _post_with_push_to_emcip(request, current_view)
            case "ignored":
                _post_with_ignored(request, current_view)
            case _:
                raise Exception(f"Unknown target status {report_target_status}")
        return redirect(current_view)


class ReportDoneListView(ReportListView):
    queryset = Report.objects.filter(status="done")

    template_name: str = "entry_helper/reports.html"
    extra_context = {
        "title_content": "Rapports investigués",
        "report_list_status_type": "done",
    }


class ReportIgnoredListView(ReportTodoListView):
    queryset = Report.objects.filter(status="ignored")

    template_name: str = "entry_helper/reports.html"
    extra_context = {
        "title_content": "Rapports ignorés",
        "report_list_status_type": "ignored",
    }

    def post(self, request):
        current_view = "entry_helper:reports_ignored"
        match report_target_status := request.POST.get("report_target_status", None):
            case "done":
                _post_with_push_to_emcip(request, current_view)
            case "todo":
                _post_with_todo(request, current_view)
            case _:
                raise Exception(f"Unknown target status {report_target_status}")
        return redirect(current_view)


def handle_failed_push_to_emcip(func):
    def query_trying_to_push(request, *args, **kwargs):
        try:
            func(request, *args, **kwargs)
        except FailedPushToEmcip as e:
            print(e)
            messages.error(request, e)

    return query_trying_to_push


@handle_failed_push_to_emcip
def _post_with_push_to_emcip(request, django_redirect_url: str) -> None:
    if report_uuid := request.POST.get("report_uuid", None):
        report = Report.objects.get(uuid=report_uuid)
        switch_report_to_done(report)


@handle_failed_push_to_emcip
def _post_with_ignored(request, django_redirect_url: str) -> None:
    if report_uuid := request.POST.get("report_uuid", None):
        report = Report.objects.get(uuid=report_uuid)
        switch_report_to_ignored(report)


@handle_failed_push_to_emcip
def _post_with_todo(request, django_redirect_url: str) -> None:
    if report_uuid := request.POST.get("report_uuid", None):
        report = Report.objects.get(uuid=report_uuid)
        switch_report_to_todo(report)
