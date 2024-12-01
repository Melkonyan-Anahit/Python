import random
import time
import os

def create_file(filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        for _ in range(100):
            f.write(' '.join(str(random.randint(1, 100)) for _ in range(20)) + '\n')

def filter_and_write_file(filename):
    with open(filename, 'r') as f:
        filtered_data = [
            [num for num in map(int, line.split()) if num > 40] 
            for line in f
        ]
    
    with open(filename, 'w') as f:
        for line in filtered_data:
            f.write(' '.join(map(str, line)) + '\n')

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.name} took {time.time() - start:.4f} seconds")
        return result
    return wrapper

@measure_time
def main():
    filename = 'randNums.txt' 
    directory as the script
    create_file(filename)
    filter_and_write_file(filename)
    
    with open(filename, 'r') as f:
        for _ in range(5):
            print(next(f).strip())

if name == "main":
    main()
