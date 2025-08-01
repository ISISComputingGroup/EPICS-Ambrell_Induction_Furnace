from collections import OrderedDict

from lewis.devices import StateMachineDevice

from .states import DefaultState


class SimulatedAmbrellEasyHeat(StateMachineDevice):
    def _initialize_data(self) -> None:
        """
        Initialize all of the device's attributes.
        """
        self.connected = True

        self.id = 12345

        # Values in data string:

        self.address = 3

        self.heat_status = 1

        self.tank_current_setpoint = 285.0

        self.tank_current = 280.0

        self.power = 1006

        self.frequency = 286

        self.count_down = 0

        self.count_up = 972

        # Power supply address, heat on (1=on, 0=off), set point amps, tank amps, power watts,
        # frequency kHz, count down timer (msec.), count up timer (msec.)
        #
        # Example reply:
        # <CR><LF>1,1,280.0,280.0,1006,286,0,972<CR><LF>
        #
        # OR:
        # Possibly EcoHeat model only: PS#, KW, SETV, TANKV, KHZ, COUNTER, %MATCH, AIR TEMP,
        # HSINK TEMP, READY LED, HEAT LED, LIMIT LED, FAULT LED, TAP, MAX VOLTS, OVERLOAD,
        # TIMER, ANALOG INPUT

        self.data = f"{self.address},{self.heat_status},{self.tank_current_setpoint},{self.tank_current},{self.power},{self.frequency},{self.count_down},{self.count_up}"


        # Values in status string:

        self.mains_voltage = 220.0

        self.total_time = 53.6

        self.max_power = 421.2

        self.max_heatsink_temp = 87.9

        self.max_enclosure_temp = 62.8

        # Unclear as to exactly what is and how it is returned from the physical PSU
        # as manual is ambiguous
        # e.g Mains voltage, total time, max. power out, max. heat sink temperature,
        # max. enclosure temperature

        self.status = f"{self.mains_voltage},{self.total_time},{self.max_power},{self.max_heatsink_temp},{self.max_enclosure_temp}"


    def _get_state_handlers(self) -> dict:
        return {
            "default": DefaultState(),
        }

    def _get_initial_state(self) -> str:
        return "default"

    def _get_transition_handlers(self) -> OrderedDict:
        return OrderedDict([])
