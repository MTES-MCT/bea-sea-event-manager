from django.shortcuts import render, redirect


def index(request):
    reports = [
        "Report 1",
        "Report 2",
        "Report 3",
    ]
    context = {
        "reports": reports,
        "button_data": {
            "label": "Label of the button item",
            "onclick": "alert('button doing stuff')",
        },
    }
    return render(request, "entry_helper/index.html", context)


from django.views.generic import ListView

from entry_helper.models import Report
from entry_helper.internals import switch_report_to_done


class ReportTodoListView(ListView):
    model = Report
    queryset = Report.objects.filter(status="todo")

    ordering = ["-event_datetime"]

    def post(self, request):
        if report_uuid := request.POST.get("report_uuid", None):
            report = Report.objects.get(uuid=report_uuid)
            switch_report_to_done(report)

        return redirect("entry_helper:reports")
