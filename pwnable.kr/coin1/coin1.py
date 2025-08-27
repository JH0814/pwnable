from pwn import *

s = ssh('coin1', 'pwnable.kr', 2222, 'guest')
p = s.remote('localhost', 9007)
p.recvuntil(b"starting in 3 sec... -\n")
for t in range(100):
    print(f"{t + 1}th Game")
    p.recvuntil("N=")
    N = int(p.recvuntil(" "))
    p.recvuntil("C=")
    C = int(p.recvuntil("\n"))

    arr = list(range(N))
    for i in range(C):
        if len(arr) > 1:
            mid = (len(arr) + 1) // 2
            weigh = arr[:mid]
            other = arr[mid:]
            payload = ' '.join(map(str, weigh))
            p.sendline(payload.encode())
            res = int(p.recvline().decode().strip())

            exp = len(weigh) * 10
            if res < exp:
                arr = weigh
            else:
                arr = other
        else:
            p.sendline(b'0')
            p.recvline()
    answer = arr[0]
    p.sendline(str(answer).encode())
p.interactive()
