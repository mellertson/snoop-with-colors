#!/usr/bin/python

import sys
import socket
from subprocess import Popen, PIPE

class Application(object):
    default_color1 = 31
    default_color2 = 32
    def __init__(self, color1=31, color2=32):
        hostname = self.getHostname()
        self.cmds = [
            ["tcpdump", "-i", "any"],
            ["GREP_COLORS='sl={}:mt={}'".format(color1, color1), "egrep", "-i", "> {}".format(hostname), "--line-buffered", "-B20"],
            ["GREP_COLORS='sl={}:mt={}'".format(color2, color2), "egrep", "-i", "> {}".format(hostname), "--line-buffered", "-B20"]
        ]
    def getHostname(self):
        """
        Gets the system's host name.
        :return hostname: as a string
        """
        return str(socket.gethostname())
    def parseArgs(self):
        """
        Parse command line aguments into a dictionary and return it
        :return myArgs: [] of parsed arguments
        """
        myArgs = []
        if len(sys.argv) != 3:
            raise RuntimeError("Incorrect number of command line arguments.")
        
        for i in range(1, len(sys.argv)):
            myArgs.append(sys.argv[i])
        return myArgs
    def run(self, args):
        args = self.parseArgs()
        
        # color code for outbound communications
        
    
        
    
    # tcpdump -i any | GREP_COLORS="\"$ICOLORS\"" egrep -i '> CodeHammer' --line-buffered -B20 | GREP_COLORS="\"$OCOLORS\"" egrep -i 'IP CodeHammer' --line-buffered -B20
    # echo "command is: $OUTPUT"
    # the following is a working example:
    # sudo tcpdump -i any | GREP_COLORS="sl=31:mt=32" egrep -i '> CodeHammer' --line-buffered -B20 | GREP_COLORS="sl=32:mt=32" egrep -i 'IP CodeHammer' --line-buffered -B20
    
    def _call_on_command_line(self, cmd=[]):
        """
        Simulates executing a command via terminal, passing it command line arguments
        Used only by this test case.
        :param cmd: the command line and arguments as a []
        :return stdout, stderr:
        """
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        return stdout, stderr
    
if __name__ == "__main__":
    app = Application()
    try:
        args = app.parseArgs()
    except RuntimeError as e:
        app.printUsage()
        exit(0)
    
    app.run(args)
        