import unittest
from snoop_with_colors.system import System as Sys


class callOnCommandLine_TestCase(unittest.TestCase):

	def setUp(self):
		self.app = Sys()

	def test_return_values(self):
		cmd = ["echo", "hello"]
		result = [self.app._callOnCommandLine(cmd=cmd)]
		self.assertEqual(result[0][0], "hello\n")
		self.assertEqual(len(result[0][1]), 0)
		
		
if __name__ == '__main__':
	unittest.main()


