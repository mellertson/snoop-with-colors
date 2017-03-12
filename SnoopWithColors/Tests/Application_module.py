import unittest
import sys
from SnoopWithColors.Application import Application

class TestCase_parseArgs(unittest.TestCase):
	def setUp(self):
		self.app = Application()
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


if __name__ == '__main__':
	unittest.main()
