import multiprocessing

# Function to be executed in a separate process
def square_numbers(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

if __name__ == '__main__':
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Create a multiprocessing Pool with the number of desired processes
    # The number of processes will be determined by the available CPU cores
    with multiprocessing.Pool() as pool:
        # Apply the function to the numbers using parallel processing
        results = pool.map(square_numbers, [numbers])

    print(results)
