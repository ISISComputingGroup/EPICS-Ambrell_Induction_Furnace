import typing
from lewis.adapters.stream import StreamInterface
from lewis.core.logging import has_log
from lewis.utils.command_builder import CmdBuilder
from lewis.utils.replies import conditional_reply

from system_tests.lewis_emulators.ambrell_easy_heat.device import SimulatedAmbrellEasyHeat

if_connected = conditional_reply("connected")


@has_log
class AmbrellEasyHeatStreamInterface(StreamInterface):
    in_terminator = "\r"

    out_prefix = "\r\n"
    out_terminator = "\r\n"

    def __init__(self) -> None:
        super(AmbrellEasyHeatStreamInterface, self).__init__()
        # Commands that we expect via serial during normal operation
        self.commands = {
            # CmdBuilder(self.catch_all).arg("^#9.*$").eos().build(),
            # Catch-all command for debugging
            CmdBuilder(self.get_id, ignore_case=True)   # get system ID
            .int()
            .escape(",SYSID")
            .eos()
            .build(),
            CmdBuilder(self.get_data, ignore_case=True)  # get raw data
            .int()
            .escape(",RDATA")
            .eos()
            .build(),
            CmdBuilder(self.get_status, ignore_case=True)  # get raw status
            .int()
            .escape(",STAT")
            .eos()
            .build(),
        }
        

    def handle_error(self, request: str, error: str) -> None:
        """
        If command is not recognised print and error

        Args:
            request: requested string
            error: problem

        """
        self.log.error("An error occurred at request " + repr(request) + ": " + repr(error))

    def catch_all(self, command: str) -> None:
        pass

    @if_connected
    def get_id(self, address: int) -> str:
        return self.out_prefix + str(self.device.id)

    @if_connected
    def get_data(self, address: int) -> str:
        return self.out_prefix + self.device.data

    @if_connected
    def get_status(self, address: int) -> str:
        return self.out_prefix + self.device.status
