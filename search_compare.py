import random
import time

def sequential_search(lst, item):
    start_time = time.time()
    # code for sequential search goes here
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, False

def ordered_sequential_search(lst, item):
    start_time = time.time()
    # code for ordered sequential search goes here
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, False

def binary_search_iterative(lst, item):
    start_time = time.time()
    # code for iterative binary search goes here
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, False

def binary_search_recursive(lst, item):
    start_time = time.time()
    # code for recursive binary search goes here
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, False

def main():
    list_sizes = [500, 1000, 10000]
    search_items = [-1]

    for size in list_sizes:
        sequential_search_times = []
        ordered_sequential_search_times = []
        binary_search_iterative_times = []
        binary_search_recursive_times = []
        for i in range(100):
            # generate a random list of given size
            lst = [random.randint(0, size) for _ in range(size)]
            # sort the list
            lst.sort()
            for item in search_items:
                # measure the time taken for sequential search
                elapsed_time, _ = sequential_search(lst, item)
                sequential_search_times.append(elapsed_time)
                # measure the time taken for ordered sequential search
                elapsed_time, _ = ordered_sequential_search(lst, item)
                ordered_sequential_search_times.append(elapsed_time)
                # measure the time taken for iterative binary search
                elapsed_time, _ = binary_search_iterative(lst, item)
                binary_search_iterative_times.append(elapsed_time)
                # measure the time taken for recursive binary search
                elapsed_time, _ = binary_search_recursive(lst, item)
                binary_search_recursive_times.append(elapsed_time)

        # calculate the average time taken for sequential search
        avg_time = sum(sequential_search_times) / len(sequential_search_times)
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average")

    avg_time = total_time / 100
    print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
