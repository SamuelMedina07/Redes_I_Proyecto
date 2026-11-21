#include<stdio.h>
#include<stdlib.h>
int main()
          {
           FILE *pf=fopen("estado17.txt","w");
           if (pf==NULL)
                        {
                          printf("Error al Abrir el Archivo\n");
                        }
           //Escribir en el arhivo17.txt
           fprintf(pf,"%d",1);
           fprintf(pf,"\n");
           fclose(pf);
            
           printf(" Se escribio el valor 0 exitosamente en el Archivo\n");
           return 0;
           
          } // fin de la funcion main          
