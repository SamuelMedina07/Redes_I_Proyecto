#include<stdio.h>
#include<stdlib.h>
int main()
         {
          FILE *pf=fopen("estado17.txt","w");
 
          if (pf==NULL)
                      { 
                       printf("ERROR,AL ABRIR EL ARCHIVO \n");
                      
                      }
          // Escribir 1 o 0 en el archivo estado17.txt
          fprintf(pf,"%d",0);
          fprintf(pf,"\n");
          fclose(pf);
          
          printf("Se Escribio el valor Correctamente en el Archivo \n");
          return 0;
} // fin del programa
