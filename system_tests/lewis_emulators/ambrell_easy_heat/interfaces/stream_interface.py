from lewis.adapters.stream import StreamInterface, Cmd
from lewis.utils.command_builder import CmdBuilder
from lewis.core.logging import has_log
from lewis.utils.replies import conditional_reply

if_connected = conditional_reply("connected")

@has_log
class Ambrell_Easy_HeatStreamInterface(StreamInterface):
    
    in_terminator = "\r"
    start_reply = "\r\n"
    out_terminator = "\r\n"

    def __init__(self):
        super(Ambrell_Easy_HeatStreamInterface, self).__init__()
        # Commands that we expect via serial during normal operation
        self.commands = {
            CmdBuilder(self.catch_all).arg("^#9.*$").build(),  # Catch-all command for debugging
            CmdBuilder(self.get_id).int().escape(",SYSID").build(), # get system ID
            CmdBuilder(self.get_data).int().escape(",RDATA").build(), # get raw data
            CmdBuilder(self.get_status).int().escape(",STAT").build(), # get raw status
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
        reply = self.start_reply + self.device.address + "," + self.device.id
        print("Start reply_",reply,"_End reply")
        return reply
    
    @if_connected
    def get_data(self, address):
        return self.start_reply + self.device.address + "," + self.device.data

    @if_connected
    def get_status(self, address):
        return self.start_reply + self.device.address + "," + self.device.status
