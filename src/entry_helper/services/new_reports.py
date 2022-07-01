from datetime import datetime, timedelta

from sqlalchemy.engine import Engine

from entry_helper.models import Report


class RawReportsClient:
    """
    A service able to gather preprocessed incident reports.

    It requires an engine to connect to the database containing incident reports.
    """
    def __init__(self, engine: Engine):
        self.engine = engine
        self.last_import_datetime: datetime = None

    @classmethod
    def from_engine(cls, engine: Engine) -> "RawReportsClient":
        """
        Initialize a client based on an sqlalchemy Engine.
        """
        return cls(engine=engine)

    def retrieve_new_reports(self) -> list[Report]:
        """
        Retrieve new reports if there are some available without saving them.
        """
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
        """
        Store provided reports
        """
        for report in reports:
            report.save()

    def import_new_reports(self) -> None:
        """
        Import and store new reports
        """
        new_reports = self.retrieve_new_reports()
        self.store_reports(new_reports)
        self.last_import_datetime = datetime.now()
        return

    def update_refresh_list_based_on_last_update_datetime(
        self,
        refresh_interval: timedelta = timedelta(hours=1),
    ) -> None:
        """
        Helper method handling "intelligent" import of new reports based on the last registered update.

        refresh_interval can be configured through a builtin timedelta object configured at 1 hour by default.
        """
        def is_time_to_refresh_reports(refresh_interval: timedelta) -> bool:
            if self.last_import_datetime is None:
                return True

            return bool(datetime.now() > (self.last_import_datetime + refresh_interval))

        if not is_time_to_refresh_reports(refresh_interval):
            return

        self.import_new_reports()
        return
