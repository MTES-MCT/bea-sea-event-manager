from django.shortcuts import render


def index(request):
    reports = [
        "Report 1",
        "Report 2",
        "Report 3",
    ]
    context = {'reports': reports, 'button_data': {'label': 'Label of the button item', 'onclick': "alert('button doing stuff')"}}
    return render(request, 'entry_helper/index.html', context)


from django.views.generic import ListView

from entry_helper.models import Report


class ReportListView(ListView):
    model = Report
