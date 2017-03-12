from subprocess import Popen, PIPE

class System(object):
	"""
	This class contains system call and system methods.
	"""
	def _callOnCommandLine(self, cmd=[]):
		"""
		Simulates executing a command via terminal, passing it command line arguments
		Used only by this test case.
		:param cmd: the command line and arguments as a []
		:return stdout, stderr:
		"""
		p = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE)
		stdout, stderr = p.communicate()
		return stdout, stderr