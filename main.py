#!/usr/bin/env python3

from datetime import datetime
import pandas as pd

from aw_core.models import Event
from aw_client import ActivityWatchClient


def row_to_event(row):
    timestamp = datetime.fromtimestamp(row['activityStartDate [ms]'] / 1000).isoformat()
    duration = row['activityDuration [ms]'] / 1000
    data = {
        'name': row['activityName'],
        # 'category': row['activityCategoryName'],
    }

    return Event(timestamp=timestamp, duration=duration, data=data)


def get_events():
    smt_dataset = pd.read_csv('smt_export.csv')
    return [row_to_event(row) for _, row in smt_dataset.iterrows()]


if __name__ == "__main__":
    events = get_events()

    aw = ActivityWatchClient(testing=False)
    bucket_name = 'savemytime'

    if bucket_name in aw.get_buckets():
        # aw.delete_bucket(bucket_name)
        print(f'NOTE: "{bucket_name}" already exists')

    aw.create_bucket(bucket_name, event_type='calendar')  # TODO: sensible event_type?
    aw.insert_events(bucket_name, events)

    print(f'Done – processed {len(events)} events.')
