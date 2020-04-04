import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname="10.60.17.183", port=22,
#             username="ouyeel_trans1", password="ouyeel_trans1")
# stdin, stdout, stderr = ssh.exec_command("tail -100 jetty/applications/logs/service-server.log")
ssh.connect(hostname="192.168.1.102", port=22,
            username="root", password="123")
stdin, stdout, stderr = ssh.exec_command("ls -l /tmp")

print(stdout.read().decode())
