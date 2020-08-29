from datetime import datetime, date, timedelta, time, timezone
import os
from crunchapilyb import *


def test_crunch_api_lyb():
    current_date = datetime.combine(date.today(), time(0, 0, 0))
    past_date = current_date - timedelta(days=15)
    timestamp_utc = past_date.replace(tzinfo=timezone.utc).timestamp()

    df1 = crunch_api_ppl(500, since_time=int(timestamp_utc),
                         csv_name="test_people.csv")
    df2 = crunch_api_org(since_time=int(timestamp_utc),
                         locations="Chicago", csv_name="test_org.csv")

    # If not empty, df1 and df2 should have positive lengths (not over
    # the appointed number), with relevant .csv files created.
    assert(df1 is None or
           (0 < len(df1) <= 500 and os.path.exists("test_people.csv")))
    assert(df2 is None or
           (len(df1) > 0 and os.path.exists("test_org.csv")))

    print("OK")


if __name__ == "__main__":
    test_crunch_api_lyb()