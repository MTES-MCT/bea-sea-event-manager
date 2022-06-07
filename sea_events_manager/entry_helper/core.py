from entry_helper.emcip_service import BEAToEmcipService
from entry_helper.models import Report


def switch_report_to_done(report: Report) -> None:
    try: 
        BEAToEmcipService().push_report_to_emcip(report)
    except Exception as e:
        print(e)
        raise e
    else:
        report.status = "done"
        report.save()


def switch_report_to_ignored(report: Report) -> None:
    report.status = "ignored"
    report.save()


def switch_report_to_todo(report: Report) -> None:
    report.status = "todo"
    report.save()
