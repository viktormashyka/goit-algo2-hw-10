import random
import time
import numpy as np
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

def run_tests():
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = {"size": [], "randomized": [], "deterministic": []}
    
    for size in sizes:
        arr = [random.randint(0, 10**6) for _ in range(size)]
        randomized_times = [measure_time(randomized_quick_sort, arr[:]) for _ in range(5)]
        deterministic_times = [measure_time(deterministic_quick_sort, arr[:]) for _ in range(5)]
        
        avg_randomized = np.mean(randomized_times)
        avg_deterministic = np.mean(deterministic_times)
        
        results["size"].append(size)
        results["randomized"].append(avg_randomized)
        results["deterministic"].append(avg_deterministic)
        
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {avg_randomized:.4f} секунд")
        print(f"   Детермінований QuickSort: {avg_deterministic:.4f} секунд")
    
    plt.figure()
    plt.plot(results["size"], results["randomized"], label="Рандомізований QuickSort")
    plt.plot(results["size"], results["deterministic"], label="Детермінований QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.show()

run_tests()
