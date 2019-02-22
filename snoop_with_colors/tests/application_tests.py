import unittest
import sys
from snoop_with_colors.application import Application as App


class init_TestCase(unittest.TestCase):
	"""
	Test case for SnoopWithColors.Application.__init__() method
	"""
	def setUp(self):
		self.app = App()

	def test_default_return_values(self):
		hostname = self.app.getHostname()
		
		# verify values in command 1
		cmd = self.app.cmds[0]
		self.assertEqual(cmd[0], "tcpdump")
		self.assertEqual(cmd[1], "-i")
		self.assertEqual(cmd[2], "any")
		
		# verify values in command 2
		cmd = self.app.cmds[1]
		self.assertEqual(cmd[0], "GREP_COLORS=sl={}:mt={}".format(App.default_color1, App.default_color1))
		self.assertEqual(cmd[1], "egrep")
		self.assertEqual(cmd[2], "-i")
		self.assertEqual(cmd[3], '"> {}"'.format(hostname))
		self.assertEqual(cmd[4], "--line-buffered")
		self.assertEqual(cmd[5], "-B20")
		
		# verify values in command 3
		cmd = self.app.cmds[2]
		self.assertEqual(cmd[0], "GREP_COLORS=sl={}:mt={}".format(App.default_color2, App.default_color2))
		self.assertEqual(cmd[1], "egrep")
		self.assertEqual(cmd[2], "-i")
		self.assertEqual(cmd[3], '"IP {}"'.format(hostname))
		self.assertEqual(cmd[4], "--line-buffered")
		self.assertEqual(cmd[5], "-B20")

	def test_default_return_values___using_different_color_codes(self):
		hostname = self.app.getHostname()
		app = App(32, 33)
		# verify values in command 2
		cmd = app.cmds[1]
		self.assertEqual(cmd[0], 'GREP_COLORS=sl={}:mt={}'.format(32, 32))
		self.assertEqual(cmd[1], "egrep")
		self.assertEqual(cmd[2], "-i")
		self.assertEqual(cmd[3], '"> {}"'.format(hostname))
		self.assertEqual(cmd[4], "--line-buffered")
		self.assertEqual(cmd[5], "-B20")
		
		# verify values in command 3
		cmd = app.cmds[2]
		self.assertEqual(cmd[0], 'GREP_COLORS=sl={}:mt={}'.format(33, 33))
		self.assertEqual(cmd[1], "egrep")
		self.assertEqual(cmd[2], "-i")
		self.assertEqual(cmd[3], '"IP {}"'.format(hostname))
		self.assertEqual(cmd[4], "--line-buffered")
		self.assertEqual(cmd[5], "-B20")


class command_TestCase(unittest.TestCase):

	def setUp(self):
		self.app = App(31, 32)

	def test_get_command(self):
		host = self.app.getHostname()
		expected = """tcpdump -i any | \
GREP_COLORS=sl=31:mt=31 egrep -i "> {}" --line-buffered -B20 --color=always | \
GREP_COLORS=sl=32:mt=32 egrep -i "IP {}" --line-buffered -B20 --color=always\
""".format(host, host)
		cmd = self.app.command
		self.assertEqual(expected, cmd, "Expected:\n{}\nbut got:\n{}\n".format(expected, cmd))


class getHostname_TestCase(unittest.TestCase):
	"""
	Test case for SnoopWithColors.Application.getHostName() method
	"""

	def setUp(self):
		self.app = App()

	def test_return_value(self):
		import socket
		hostname = socket.gethostname()
		result = self.app.getHostname()
		self.assertEqual(hostname, self.app.getHostname(), "Exepcted {} as hostname, but got {}".format(hostname, result))


class parseArgs_TestCase(unittest.TestCase):
	"""
	Test case for SnoopWithColors.Application.parseArgs() method
	"""

	def setUp(self):
		self.app = App()

	def test_exceptions_handling(self):
		"""
		Test exception handling of SnoopWithColors.Application.parseArgs() method
		"""
		argv = sys.argv
		
		# test parse args with no command line arguments
		sys.argv = argv[0:1]
		with self.assertRaises(RuntimeError):
			self.app.parseArgs()
			
		# test parse args with one command line argument
		sys.argv = argv[0:1]
		sys.argv.append(31)
		with self.assertRaises(RuntimeError):
			self.app.parseArgs()
			
		# test parse args with two command line arguments
		sys.argv = argv[0:1]
		sys.argv.append(31)
		sys.argv.append(32)
		# should not raise
		self.app.parseArgs()
			
		# test parse args with three command line arguments
		sys.argv = argv[0:1]
		sys.argv.append(31)
		sys.argv.append(32)
		sys.argv.append(33)
		with self.assertRaises(RuntimeError):
			self.app.parseArgs()
			
		# restore the original command line arguments
		sys.argv=argv

	def test_return_value(self):
		"""
		Test the return value of SnoopWithColors.Application.parseArgs()
		"""
		argv = sys.argv
		
		# test parse args with no command line arguments
		sys.argv = argv[0:1]
		sys.argv.append(31)
		sys.argv.append(32)
		args = self.app.parseArgs()
		
		# verify the number of args returned
		self.assertEqual(len(args), 2, "Expected 2 command line args, but got {}".format(len(args)))
		
		# verify the values of the returned args
		self.assertEqual(args[0], 31)
		self.assertEqual(args[1], 32)
		
		# restore the original command line arguments
		sys.argv=argv


class run_TestCase(unittest.TestCase):
	"""
	Test case for SnoopWithColors.Application.run() method
	"""

	def setUp(self):
		self.app = App()

	
if __name__ == '__main__':
	unittest.main()



