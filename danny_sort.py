# Original Idea that started it all:
def danny_bub(list):
    length = len(list) - 1
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(counter, length - 1, 1):
            if list[i] > list[i + 1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        if(not sorted):
            for j in range(length, counter, -1):
                if list[j] < list[j - 1]:
                    list[j], list[j-1] = list[j-1], list[j]
        counter += 1
        length -= 1
    print list
danny_bub(my_list)

# Refined and maximized "Ascending" and "Descending" bubble sort for quick implimentation
def danny_bub2(list): # Only 121 "Steps" to solve this one
    for i in range((len(list))//2):
        for j in range(i, (len(list) - 1) - i): 
            if list[j] > list[j+1]: 
                list[j], list[j+1] = list[j+1], list[j]      
        for k in range((len(list) - 2) - i, i, -1): 
            if list[k] < list[k - 1]: 
                list[k], list[k-1] = list[k-1], list[k]
    print list

# My version of a select sort which "may" be better for larger lists as it emphasizes removing index length as quickly as possible 
def danny_select(list):
    maxPos = 0
    beg = 0
    end = len(list)
    for num in range((len(list) - 1)//2):
        for loc in range(beg + 1, end - num):
            if list[loc] > list[maxPos]:
                if loc == end - num - 1:
                    loc -= 1
                    end -= 1
                else:
                    maxPos = loc
        list[loc], list[maxPos]=list[maxPos], list[loc]
        minPos = loc - 1
        for loc2 in range(end - 2, num - 1, -1):
            if list[loc2] < list[minPos]:
                if loc2 == beg:
                    beg += 1
                    loc2 += 1
                else:
                    minPos = loc2
        list[loc2], list[minPos]=list[minPos], list[loc2]
        maxPos = loc2 + 1
        if maxPos == minPos:
            return list
    return list

danny_select(my_list)

# My shorter basic straightforward select which is great for quick implementation
def danny_shortsort_select(list):
    maxPos = 0
    for num in range((len(list) - 1)//2):
        for loc in range(num + 1, len(list) - num):
            if list[loc] > list[maxPos]:
                maxPos = loc
        list[loc], list[maxPos]=list[maxPos], list[loc]
        minPos = loc - 1
        for loc2 in range(loc - 2, num - 1, -1):
            if list[loc2] < list[minPos]:
                minPos = loc2
        list[loc2], list[minPos]=list[minPos], list[loc2]
        maxPos = loc2 + 1
    print list

danny_shortsort_select(my_list)
   



# Basic Sorts for comparison         
def bubble_sort(list):
    length = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    print list
bubble_sort(my_list)

def select_sort(list):
    for num in range(len(list) - 1, 0, -1):
        maxPos = 0
        for loc in range(1, num + 1):
            if list[loc] > list[maxPos]:
                maxPos = loc
        list[num], list[maxPos]=list[maxPos], list[num]
    print list

select_sort(my_list)



# TEST LISTS
my_list = [98,4,6,8,1,45,87,77,3] #150 to 114 Bubble to Danny
my_list2 = [98,87,77,1,8,45,6,4,3] #221 to 150 with this one! 
test_list = [35, 26, -8, -24, 1, -10, 29, -20, -2, 8, 41, 0, -22, 26, 12, -25, 41, 49, 31, 41, -19, 23, 40, 19, -3, -40, -7, 11, 42, 47, -2, 37, -24, 31, 5, -49, 22, -10, 33, 17, -50, -1, 37, -26, -18, 37, -31, 7, -26, 47, 31, -5, -42, -18, 1, 44, -39, 5, 21, 5, 32, 4, 47, 10, 9, -6, 10, -12, 8, -21, -31, -32, 11, 16, -2, -41, 26, 38, 43, 35, 40, 43, 4, -11, 21, -23, 31, 35, 40, 9, 45, 8, -5, 16, 50, 42, 30, -42, 11, -1]

test_list2 = [77, 64, 13, -11, 27, 11, 68, -5, 21, 38, 87, 26, -8, 64, 43, -13, 87, 98, 72, 86, -4, 60, 85, 53, 21, -35, 15, 42, 87, 95, 22, 80, -11, 71, 32, -48, 58, 10, 74, 50, -50, 24, 81, -14, -1, 81, -22, 35, -14, 96, 71, 17, -38, -2, 26, 90, -34, 33, 56, 32, 72, 31, 95, 41, 38, 17, 40, 8, 36, -7, -22, -22, 42, 49, 21, -37, 64, 82, 89, 77, 85, 89, 31, 9, 56, -9, 72, 78, 85, 39, 93, 37, 18, 49, 100, 88, 69, -38, 42, 23]

test_list3 = [85, 76, 42, 26, 51, 40, 79, 30, 48, 58, 91, 50, 28, 76, 62, 25, 91, 99, 81, 91, 31, 73, 90, 69, 47, 10, 43, 61, 92, 97, 48, 87, 26, 81, 55, 1, 72, 40, 83, 67, 0, 49, 87, 24, 32, 87, 19, 57, 24, 97, 81, 45, 8, 32, 51, 94, 11, 55, 71, 55, 82, 54, 97, 60, 59, 44, 60, 38, 58, 29, 19, 18, 61, 66, 48, 9, 76, 88, 93, 85, 90, 93, 54, 39, 71, 27, 81, 85, 90, 59, 95, 58, 45, 66, 100, 92, 80, 8, 61, 49]



