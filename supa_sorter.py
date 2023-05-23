import random, time, copy

list_of_sorts = ["Python Built In Method", ]

# Generates the inital list of unsorted numbers, possible improvements
    # Consider making it so no number is repeated
    # Run loops for increasing lengths of sorts, store results in Pandas and output graphs
    # Research more effecient lists
    # make a procedure of the claculation and print of the time taken
    # Find new sorts to put in
    # In the reporting put into the output details of hardware, OS etc.....
    # Export the results in to JSON or XLS

def generate_pre_sort_list(number_of_items_to_sort):
    global pre_sort_numbers
    start_time = time.time()
    
    pre_sort_numbers = [random.randint(1, sort_list_length) for _ in range(sort_list_length)]
    
    time_taken_to_create = time.time() - start_time
    print(f"It took {time_taken_to_create:.2f} seconds to create the source data.")


def python_sort(pre_sort_numbers):
    global python_sort_list
    python_sort_list = copy.copy(pre_sort_numbers)
    start_time = time.time()
    
    python_sort_list.sort()
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Python's in built sort method.")

def selection_sort_v1(pre_sort_numbers):
    global selection_sort_v1_numbers
    selection_sort_v1_numbers = copy.copy(pre_sort_numbers)
    start_time = time.time()
    
    for i in range(len(selection_sort_v1_numbers)):
        min_idx = i
        for j in range(i+1, len(selection_sort_v1_numbers)):
            if selection_sort_v1_numbers[min_idx] > selection_sort_v1_numbers[j]:
                min_idx = j
        selection_sort_v1_numbers[i], selection_sort_v1_numbers[min_idx] = selection_sort_v1_numbers[min_idx], selection_sort_v1_numbers[i]	    # Swap the found minimum element with the first element 
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Selection Sort v1.")

def bubble_sort_v1(pre_sort_numbers):
    global bubble_sort_v1_numbers
    bubble_sort_v1_numbers = copy.copy(pre_sort_numbers)
    
    n = len(bubble_sort_v1_numbers)
    start_time = time.time()
    for i in range(n): 
        for j in range(0, n-i-1):
            if bubble_sort_v1_numbers[j] > bubble_sort_v1_numbers[j+1]:
                bubble_sort_v1_numbers[j], bubble_sort_v1_numbers[j+1] = bubble_sort_v1_numbers[j+1], bubble_sort_v1_numbers[j]
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Bubble Sort v1.")

def insertion_sort_v1(pre_sort_numbers):
    global insertion_sort_v1_numbers
    insertion_sort_v1_numbers = copy.copy(pre_sort_numbers)
    start_time = time.time()
    
    for i in range(1, len(insertion_sort_v1_numbers)):
        key = insertion_sort_v1_numbers[i]
        j = i-1
        while j >= 0 and key < insertion_sort_v1_numbers[j] :
                insertion_sort_v1_numbers[j + 1] = insertion_sort_v1_numbers[j]
                j -= 1
        insertion_sort_v1_numbers[j + 1] = key
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Insertion Sort v1.")

def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, N, largest) 
 
def heap_sort_v1(pre_sort_numbers):
    global heap_sort_v1_numbers
    heap_sort_v1_numbers = copy.copy(pre_sort_numbers)
    start_time = time.time()
    
    N = len(heap_sort_v1_numbers)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(heap_sort_v1_numbers, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        heap_sort_v1_numbers[i], heap_sort_v1_numbers[0] = heap_sort_v1_numbers[0], heap_sort_v1_numbers[i]  # swap
        heapify(heap_sort_v1_numbers, i, 0)

    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Heap Sort v1.")

def shell_sort_v1(pre_sort_numbers, n):
    global shell_sort_v1_numbers
    shell_sort_v1_numbers = copy.copy(pre_sort_numbers)
    start_time = time.time()

    gap=n//2
    while gap>0:
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            i=j-gap # This will keep help in maintain gap value
              
            while i>=0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if shell_sort_v1_numbers[i+gap]>shell_sort_v1_numbers[i]:
  
                    break
                else:
                    shell_sort_v1_numbers[i+gap],shell_sort_v1_numbers[i]=shell_sort_v1_numbers[i],shell_sort_v1_numbers[i+gap]
  
                i=i-gap # To check left side also
                            # If the element present is greater than current element 
            j+=1
        gap=gap//2

def gnome_sort(pre_sort_numbers):
    global gnome_sort_numbers
    index = 0
    gnome_sort_numbers = copy.copy(pre_sort_numbers)
    n=len(gnome_sort_numbers)
    start_time = time.time()
    
    while index < n:
        if index == 0:
            index = index + 1
        if gnome_sort_numbers[index] >= gnome_sort_numbers[index - 1]:
            index = index + 1
        else:
            gnome_sort_numbers[index], gnome_sort_numbers[index-1] = gnome_sort_numbers[index-1], gnome_sort_numbers[index]
            index = index - 1
        
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Gnome Sort.")

# Checks to make sure all the sorted lists match the Python sort method list, as you add sorts, add the result list to list_of_sorted_lists 
def check_sorted_lists():
    list_of_sorted_lists = [python_sort_list, selection_sort_v1_numbers, bubble_sort_v1_numbers,
                          insertion_sort_v1_numbers, shell_sort_v1_numbers, gnome_sort_numbers]
    for sorted_list in list_of_sorted_lists:
        if python_sort_list != sorted_list:
            print(f"The sorted lists are not identical, {sorted_list} broke the pattern.")
    print("All the sorted lists are the identical.")            

# Main Program
print("Welcome To Sean's Super Sorter Analyser!")
sort_list_length = int(input("How many items would you like to run through Super Sorter? "))
# generate_pre_sort_list(sort_list_length)
generate_pre_sort_list(sort_list_length)

# provides the benchmark sort using .sort method.
python_sort(pre_sort_numbers) 

# These are the various sorts I have built so far
insertion_sort_v1(pre_sort_numbers)
selection_sort_v1(pre_sort_numbers)
bubble_sort_v1(pre_sort_numbers)
heap_sort_v1(pre_sort_numbers)
shell_sort_v1(pre_sort_numbers, len(pre_sort_numbers))
gnome_sort(pre_sort_numbers)

# Checks that all sorts match the Python sort method generated
check_sorted_lists() 