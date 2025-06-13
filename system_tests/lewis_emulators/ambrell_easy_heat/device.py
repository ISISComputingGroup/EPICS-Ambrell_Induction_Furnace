from collections import OrderedDict
from .states import DefaultState
from lewis.devices import StateMachineDevice


class SimulatedAmbrell_Easy_Heat(StateMachineDevice):

    def _initialize_data(self):
        """
        Initialize all of the device's attributes.
        """
        self.connected = True

        self.address = 3
        
        self.id = 12345

        self.data = "1,1,280.0,280.0,1006,286,0,972"
                                # PS#, KW, SETV, TANKV, KHZ, COUNTER, %MATCH, AIR TEMP,
                                # HSINK TEMP, READY LED, HEAT LED, LIMIT LED, FAULT LED, TAP, MAX VOLTS, OVERLOAD, TIMER, ANALOG INPUT
                                #
                                # OR:
                                # Power supply address, heat on (1=on, 0=off), set point amps, tank amps, power watts, frequency kHz, 
                                # count down timer (msec.), count up timer (msec.)
                                #
                                # OR:
                                # Address, heatstatus, setpoint, amps-out, frequency, timer, counter
                                #
                                # Example reply:
                                # <CR><LF>1,1,280.0,280.0,1006,286,0,972<CR><LF>
        
        self.status = "1,2,3,4,5" # Mains voltage, total time, max. power out, max. heat sink temperature, max. enclosure temperature

    def _get_state_handlers(self):
        return {
            'default': DefaultState(),
        }

    def _get_initial_state(self):
        return 'default'

    def _get_transition_handlers(self):
        return OrderedDict([])
