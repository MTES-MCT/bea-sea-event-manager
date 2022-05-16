from django.shortcuts import redirect
from django.views.generic import ListView

from entry_helper.models import Report
from entry_helper.internals import switch_report_to_done
from django.contrib.auth.mixins import LoginRequiredMixin


class ReportTodoListView(LoginRequiredMixin, ListView):
    model = Report
    queryset = Report.objects.filter(status="todo")

    template_name: str = "entry_helper/report_todo.html"
    login_url = '/admin/login/'

    ordering = ["-event_datetime"]

    def post(self, request):
        if report_uuid := request.POST.get("report_uuid", None):
            report = Report.objects.get(uuid=report_uuid)
            switch_report_to_done(report)

        return redirect("entry_helper:reports")


class ReportDoneListView(LoginRequiredMixin, ListView):
    model = Report
    queryset = Report.objects.filter(status="done")

    template_name: str = "entry_helper/report_done.html"
    login_url = '/admin/login/'

    ordering = ["-event_datetime"]
