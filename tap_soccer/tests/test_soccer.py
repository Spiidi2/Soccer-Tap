"""Test sample sync."""



from tap_soccer.tap import TapSoccer

COUNTER = 0

SAMPLE_FILENAME = "/tmp/testfile.soccer"
SAMPLE_CONFIG = {"filepath": SAMPLE_FILENAME}
SAMPLE_CONFIG_BAD = {"not_valid": SAMPLE_FILENAME}



