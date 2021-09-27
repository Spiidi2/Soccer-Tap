"""Tests init and discovery features for tap-soccer."""

import datetime
from pathlib import Path



from tap_soccer.tap import TapSoccer

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "filepath": str(Path(__file__).parent / "resources/testfile.soccer"),
}

