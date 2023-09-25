import multiprocessing
import time

def function_1():
    """Example function 1"""
    print("Function 1 started")
    time.sleep(1)
    print("Function 1 completed")

def function_2():
    """Example function 2"""
    print("Function 2 started")
    time.sleep(2)
    print("Function 2 completed")

def function_3():
    """Example function 3"""
    print("Function 3 started")
    time.sleep(3)
    print("Function 3 completed")

def function_4():
    """Example function 4"""
    print("Function 4 started")
    time.sleep(1)
    print("Function 4 completed")

def function_5():
    """Example function 5"""
    print("Function 5 started")
    time.sleep(2)
    print("Function 5 completed")

if __name__ == "__main__":
    # Create a list of functions
    functions = [function_1, function_2, function_3, function_4, function_5]

    start_time = time.time()
    # Create a multiprocessing Pool with a maximum of 2 processes
    pool = multiprocessing.Pool(processes=2)
    

    # Apply the functions to the Pool asynchronously
    results = [pool.apply_async(func) for func in functions]

    # Wait for all the functions to complete
    pool.close()
    pool.join()

    # Get the results
    for result in results:
        result.get()

    print("TIME TAKEN =====>" ,time.time()- start_time)