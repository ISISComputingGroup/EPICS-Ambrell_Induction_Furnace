from lewis.adapters.stream import StreamInterface, Cmd
from lewis.utils.command_builder import CmdBuilder
from lewis.core.logging import has_log
from lewis.utils.replies import conditional_reply

if_connected = conditional_reply("connected")

@has_log
class Ambrell_Easy_HeatStreamInterface(StreamInterface):
    
    in_terminator = "\r"
    
    out_prefix = "\r\n"
    out_terminator = "\r\n"

    def __init__(self):
        super(Ambrell_Easy_HeatStreamInterface, self).__init__()
        # Commands that we expect via serial during normal operation
        self.commands = {
            # CmdBuilder(self.catch_all).arg("^#9.*$").eos().build(),  # Catch-all command for debugging
            CmdBuilder(self.get_id, ignore_case=True).int().escape(",SYSID").eos().build(), # get system ID
            CmdBuilder(self.get_data, ignore_case=True).int().escape(",RDATA").eos().build(), # get raw data
            CmdBuilder(self.get_status, ignore_case=True).int().escape(",STAT").eos().build(), # get raw status
        }

    def handle_error(self, request, error):
        """
        If command is not recognised print and error

        Args:
            request: requested string
            error: problem

        """
        self.log.error("An error occurred at request " + repr(request) + ": " + repr(error))

    def catch_all(self, command):
        pass
   
    @if_connected
    def get_id(self, address):
        return self.out_prefix + str(self.device.id)
    
    @if_connected
    def get_data(self, address):
        return self.out_prefix + self.device.data

    @if_connected
    def get_status(self, address):
        return self.out_prefix + self.device.status
