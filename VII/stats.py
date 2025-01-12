import random
import time

from bubblesort import bubble_sort
from heapsort import heap_sort
from insertsort import insert_sort
from mergesort import merge_sort
from quicksort import quick_sort

def generate_random_data(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def calculate_stats(times):
    if not times:
        return None
    
    return {
        'min': min(times),
        'max': max(times),
        'avg': sum(times) / len(times)
    }

def test_sorting_performance():
    test_sizes = [
        10, 50, 100, 500, 1000, 
        10000, 50000, 1000000 # (zmienić wartości w przypadku długiego wykonywania się testów)
    ]
    sorting_algorithms = [
        ('Bubble Sort', bubble_sort),
        ('Insertion Sort', insert_sort),
        ('Heap Sort', heap_sort),
        ('Merge Sort', merge_sort),
        ('Quick Sort', quick_sort)
    ]
    
    results = {}
    algorithm_stats = {}
    
    for size in test_sizes:
        print(f"\nRozmiar zbioru: {size}")
        
        data = generate_random_data(size)
        
        for name, sort_func in sorting_algorithms:
            try:
                if name not in algorithm_stats:
                    algorithm_stats[name] = []
                
                test_data = data.copy()
                
                start_time = time.time()
                sort_func(test_data)
                end_time = time.time()
                
                duration_ms = (end_time - start_time) * 1000
                
                if size not in results:
                    results[size] = {}
                results[size][name] = duration_ms
                
                algorithm_stats[name].append(duration_ms)
                
                print(f"{name}: {duration_ms:.3f} ms")
            
            except Exception as e:
                print(f"Błąd w {name}: {e}")
    
    return results, algorithm_stats

def print_performance_summary(results, algorithm_stats):
    print("\n\nPODSUMOWANIE WYDAJNOŚCI:")
    for size, algorithms in results.items():
        print(f"\nRozmiar zbioru: {size}")
        for name, duration in sorted(algorithms.items(), key=lambda x: x[1]):
            print(f"{name}: {duration:.3f} ms")
    
    print("\n\nSTATYSTYKI ALGORYTMÓW:")
    for name, times in algorithm_stats.items():
        stats = calculate_stats(times)
        print(f"\n{name}:")
        print(f"  Minimum: {stats['min']:.3f} ms")
        print(f"  Maksimum: {stats['max']:.3f} ms")
        print(f"  Średnia: {stats['avg']:.3f} ms")


performance_results, algorithm_statistics = test_sorting_performance()
print_performance_summary(performance_results, algorithm_statistics)