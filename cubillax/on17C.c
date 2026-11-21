#include<stdio.h>
#include<stdlib.h>
int main() {
            FILE *pf=fopen("estado17.txt","w");
            if (pf==NULL)
                         {
                          printf("ERROR AL ABRIR ARCHIVO\n");
                         }
            
            //Escribir en el arhivo estado17.txt
            fprintf(pf,"%d",1);
            fprintf(pf,"\n");
            fclose(pf);
            
            printf("Se Escribio correctamente en el archivo\n");
            return 0;
} // fin del main

