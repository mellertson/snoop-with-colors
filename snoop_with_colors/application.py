#!/usr/bin/env
import sys
import socket
import subprocess


class Application(object):
    default_color1 = 31
    default_color2 = 32

    def __init__(self, color1=31, color2=32):
        hostname = self.getHostname()
        self.cmds = [
            ["tcpdump", "-i", "any"],
            ["GREP_COLORS=sl={}:mt={}".format(color1, color1), "egrep", "-i", '"> {}"'.format(hostname), "--line-buffered", "-B20", "--color=always"],
            ["GREP_COLORS=sl={}:mt={}".format(color2, color2), "egrep", '-i', '"IP {}"'.format(hostname), "--line-buffered", "-B20", "--color=always"]
        ]

    def getHostname(self):
        """
        Gets the system's host name.
        :return hostname: as a string
        """
        return str(socket.gethostname())

    @classmethod
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

    @property
    def command(self):
        """
        Formats a string to run on the command line.
        :return cmd:
        """
        cmd = ''
        i = 0
        for command_str in self.cmds:
            for part in command_str:
                cmd += "{} ".format(part)
            i += 1
            cmd += "| " if i < len(self.cmds) else ""
        cmd = cmd.strip()
        return cmd

    def run(self):
        """
        Runs the tcpdump command on the command line and colorizes output using color codes input
        into the first two command line arguments.
        :return:
        """
        # get the command to run in a subprocess
        cmd = self.command
        print "Running command:\n{}\n".format(cmd)
        
        # run the command in a subprocess
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            out = p.stderr.read(1)
            if out == '' and p.poll() != None:
                break
            if out != '':
                sys.stdout.write(out)
                sys.stdout.flush()


if __name__ == "__main__":
    try:
        args = Application.parseArgs()
    except RuntimeError as e:
        # app.printUsage()
        print "\nAn error occurred: {}\n".format(e.message)
        raise e
    
    app = Application(color1=args[0], color2=args[1])
    app.run()
        
# TODO: Add capability to install using 'pip install snoop_with_colors'






