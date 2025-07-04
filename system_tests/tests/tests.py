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
        expected_system_id = 12345
        self.ca.assert_that_pv_is("ID", expected_system_id, timeout=10) # timeout to cover 10s SCAN of record.  Value returned in ~9s.

#    def test_WHEN_raw_data_requested_THEN_value_returned(self):
#        expected_raw_data = "1,1,280.0,280.0,1006,286,0,972"
#        self.ca.assert_that_pv_is("DATA:RAW", expected_raw_data, timeout=2) # timeout to cover 1s SCAN of record.  Value returned in <1s.
#
#    def test_WHEN_raw_status_requested_THEN_value_returned(self):
#        expected_raw_status = "1,2,3,4,5"
#        self.ca.assert_that_pv_is("STATUS:RAW", expected_raw_status, timeout=2) # timeout to cover 1s SCAN of record.  Value returned in <1s.

#   Tests for record redirection from returned data string

    def test_WHEN_data_requested_THEN_address_returned_and_PV_populated(self):
        expected_address = 3
        self.ca.assert_that_pv_is("ADDRESS:RBV", expected_address, timeout=2) # timeout to cover 1s SCAN of record.  Value returned in <1s.

    def test_WHEN_data_requested_THEN_heat_status_returned_and_PV_populated(self):
        expected_heat_status = "ON"
        self.ca.assert_that_pv_is("HEAT:RBV", expected_heat_status, timeout=2)

    def test_WHEN_data_requested_THEN_tank_current_setpoint_returned_and_PV_populated(self):
        expected_tank_current_setpoint = 285.0
        self.ca.assert_that_pv_is("TANK:CURR:SP:RBV", expected_tank_current_setpoint, timeout=2)

    def test_WHEN_data_requested_THEN_tank_current_returned_and_PV_populated(self):
        expected_tank_current = 280.0
        self.ca.assert_that_pv_is("TANK:CURR:RBV", expected_tank_current, timeout=2)

    def test_WHEN_data_requested_THEN_power_returned_and_PV_populated(self):
        expected_power = 1006
        self.ca.assert_that_pv_is("POWER:RBV", expected_power, timeout=2)

    def test_WHEN_data_requested_THEN_frequency_returned_and_PV_populated(self):
        expected_frequency = 286
        self.ca.assert_that_pv_is("FREQ:RBV", expected_frequency, timeout=2)

    def test_WHEN_data_requested_THEN_count_down_timer_returned_and_PV_populated(self):
        expected_count_down_timer = 0
        self.ca.assert_that_pv_is("TIMER:DOWN:RBV", expected_count_down_timer, timeout=2)

    def test_WHEN_data_requested_THEN_count_up_timer_returned_and_PV_populated(self):
        expected_count_up_timer = 972
        self.ca.assert_that_pv_is("TIMER:UP:RBV", expected_count_up_timer, timeout=2)
