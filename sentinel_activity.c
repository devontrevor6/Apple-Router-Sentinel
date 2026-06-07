#include <stdio.h>
#include <sys/stat.h>
#include <time.h>
void check_activity(const char *path, const char *label) {
    struct stat attr;
    if (stat(path, &attr) == 0) {
        printf("[!] %s ACTIVITY:\n", label);
        printf("    > Last Pulse: %s", ctime(&attr.st_mtime));
    }
}
int main() {
    printf("[!] SOVEREIGN SIEGE: Shadow Reconstruction (Kernel-Level)\n");
    check_activity("/sdcard/Android", "USER INTERFACE");
    check_activity("/data/data/com.termux/files/home", "TERMINAL ACCESS");
    check_activity("/sdcard/Download", "DATA INGRESS");
    printf("\n[!] If the times above are after 7:00, the device was active.\n");
    return 0;
}
