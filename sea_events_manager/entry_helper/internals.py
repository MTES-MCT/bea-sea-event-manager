def switch_report_to_done(report):
    report.status = "done"
    report.save()


def switch_report_to_ignored(report):
    report.status = "ignored"
    report.save()


def switch_report_to_todo(report):
    report.status = "todo"
    report.save()
