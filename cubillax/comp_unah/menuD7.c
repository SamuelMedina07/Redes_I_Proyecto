#include<stdio.h>
#include<stdlib.h>
int main() 
          {
             int op=0;
             system("sudo clear");
             printf(" ****** MENU DE OPCIONES ARDUINO ****\n");
             printf("\n\n");
             printf(" 1-  ## Encender GPIO D7 \n");
             printf(" 2-  ## Apagar GPIO D7 \n");
             printf("\n\n");
             printf(" Digite Opcion del menu [1-2] : ");
             scanf("%d",&op);
             if (op==1) 
                       {
                        system("sudo curl -s http://192.168.88.100/on");
                        return 1;
                       }
             if (op==2)
                       {
                        system("sudo curl -s http://192.168.88.100/off");                       
                        return 1;
                       }

             return 0;
} // fin del main

