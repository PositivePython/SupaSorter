import random, time, copy
import matplotlib.pyplot as plt

list_of_sorts = ["Python Built In Method", "Selection Sort", "Bubble Sort", "Insertion Sort", "Heap Sort",
                 "Shell Sort", "Gnome Sort", "Bingo Sort"]
single_sort_results = {}
time_taken_to_sort = 0

# Generates the inital list of unsorted numbers, possible improvements
    # Consider making it so no number is repeated
    # Run loops for increasing lengths of sorts, store results in Pandas and output graphs
    # Research more effecient lists
    # make a procedure of the claculation and print of the time taken
    # Find new sorts to put in
    # In the reporting put into the output details of hardware, OS etc.....
    # Export the results in to JSON or XLS
    # Run the sorts through a list
    # Improve the timing mechanism so it is slicker timeit?

def generate_pre_sort_list(base_data):
    global pre_sort_numbers
    start_time = time.time()
    
    pre_sort_numbers = [random.randint(1, base_data) for _ in range(base_data)]
    
    time_taken_to_create = time.time() - start_time
    print(f"It took {time_taken_to_create:.2f} seconds to create the source data.")


def python_sort(pre_sort_numbers):
    global python_sort_result
    python_sort_result = copy.copy(pre_sort_numbers)
    start_time = time.time()
    
    python_sort_result.sort()
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Python's in built sort method.")
    
    add_to_single_sort_barchart("Python Sort", time_taken_to_sort)

def selection_sort(pre_sort_numbers):
    global selection_sort_result
    selection_sort_result = copy.copy(pre_sort_numbers)
    start_time = time.time()
    
    for i in range(len(selection_sort_result)):
        min_idx = i
        for j in range(i+1, len(selection_sort_result)):
            if selection_sort_result[min_idx] > selection_sort_result[j]:
                min_idx = j
        selection_sort_result[i], selection_sort_result[min_idx] = selection_sort_result[min_idx], selection_sort_result[i]	    # Swap the found minimum element with the first element 
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Selection Sort.")
    
    add_to_single_sort_barchart("Selection Sort", time_taken_to_sort)

def bubble_sort(pre_sort_numbers):
    global bubble_sort_result
    bubble_sort_result = copy.copy(pre_sort_numbers)
    
    n = len(bubble_sort_result)
    start_time = time.time()
    for i in range(n): 
        for j in range(0, n-i-1):
            if bubble_sort_result[j] > bubble_sort_result[j+1]:
                bubble_sort_result[j], bubble_sort_result[j+1] = bubble_sort_result[j+1], bubble_sort_result[j]
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Bubble Sort.")
    
    add_to_single_sort_barchart("Bubble Sort", time_taken_to_sort)

def insertion_sort(pre_sort_numbers):
    global insertion_sort_result
    insertion_sort_result = copy.copy(pre_sort_numbers)
    start_time = time.time()
    
    for i in range(1, len(insertion_sort_result)):
        key = insertion_sort_result[i]
        j = i-1
        while j >= 0 and key < insertion_sort_result[j] :
                insertion_sort_result[j + 1] = insertion_sort_result[j]
                j -= 1
        insertion_sort_result[j + 1] = key
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Insertion Sort.")
    
    add_to_single_sort_barchart("Insertion Sort", time_taken_to_sort)

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
 
