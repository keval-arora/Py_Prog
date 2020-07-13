import random
from time import time
from sort_algos import quick_sort,merge_sort, merge_sorted

def ran_list(size, max_range):   
    random_list = [random.randint(1,max_range) for count in range(size)]
    return random_list

def analyzer(fun_name, lis):
    start_time = time()
    fun_name(lis)
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Performance for {(fun_name.__name__).capitalize()} is {elapsed_time:.5f}")
    

#Input:
size = int(input("Please enter the size of list"))
max_range = int(input("Please enter the maximum range of list"))
run_time = int(input("How many time do you want to analyze?"))
my_list = ran_list(size, max_range)

for num in range(run_time):
    print(f"Run: {num}")
    analyzer(quick_sort, my_list.copy())
    analyzer(merge_sort, my_list.copy())
    print("-"*40)

# select = int(input("""Please select one of the following option
# 1. Quick Sort
# 2. Merge Sort
# """))

# if select == 1:
#     analyzer(quick_sort, my_list.copy())
# else:
#     analyzer(merge_sort, my_list.copy())
