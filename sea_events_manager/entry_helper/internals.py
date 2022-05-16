def switch_report_to_done(report):
    report.status = "done"
    report.save()
