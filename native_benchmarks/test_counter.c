#include <stdio.h>
#include <stdint.h>

int main() {
    uint64_t val;
    
    printf("Attempting to read ARMv8 physical counter register...\n");
    
    // Inline assembly to read the virtual count register (CNTVCT_EL0)
    __asm__ __volatile__("mrs %0, cntvct_el0" : "=r" (val));
    
    printf("Success! Current hardware counter value: %lu\n", val);
    return 0;
}
