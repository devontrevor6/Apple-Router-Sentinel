#include <stdio.h>
#include <stdint.h>
#include <x86intrin.h>

int main() {
    char *secret = "SIG_REDUNDANT_BRAKE_0xAF32";
    uint64_t t1, t2;
    unsigned int junk;
    
    printf("--- HIGH-RESOLUTION PERFORMANCE CLOCK BASELINE ---\n");
    printf("Target System: Native Hardware Cycle Trace\n\n");

    for (int i = 0; i < 20; i++) {
        _mm_lfence();
        t1 = __rdtscp(&junk);
        _mm_lfence();
        
        volatile char leak = *secret; 
        
        _mm_lfence();
        t2 = __rdtscp(&junk);
        _mm_lfence();
        
        uint64_t delta = t2 - t1;
        printf("Pulse %02d | Latency: %lu cycles\n", i, delta);
    }
    return 0;
}
