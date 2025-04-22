

from concurrent.futures import ThreadPoolExecutor
import time 


numbers = [1,2,3,4,5]

def print_number(number):
    time.sleep(1)
    return f"Number : {number}"
    

t = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results= executor.map(print_number, numbers)


for result in results:
    print(result)

finished_time = time.time() - t
print(finished_time)