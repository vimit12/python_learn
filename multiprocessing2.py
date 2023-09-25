import multiprocessing

def process_data(data):
    """Function to process a chunk of data."""
    # Perform some complex computation or task on the data
    processed_data = []

    for item in data:
        result = item * 2  # Example computation
        processed_data.append(result)

    return processed_data

if __name__ == "__main__":
    # Create a large dataset
    dataset = list(range(1000000))

    # Define the number of processes to use
    num_processes = multiprocessing.cpu_count()
    print("NO OF PROCESSOR ======>",num_processes)
    # Split the dataset into chunks for each process
    chunk_size = len(dataset) // num_processes
    print("CHUNCK SIZE ======>",chunk_size)
    chunks = [dataset[i:i+chunk_size] for i in range(0, len(dataset), chunk_size)]

    # Create a multiprocessing Pool
    pool = multiprocessing.Pool()

    # Apply the process_data function to each chunk in parallel
    results = pool.map(process_data, chunks)

    # Flatten the results into a single list
    flattened_results = [item for sublist in results for item in sublist]

    # Print the first few results
    print(flattened_results[:10])
