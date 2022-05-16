from django.shortcuts import render


def index(request):
    reports = [
        "Report 1",
        "Report 2",
        "Report 3",
    ]
    context = {'reports': reports, 'button_data': {'label': 'Label of the button item', 'onclick': "alert('button doing stuff')"}}
    return render(request, 'entry_helper/index.html', context)
