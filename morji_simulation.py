import time
import sys
import numpy as np

def run_poc():
    print("--- Initiating Morji Protocol vs. Standard Computing PoC ---\n")

    # ==========================================
    # SYSTEM A: Standard Human-Readable Approach
    # ==========================================
    system_a_payload = """
    {
      "directive": "optimize_energy_distribution",
      "target_region": "sub_saharan_grid",
      "immutable_laws": ["ubuntu", "no_harm"],
      "parameters": {"drought_level": 0.84, "solar_output": 0.91, "population_density": 0.65}
    }
    """
    
    size_a = sys.getsizeof(system_a_payload)
    
    start_time = time.perf_counter()
    for _ in range(100000):
        "optimize_energy_distribution" in system_a_payload 
    time_a = time.perf_counter() - start_time

    print(f"SYSTEM A (Standard Code):")
    print(f"Payload Size: {size_a} bytes")
    print(f"Processing Latency: {time_a:.4f} seconds\n")

    # ==========================================
    # SYSTEM B: The Morji Language 
    # ==========================================
    morji_payload = np.array([0.84, 0.91, 0.65, 1.0, -1.0], dtype=np.float16)
    
    size_b = sys.getsizeof(morji_payload)
    
    start_time = time.perf_counter()
    for _ in range(100000):
        _ = morji_payload * 2.0 
    time_b = time.perf_counter() - start_time

    print(f"SYSTEM B (Morji Protocol):")
    print(f"Payload Size: {size_b} bytes")
    print(f"Processing Latency: {time_b:.4f} seconds\n")

    # ==========================================
    # RESULTS & EFFICIENCY MULTIPLIER
    # ==========================================
    size_reduction = ((size_a - size_b) / size_a) * 100
    speed_increase = time_a / time_b

    print(f"--- EXPERIMENT RESULTS ---")
    print(f"Data Weight Reduction: {size_reduction:.1f}%")
    print(f"Processing Speed Multiplier: {speed_increase:.1f}x faster")

if __name__ == "__main__":
    run_poc()
