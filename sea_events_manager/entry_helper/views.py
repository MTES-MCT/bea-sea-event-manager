from django.shortcuts import redirect
from django.views.generic import ListView

from entry_helper.models import Report
from entry_helper.internals import switch_report_to_done
from django.contrib.auth.mixins import LoginRequiredMixin


class ReportListView(LoginRequiredMixin, ListView):
    model = Report

    ordering = ["-event_datetime"]

    login_url = '/admin/login/'


class ReportTodoListView(ReportListView):
    queryset = Report.objects.filter(status="todo")

    template_name: str = "entry_helper/report_todo.html"

    def post(self, request):
        _post_with_push_to_emcip(request, "entry_helper:reports")


class ReportDoneListView(ReportListView):
    queryset = Report.objects.filter(status="done")

    template_name: str = "entry_helper/report_done.html"


def _post_with_push_to_emcip(request, django_redirect_url: str):
    if report_uuid := request.POST.get("report_uuid", None):
        report = Report.objects.get(uuid=report_uuid)
        switch_report_to_done(report)

    return redirect(django_redirect_url)
