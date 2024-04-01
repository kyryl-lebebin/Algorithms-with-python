'''
    Specification: 
        To use it, write suc code

        @quadratic(n=int(input()))
        def func(arr):
            Pass

        func()
'''



import random
import time
import matplotlib.pyplot as plt


def quadratic(n):
    """
    Decorator factory that takes an argument n and returns a decorator that times the execution of a function,
    performs the function on arrays of sizes 1 to n filled with random numbers, plots the execution time against
    array size, and compares this to a quadratic curve.
    """
    def decorator(func):
        def wrapper():
            array_sizes = []
            time_taken = []
            squared_counts = []

            for size in range(1, n + 1):
                random_array = [random.randint(0, 1000) for _ in range(size)]
                start_time = time.perf_counter()
                func(random_array)
                end_time = time.perf_counter()

                array_sizes.append(size)
                time_taken.append(end_time - start_time)
                squared_counts.append(size ** 2)

            # Plotting the results using matplotlib
            plt.figure(figsize=(10, 5))
            plt.plot(array_sizes, time_taken, label=f'{func.__name__} Time', marker='o')
            plt.plot(array_sizes, [y * 1e-8 for y in squared_counts], label='n^2 (scaled)', linestyle='--')
            plt.xlabel('Array Size (n)')
            plt.ylabel('Time Taken (seconds)')
            plt.title(f'Time Complexity of {func.__name__} vs. n^2 (scaled)')
            plt.legend()
            plt.grid(True)
            plt.show()
            
            return func()
        return wrapper
    return decorator

# Adjusted example usage with a predefined range for n
'''@quadratic(n=int(input()))  # Using the decorator with a predetermined n
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


insertion_sort()  '''


