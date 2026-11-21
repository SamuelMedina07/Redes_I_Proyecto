section .data
   comando db "/usr/bin/curl -s http://192.168.88.100/off", 0

section .text
   global main
   extern system

main:
     push rbp
     mov rbp, rsp

     lea rdi, [rel comando]
     call system

     xor eax, eax
     pop rbp
     ret
