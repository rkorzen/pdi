import paramiko
import os
hostname = "frog01.mikr.us"
port = 12125
username = "frog"
password = os.getenv("PASSWORD")

transport = paramiko.Transport((hostname, port))
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)

# sftp.get("remotefile.txt", "localfile.txt")
sftp.put("json_example.py", "json_example.py")

sftp.close()
transport.close()
