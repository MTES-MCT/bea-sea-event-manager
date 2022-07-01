from entry_helper.emcip_service import BEAToEmcipService, AttributeMapping
from entry_helper.models import Report

attribute_mapping_config = AttributeMapping.from_dict(
    {
        "occurrence_date": {
            "nodes_breadcrumb": ["TE-28"],
            "code": "TA-346",
            "regex": "^[12][901][0-9][0-9]-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T00:00Z$"
        },
    }
)


def _prevent_edit_for_done_reports(report: Report) -> None:
    if report.status == "done":
        raise Exception("Report is already done")


def switch_report_to_done(report: Report) -> None:
    _prevent_edit_for_done_reports(report)
    BEAToEmcipService(attributes_mapping=attribute_mapping_config).push_report_to_emcip(
        report
    )
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
