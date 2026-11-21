#include <stdio.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <string.h>

int main() {
    int s = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in a = {0};

    a.sin_family = AF_INET;
    a.sin_port = htons(80);
    inet_pton(AF_INET, "192.168.88.100", &a.sin_addr);

    if (connect(s, (struct sockaddr *)&a, sizeof(a)) < 0) {
        perror("Error de conexion");
        close(s);
        return 1;
    }

    char *m = "GET /off HTTP/1.1\r\nHost: arduino\r\nConnection: close\r\n\r\n";
    send(s, m, strlen(m), 0);

    char r[512];
    int n = read(s, r, sizeof(r) - 1);

    if (n > 0) {
        r[n] = '\0';
        printf("D7 APAGADO correctamente\n");
    } else {
        printf("No se recibio respuesta del Arduino\n");
        close(s);
        return 1;
    }

    close(s);
    return 0;
}
