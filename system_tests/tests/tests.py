import unittest

from utils.channel_access import ChannelAccess
from utils.ioc_launcher import get_default_ioc_dir
from utils.test_modes import TestModes
from utils.testing import get_running_lewis_and_ioc, skip_if_recsim


DEVICE_PREFIX = "AMBRHEAT_01"


IOCS = [
    {
        "name": DEVICE_PREFIX,
        "directory": get_default_ioc_dir("AMBRHEAT"),
        "macros": {"ADDRESS":3},
        "emulator": "ambrell_easy_heat",
    },
]


TEST_MODES = [TestModes.RECSIM, TestModes.DEVSIM]


class Ambrell_Easy_HeatTests(unittest.TestCase):
    """
    Tests for the AMBRHEAT IOC.
    """
    def setUp(self):
        self._lewis, self._ioc = get_running_lewis_and_ioc("ambrell_easy_heat", DEVICE_PREFIX)
        self.ca = ChannelAccess(device_prefix=DEVICE_PREFIX)

    def test_WHEN_system_id_requested_THEN_value_returned(self):
        expected_system_id = "12345"
        self.ca.assert_that_pv_is("ID", expected_system_id, timeout=10) # timeout to cover 10s SCAN of record.  Value returned in ~9s.

    def test_WHEN_raw_data_requested_THEN_value_returned(self):
        expected_raw_data = "1,1,280.0,280.0,1006,286,0,972"
        self.ca.assert_that_pv_is("DATA:RAW", expected_raw_data, timeout=2) # timeout to cover 1s SCAN of record.  Value returned in <1s.

    def test_WHEN_raw_status_requested_THEN_value_returned(self):
        expected_raw_status = "1,2,3,4,5"
        self.ca.assert_that_pv_is("STATUS:RAW", expected_raw_status, timeout=2) # timeout to cover 1s SCAN of record.  Value returned in <1s.
