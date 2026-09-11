#include <stdio.h>
#include <stdint.h>

// Macro to grab the hardware timer cycle count instantly
static inline uint64_t get_hardware_ticks(void) {
    uint64_t ticks;
    __asm__ __volatile__("mrs %0, cntvct_el0" : "=r" (ticks));
    return ticks;
}

int main() {
    volatile int memory_buffer[64] = {0};
    uint64_t start, end;
    uint64_t arithmetic_delta, memory_delta;
    volatile int computation = 10;

    printf("=== INITIALIZING HARDWARE LATENCY PROFILE ===\n\n");

    // 1. Benchmark internal CPU register math
    start = get_hardware_ticks();
    computation = (computation * 5) + 32;
    end = get_hardware_ticks();
    arithmetic_delta = end - start;

    // 2. Benchmark reading a value out of memory
    start = get_hardware_ticks();
    int read_value = memory_buffer[32];
    end = get_hardware_ticks();
    memory_delta = end - start;

    // Output the physical timing differentials
    printf("Register Arithmetic Duration : %lu hardware ticks\n", arithmetic_delta);
    printf("Memory Buffer Read Duration  : %lu hardware ticks\n", memory_delta);
    printf("--------------------------------------------------\n");
    printf("Note: These values are tied to your system timer frequency.\n");

    return 0;
}
