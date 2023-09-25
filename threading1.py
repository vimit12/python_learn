import threading
import time

# Function to be executed in a separate thread
def print_numbers():
    for i in range(1, 6):
        print(i)
        # time.sleep(1)

# Function to be executed in a separate thread
def print_letters():
    for char in 'ABCDE':
        print(char)
        # time.sleep(1)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

print("Threads execution complete")
