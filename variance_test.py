import time
import statistics

def check_variance():
    print("\033[94m[*] Initializing Thread Latency Variance Test...\033[0m")
    samples = []

    for _ in range(100):
        t0 = time.perf_counter_ns()
        _ = [i**2 for i in range(100)]
        t1 = time.perf_counter_ns()
        samples.append(t1 - t0)
        time.sleep(0.01)
        
    avg_latency = sum(samples) / len(samples)
    v_jerk = statistics.variance(samples) if len(samples) > 1 else 0
    print("-" * 50)
    print(f"Total Samples Collected: {len(samples)}")
    print(f"Average Execution Time : {avg_latency:.2f} ns")
    print(f"Jitter Variance Profile: {v_jerk:.2f}")
    print("-" * 50)

if __name__ == "__main__":
    check_variance()
