import time
import statistics

def standard_operation():
    total = 0
    for i in range(1000):
        total += i
    return total

def run_variance_test(iterations=100):
    durations = []
    print(f"Starting baseline test over {iterations} iterations...")
    
    for _ in range(iterations):
        start_time = time.perf_counter()
        standard_operation()
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        durations.append(elapsed)

    avg_duration = statistics.mean(durations)
    min_duration = min(durations)
    max_duration = max(durations)
    std_dev = statistics.stdev(durations)

    print("\n=== Baseline Results ===")
    print(f"Average Execution Time : {avg_duration:.9f} seconds")
    print(f"Minimum Execution Time : {min_duration:.9f} seconds")
    print(f"Maximum Execution Time : {max_duration:.9f} seconds")
    print(f"Standard Deviation     : {std_dev:.9f} seconds")
    print("=========================")

if __name__ == "__main__":
    run_variance_test()
