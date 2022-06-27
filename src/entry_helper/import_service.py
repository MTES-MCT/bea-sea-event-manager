from datetime import datetime, timedelta

from sqlalchemy.engine import Engine, create_engine

from entry_helper.models import Report

engine = create_engine("postgresql://cibnav_user:cibnav_pwd@localhost:5432/cibnav_test")


class RawReportsClient:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.last_import_datetime: datetime = None

    @classmethod
    def from_engine(cls, engine: Engine) -> "RawReportsClient":
        return cls(engine=engine)

    def retrieve_new_reports(self) -> list[Report]:
        def retrieve_eligible_new_reports() -> list[Report]:
            raw_reports_table_name = "seamis_reports_with_ship"
            with self.engine.connect() as conn:
                raw_reports = (
                    conn.execute(f"SELECT * FROM {raw_reports_table_name}")
                    .mappings()
                    .all()
                )
                return [Report.from_raw_report(raw_report) for raw_report in raw_reports]

        def is_new_report(report: Report) -> bool:
            return not Report.objects.filter(
                report_number=report.report_number,
                registration_number=report.registration_number,
            ).exists()

        return [
            new_report
            for new_report in retrieve_eligible_new_reports()
            if is_new_report(new_report)
        ]

    def store_reports(self, reports: list[Report]) -> None:
        for report in reports:
            report.save()

    def update_refresh_list_based_on_last_update_datetime(
        self,
        refresh_interval: timedelta = timedelta(hours=1),
    ) -> None:
        print("try to update")
        def is_time_to_refresh_reports(refresh_interval: timedelta) -> bool:
            if self.last_import_datetime is None:
                self.last_import_datetime = datetime.now()
                return True

            return bool(datetime.now() > (self.last_import_datetime + refresh_interval))

        if not is_time_to_refresh_reports(refresh_interval):
            return

        new_reports = self.retrieve_new_reports()
        self.store_reports(new_reports)
        return
