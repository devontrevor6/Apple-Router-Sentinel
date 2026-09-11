#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define ITERATIONS 5000

static inline uint64_t read_counter(void) {
    uint64_t val;
    __asm__ __volatile__("mrs %0, cntvct_el0" : "=r" (val));
    return val;
}

int main() {
    uint64_t *deltas = malloc(ITERATIONS * sizeof(uint64_t));
    if (deltas == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    FILE *artifact_file = fopen("artifacts/timer_matrix_data.log", "w");
    if (artifact_file == NULL) {
        printf("Failed to open artifacts log file.\n");
        free(deltas);
        return 1;
    }

    fprintf(artifact_file, "Iteration,Delta_Ticks\n");
    printf("=== RUNNING TIMER MATRIX DATA COLLECTION (%d ITERATIONS) ===\n", ITERATIONS);

    // Capture consecutive back-to-back register reads
    for (int i = 0; i < ITERATIONS; i++) {
        uint64_t start = read_counter();
        uint64_t end = read_counter();
        deltas[i] = end - start;
        fprintf(artifact_file, "%d,%lu\n", i, deltas[i]);
    }

    fclose(artifact_file);

    // Calculate distributions
    uint64_t zero_count = 0;
    uint64_t one_count = 0;
    uint64_t greater_count = 0;
    uint64_t total_ticks = 0;

    for (int i = 0; i < ITERATIONS; i++) {
        total_ticks += deltas[i];
        if (deltas[i] == 0) zero_count++;
        else if (deltas[i] == 1) one_count++;
        else greater_count++;
    }

    printf("\n=== DATA COLLECTION COMPLETE ===");
    printf("\nLog exported to: artifacts/timer_matrix_data.log\n");
    printf("\n--- Statistical Distribution ---\n");
    printf("0 Ticks (Sub-timer resolution) : %lu occurrences (%.2f%%)\n", zero_count, (double)zero_count / ITERATIONS * 100);
    printf("1 Tick  (Immediate boundary)   : %lu occurrences (%.2f%%)\n", one_count, (double)one_count / ITERATIONS * 100);
    printf(">1 Ticks (OS Interruption/Jitter): %lu occurrences (%.2f%%)\n", greater_count, (double)greater_count / ITERATIONS * 100);
    printf("Total accumulated counter ticks: %lu\n", total_ticks);
    printf("--------------------------------\n");

    free(deltas);
    return 0;
}
