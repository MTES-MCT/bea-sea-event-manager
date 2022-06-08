import sqlite3
import pathlib

import pandas as pd

from entry_helper.models import Report


_columns_mapping_to_django = {
    'report_identifier': 'report_number',
    'ship_name': 'ship_name',
    'IMO_number': 'imo_number',
    'registry_number': 'registration_number',
    'declarative_entity': 'declarative_entity',
    'occurrence_location': 'event_location',
    'occurrence_date': 'event_datetime',
    'occurrence_type': 'event_type',
    'length_overall': 'ship_total_length',
    'ship_type': 'ship_type',
    'nb_deceased': 'nb_deceased',
    'nb_lost': 'nb_lost',
    'nb_injured': 'nb_injured',
}


def _extract_bea_data() -> pd.DataFrame:

    query = "SELECT * FROM seamis_report_with_ship_data"

    cwd = pathlib.Path(__file__).parent
    with sqlite3.connect(f'{cwd}/demo_data/seamis_reports_with_ships_data.db.fake.sqlite3') as conn:
        df = pd.read_sql(query, conn)

    return df


def _transform(bea_data: pd.DataFrame) -> pd.DataFrame:
    bea_data_to_keep = bea_data[list(_columns_mapping_to_django.keys())]
    return bea_data_to_keep.rename(columns=_columns_mapping_to_django)


def _load_into_django(bea_data_formated_for_django: pd.DataFrame) -> None:
    for bea_row in bea_data_formated_for_django.to_dict(orient='records'):
        if Report.objects.filter(report_number=bea_row['report_number']):
            continue

        report = Report(**bea_row)
        report.save()

def task_load_fake_bea_data_into_django():
    bea_data = _extract_bea_data()
    bea_data_formated_for_django = _transform(bea_data)
    _load_into_django(bea_data_formated_for_django)
