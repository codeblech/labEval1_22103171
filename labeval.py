slist = []
def add_item(item):
    slist.append(item)
    print(f"{item} added to the list \n")
    
def remove_item(item):
    for i in slist:
        if i == item:
            slist.remove(item)
            print(f"{item} removed from the list \n")
            
def search_item(item):
    return item in slist

def display_list():
    for i, item in enumerate(slist):
        print(f"{i+1}: {item}", end="\n")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def bs_reverse(item):
    sorted_list = quick_sort(slist)
    index =  binary_search(sorted_list, item)
    if index != -1:
        print(f"search result revered: {sorted_list[index][::-1]}")
    else:
        print("item not found in binary search")
    
x = True
while (x):
    print("What operation would you perform: ")
    print("1. add  2. remove  3. search  4. display  5. binary search reverse")
    opt = int(input("enter option: "))
    
    if (opt == 1):
        item = input("item to add: ")
        add_item(item)
    elif (opt == 2):
        item = input("item to remove: ")
        remove_item(item)
    elif (opt == 3):
        item = input("item to search: ")
        if search_item(item):
            print("item found")
        else:
            print("not found")
    elif (opt == 4):
        display_list()
    elif (opt == 5):
        item = input("item to search & reverse: ")
        bs_reverse(item)
    cont = input("Continue? [y/n]")
    if cont == "n":
        x = False