from collections import OrderedDict

from lewis.devices import StateMachineDevice

from .states import DefaultState


class SimulatedAmbrellEasyHeat(StateMachineDevice):
    def _initialize_data(self):
        """
        Initialize all of the device's attributes.
        """
        self.connected = True

        self.address = 3

        self.heat_status = 1

        self.id = 12345

        self.data = (
            str(self.address) + "," + str(self.heat_status) + "," + "285.0,280.0,1006,286,0,972"
        )
        #
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

        self.status = "220.0,53.6,421.2,87.9,62.8"
        # Unclear as to exactly what is and how it is returned from the physical PSU
        # as manual is ambiguous
        # e.g Mains voltage, total time, max. power out, max. heat sink temperature,
        # max. enclosure temperature

    def _get_state_handlers(self) -> dict:
        return {
            "default": DefaultState(),
        }

    def _get_initial_state(self) -> str:
        return "default"

    def _get_transition_handlers(self) -> OrderedDict:
        return OrderedDict([])
