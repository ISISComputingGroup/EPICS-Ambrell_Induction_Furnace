import unittest

from utils.channel_access import ChannelAccess  # pyright: ignore
from utils.ioc_launcher import get_default_ioc_dir  # pyright: ignore
from utils.test_modes import TestModes  # pyright: ignore
from utils.testing import get_running_lewis_and_ioc, skip_if_recsim  # pyright: ignore

DEVICE_PREFIX = "AMBRHEAT_01"


IOCS = [
    {
        "name": DEVICE_PREFIX,
        "directory": get_default_ioc_dir("AMBRHEAT"),
        "macros": {"ADDRESS": 3},
        "emulator": "ambrell_easy_heat",
    },
]


TEST_MODES = [TestModes.RECSIM, TestModes.DEVSIM]


class AmbrellEasyHeatTests(unittest.TestCase):
    """
    Tests for the AMBRHEAT IOC.
    """

    def setUp(self):
        self._lewis, self._ioc = get_running_lewis_and_ioc("ambrell_easy_heat", DEVICE_PREFIX)
        self.ca = ChannelAccess(device_prefix=DEVICE_PREFIX)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_system_id_requested_THEN_value_returned(self):
        expected_system_id = 54321
        self._lewis.backdoor_set_on_device("id", expected_system_id)
        self.ca.assert_that_pv_is(
            "ID", expected_system_id, timeout=10
        )  # timeout to cover 10s SCAN of record.  Value returned in ~9s.

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_data_requested_THEN_address_returned_and_PV_populated(self):
        expected_address = 4
        self._lewis.backdoor_set_on_device("address", expected_address)
        self.ca.assert_that_pv_is(
            "ADDRESS:RBV", expected_address, timeout=2
        )  # timeout to cover 1s SCAN of record.  Value returned in <1s.

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_data_requested_THEN_heat_status_returned_and_PV_populated(self):
        expected_heat_status = "OFF"
        self._lewis.backdoor_set_on_device("heat_status", expected_heat_status)
        self.ca.assert_that_pv_is("HEAT:RBV", expected_heat_status, timeout=2)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_data_requested_THEN_tank_current_setpoint_returned_and_PV_populated(self):
        expected_tank_current_setpoint = 185.0
        self._lewis.backdoor_set_on_device("tank_current_setpoint", expected_tank_current_setpoint)
        self.ca.assert_that_pv_is("TANK:CURR:SP:RBV", expected_tank_current_setpoint, timeout=2)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_data_requested_THEN_tank_current_returned_and_PV_populated(self):
        expected_tank_current = 180.0
        self._lewis.backdoor_set_on_device("tank_current", expected_tank_current)
        self.ca.assert_that_pv_is("TANK:CURR:RBV", expected_tank_current, timeout=2)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_data_requested_THEN_power_returned_and_PV_populated(self):
        expected_power = 2006
        self._lewis.backdoor_set_on_device("power", expected_power)
        self.ca.assert_that_pv_is("POWER:RBV", expected_power, timeout=2)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_data_requested_THEN_frequency_returned_and_PV_populated(self):
        expected_frequency = 186
        self._lewis.backdoor_set_on_device("frequency", expected_frequency)
        self.ca.assert_that_pv_is("FREQ:RBV", expected_frequency, timeout=2)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_data_requested_THEN_count_down_timer_returned_and_PV_populated(self):
        expected_count_down_timer = 15
        self._lewis.backdoor_set_on_device("count_down", expected_count_down_timer)
        self.ca.assert_that_pv_is("TIME:DOWN:RBV", expected_count_down_timer, timeout=2)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_data_requested_THEN_count_up_timer_returned_and_PV_populated(self):
        expected_count_up_timer = 872
        self._lewis.backdoor_set_on_device("count_up", expected_count_up_timer)
        self.ca.assert_that_pv_is("TIME:UP:RBV", expected_count_up_timer, timeout=2)


    #   Tests for record redirection from returned status string

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_status_requested_THEN_mains_voltage_returned_and_PV_populated(self):
        expected_mains_voltage = 120.0
        self._lewis.backdoor_set_on_device("mains_voltage", expected_mains_voltage)
        self.ca.assert_that_pv_is(
            "VOLT:MAINS:RBV", expected_mains_voltage, timeout=2
        )  # timeout to cover 1s SCAN of record.  Value returned in <1s.

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_status_requested_THEN_total_time_returned_and_PV_populated(self):
        expected_total_time = 43.6
        self._lewis.backdoor_set_on_device("total_time", expected_total_time)
        self.ca.assert_that_pv_is("TIME:TOTAL:RBV", expected_total_time, timeout=2)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_status_requested_THEN_maximum_power_returned_and_PV_populated(self):
        expected_maximum_power = 521.2
        self._lewis.backdoor_set_on_device("max_power", expected_maximum_power)
        self.ca.assert_that_pv_is("POWER:MAX:RBV", expected_maximum_power, timeout=2)

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_status_requested_THEN_maximum_heatsink_temperature_returned_and_PV_populated(
        self,
    ):
        expected_maximum_heatsink_temperature = 77.9
        self._lewis.backdoor_set_on_device("max_heatsink_temp", expected_maximum_heatsink_temperature)
        self.ca.assert_that_pv_is(
            "TEMP:HEATSINK:MAX:RBV", expected_maximum_heatsink_temperature, timeout=2
        )

    @skip_if_recsim("Lewis backdoor not available in RecSim")
    def test_WHEN_status_requested_THEN_maximum_enclosure_temperature_returned_and_PV_populated(
        self,
    ):
        expected_maximum_enclosure_temperature = 52.8
        self._lewis.backdoor_set_on_device("max_enclosure_temp", expected_maximum_enclosure_temperature)
        self.ca.assert_that_pv_is(
            "TEMP:ENCLOSURE:MAX:RBV", expected_maximum_enclosure_temperature, timeout=2
        )
