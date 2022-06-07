from entry_helper.emcip_service import BEAToEmcipService
from entry_helper.models import Report

def _prevent_edit_for_done_reports(report: Report) -> None:
    if report.status == "done":
        raise Exception("Report is already done")

def switch_report_to_done(report: Report) -> None:
    _prevent_edit_for_done_reports(report)
    try:
        BEAToEmcipService().push_report_to_emcip(report)
    except Exception as e:
        print(e)
        raise e
    else:
        report.status = "done"
        report.save()


def switch_report_to_ignored(report: Report) -> None:
    _prevent_edit_for_done_reports(report)
    report.status = "ignored"
    report.save()


def switch_report_to_todo(report: Report) -> None:
    _prevent_edit_for_done_reports(report)
    report.status = "todo"
    report.save()
