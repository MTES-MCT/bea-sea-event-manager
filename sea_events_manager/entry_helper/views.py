from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from entry_helper.models import Report
from entry_helper.internals import switch_report_to_done

from data_scripts.setup_bea_fake_data import task_load_fake_bea_data_into_django


class ReportListView(LoginRequiredMixin, ListView):
    model = Report

    ordering = ["-event_datetime"]

    login_url = '/admin/login/'


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
        _post_with_push_to_emcip(request, "entry_helper:reports")


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
        _post_with_push_to_emcip(request, django_redirect_url="entry_helper:reports_ignored")


def _post_with_push_to_emcip(request, django_redirect_url: str):
    if report_uuid := request.POST.get("report_uuid", None):
        report = Report.objects.get(uuid=report_uuid)
        switch_report_to_done(report)

    return redirect(django_redirect_url)
