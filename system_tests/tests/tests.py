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

    # def test_that_fails(self):
    #    self.fail("You haven't implemented any tests!")

    def test_WHEN_system_id_requested_THEN_value_returned(self):
        expected_system_id = 12345
        self.ca.assert_that_pv_is("ID", expected_system_id, timeout=2)
