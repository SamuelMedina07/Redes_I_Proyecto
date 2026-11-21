section .data
  file_name  db 'estado17.txt', 0
  value  db '0',0xA, 0

section .bss
  file_handle resb 4
 
section .text
   global _start

_start:
       ;Abrir Arhivo
       mov eax, 5          ; abrir archivo
       mov ebx, file_name  ; asignar variable temporal
       mov ecx, 0x2        ; Apertura el arhivo en modo lectura y Escrituta
       int 0x80            ; llmar la funcion syscall para ejecutar la interrupcion

       mov [file_handle], eax
       
      ;Escribir el valor en el arhivo
      mov eax, 4
      mov ebx, [file_handle]
      mov ecx, value ;direccion del valor a escribir
      mov edx, 2
      int 0x80 

      ;cerra el programa
      mov eax, 6
      mov ebx, [file_handle]
      int 0x80

      ;salir o logaout
      mov eax, 1
      xor ebx, ebx
      int 0x80
