from netmiko import ConnectHandler
from datetime import datetime
import paramiko,sys
import getpass
import time


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host_name = 'fw1a'



user_name = 'amitrawat'
user_password ='h9'

ssh.connect (host_name, port = 22 , username =user_name , password = user_password)
transport = ssh.get_transport()
session = transport.open_session()
session.get_pty()
session.invoke_shell()
session.keep_this = ssh
session.send(b'set cli pager off \n')
time.sleep(2)
session.send(b'show routing route \n')
time.sleep(10)
x = session.recv(64999)
print (x.decode('ascii'))
session.close()