def heap_sort(pre_sort_numbers):
    global heap_sort_result
    heap_sort_result = copy.copy(pre_sort_numbers)
    start_time = time.time()
    
    N = len(heap_sort_result)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(heap_sort_result, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        heap_sort_result[i], heap_sort_result[0] = heap_sort_result[0], heap_sort_result[i]  # swap
        heapify(heap_sort_result, i, 0)

    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Heap Sort.")
    
    add_to_single_sort_barchart("Heap Sort", time_taken_to_sort)

def shell_sort(pre_sort_numbers, n):
    global shell_sort_result
    shell_sort_result = copy.copy(pre_sort_numbers)
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
                if shell_sort_result[i+gap]>shell_sort_result[i]:
  
                    break
                else:
                    shell_sort_result[i+gap],shell_sort_result[i]=shell_sort_result[i],shell_sort_result[i+gap]
  
                i=i-gap # To check left side also
                            # If the element present is greater than current element 
            j+=1
        gap=gap//2
    
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Shell Sort.")
    
    add_to_single_sort_barchart("Shell Sort", time_taken_to_sort)

def gnome_sort(pre_sort_numbers):
    global gnome_sort_result
    gnome_sort_result = copy.copy(pre_sort_numbers)
    start_time = time.time()
    n=len(gnome_sort_result)
    index = 0

    while index < n:
        if index == 0:
            index = index + 1
        if gnome_sort_result[index] >= gnome_sort_result[index - 1]:
            index = index + 1
        else:
            gnome_sort_result[index], gnome_sort_result[index-1] = gnome_sort_result[index-1], gnome_sort_result[index]
            index = index - 1
        
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Gnome Sort.")
    
    add_to_single_sort_barchart("Gnome Sort", time_taken_to_sort)
    
def cocktail_sort(pre_sort_numbers):
    global cocktail_sort_result
    cocktail_sort_result = copy.copy(pre_sort_numbers)
    start_time = time.time()
    n = len(cocktail_sort_result)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
 
        # reset the swapped flag on entering the loop, because it might be true from a previous iteration.
        swapped = False
        # loop from left to right same as the bubble sort
        for i in range(start, end):
            if (cocktail_sort_result[i] > cocktail_sort_result[i + 1]):
                cocktail_sort_result[i], cocktail_sort_result[i + 1] = cocktail_sort_result[i + 1], cocktail_sort_result[i]
                swapped = True
 
        # if nothing moved, then array is sorted.
        if (swapped == False):
            break
 
        # otherwise, reset the swapped flag so that it can be used in the next stage
        swapped = False
 
        # move the end point back by one, because item at the end is in its rightful spot
        end = end-1
 
        # from right to left, doing the same comparison as in the previous stage
        for i in range(end-1, start-1, -1):
            if (cocktail_sort_result[i] > cocktail_sort_result[i + 1]):
                cocktail_sort_result[i], cocktail_sort_result[i + 1] = cocktail_sort_result[i + 1], cocktail_sort_result[i]
                swapped = True
 
        # increase the starting point, because the last stage would have moved the next smallest number to its rightful spot.
        start = start + 1
        
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Cocktail Sort.")
    
    add_to_single_sort_barchart("Cocktail Sort", time_taken_to_sort)

def bingo_sort(pre_sort_numbers, size):
    global bingo_sort_result
    bingo_sort_result = copy.copy(pre_sort_numbers)
    start_time = time.time()
  
    # Finding the smallest element From the Array
    bingo = min(pre_sort_numbers)
     
    # Finding the largest element from the Array
    largest = max(bingo_sort_result)
    next_bingo = largest
    next_pos = 0
    while bingo < next_bingo:
       
        # Will keep the track of the element position to shifted to their correct position
        start_pos = next_pos
        for i in range(start_pos, size):
            if bingo_sort_result[i] == bingo:
                bingo_sort_result[i], bingo_sort_result[next_pos] = bingo_sort_result[next_pos], bingo_sort_result[i]
                next_pos += 1
                 
            #  Here we are finding the next Bingo Element for the next pass
            elif bingo_sort_result[i] < next_bingo:
                next_bingo = bingo_sort_result[i]
        bingo = next_bingo
        next_bingo = largest

    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Bingo Sort.")
    
    add_to_single_sort_barchart("Bingo Sort", time_taken_to_sort)
    
# 2 Functions to deliver Comb Sort
  
# To find next gap from current
def get_next_gap(gap):
  
    # Shrink gap by Shrink factor
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
  
# Function to sort arr[] using Comb Sort
def comb_sort(pre_sort_numbers):
    global comb_sort_result
    comb_sort_result = copy.copy(pre_sort_numbers)
    start_time = time.time()
    n = len(comb_sort_result)
  
    # Initialize gap
    gap = n
  
    # Initialize swapped as true to make sure that loop runs
    swapped = True
  
    # Keep running while gap is more than 1 and last iteration caused a swap
    while gap !=1 or swapped == 1:

        # Find next gap
        gap = get_next_gap(gap)
  
        # Initialize swapped as false so that we can check if swap happened or not
        swapped = False
  
        # Compare all elements with current gap
        for i in range(0, n-gap):
            if comb_sort_result[i] > comb_sort_result[i + gap]:
                comb_sort_result[i], comb_sort_result[i + gap]=comb_sort_result[i + gap], comb_sort_result[i]
                swapped = True
  
    time_taken_to_sort = time.time() - start_time
    print(f"It took {time_taken_to_sort:.2f} seconds to use Comb Sort.")
    
    add_to_single_sort_barchart("Comb Sort", time_taken_to_sort)

# Checks to make sure all the sorted lists match the Python sort method list, as you add sorts, add the result list to list_of_sorted_lists 
def check_sorted_lists():
    list_of_sorted_lists = [selection_sort_result, bubble_sort_result, heap_sort_result, insertion_sort_result,
                            shell_sort_result, gnome_sort_result, cocktail_sort_result, bingo_sort_result,
                            comb_sort_result]
    for sorted_list in list_of_sorted_lists:
        if python_sort_result != sorted_list:
            print(f"The sorted lists are not identical, {sorted_list} broke the pattern.")
    print("All the sorted lists are the identical.")

def add_to_single_sort_barchart(sort_type, time_taken):
    single_sort_results[sort_type] = time_taken

# Main Program
print("Welcome To Sean's Supa Sorter Analyser!")
print()
test_type = int(input("You have two options. Press 1 if you'd like to run each test once, using a list length of you choice, or 2 if you'd like to run a full cycle sort test : "))

if test_type == 1:
    print()
    sort_list_length = int(input("How many items would you like to run through Supa Sorter? "))
    
    # generate_pre_sort_list(sort_list_length)
    generate_pre_sort_list(sort_list_length)

    # provides the benchmark sort using .sort method.
    python_sort(pre_sort_numbers)

    # These are the various sorts I have built so far
    insertion_sort(pre_sort_numbers)
    selection_sort(pre_sort_numbers)
    bubble_sort(pre_sort_numbers)
    heap_sort(pre_sort_numbers)
    shell_sort(pre_sort_numbers, len(pre_sort_numbers))
    gnome_sort(pre_sort_numbers)
    cocktail_sort(pre_sort_numbers)
    bingo_sort(pre_sort_numbers, len(pre_sort_numbers))
    comb_sort(pre_sort_numbers)

    # Checks that all sorts match the Python sort method generated
    check_sorted_lists()
    
    #Outputs a bar chart of the results    
    x, y = zip(*single_sort_results.items())
    plt.figure(figsize=(15, 4))
    plt.bar(x, y)
    plt.xlabel("Sort Engines")
    plt.ylabel("Time Taken (seconds")
    plt.title("Different Sort Engines in Python Sorting %i Integers" %sort_list_length)
    plt.show()
    
elif test_type == 2:
    test_cycles = [100, 500, 1000, 2500, 5000, 7500, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    
    for test in test_cycles:
        print(f"Here are the results for a sample of {test} numbers.")
        
        # generate_pre_sort_list(test)
        generate_pre_sort_list(test)
        
        # provides the benchmark sort using .sort method.
        python_sort(pre_sort_numbers) 

        # These are the various sorts I have built so far
        insertion_sort(pre_sort_numbers)
        selection_sort(pre_sort_numbers)
        bubble_sort(pre_sort_numbers)
        heap_sort(pre_sort_numbers)
        shell_sort(pre_sort_numbers, len(pre_sort_numbers))
        gnome_sort(pre_sort_numbers)
        cocktail_sort(pre_sort_numbers)
        bingo_sort(pre_sort_numbers, len(pre_sort_numbers))
        comb_sort(pre_sort_numbers)
        
        print()



