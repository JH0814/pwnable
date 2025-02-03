from pwn import *

p = ssh('col', 'pwnable.kr', 2222, 'guest')

path = './col'
argv = p32(0x6C5CEC8) * 4
argv += p32(0x6C5CECC)

payload = [path, argv]
s = p.run(payload)
s.interactive()