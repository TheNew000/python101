import itertools

def list_sum(li):
    for i in li:
        if type(i) != int and type(i) != float:
            print('The list MUST include only Numbers (Integers)')
            return
    print sum(li)

list_sum([4,6,8,1,45,87,98])


def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    print tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print tuple(pool[i] for i in indices[:r])
                break
        else:
            if r > 0:
                print tuple(pool[i] for i in indices[:r])
                r -= 1
            else:
                break


# print permutations([98,4,6,8,1,45,87])


my_list = [98,4,6,8,1,45,87,77,3]

# print(list(itertools.permutations(my_list)))

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

def merge_sort(list):
    holder = len(list)
    return merge_help(list, holder)
    
def merge_help(list, holder):
    if len(list) > 1:
        medium = len(list)//2
        left = list[:medium]
        right = list[medium:]

        merge_help(left, holder)
        merge_help(right, holder)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i = i+1
            else:
                list[k]=right[j]
                j = j+1
            k = k+1

        while i < len(left):
            list[k]=left[i]
            i = i+1
            k = k+1

        while j < len(right):
            list[k]=right[j]
            j=j+1
            k=k+1
    else:
        return list
    if k == holder:
        print list

merge_sort(my_list)


my_list = [3,98,4,6,8,1,45,87,77]

def quick_sort(list):
    quick_help(list, 0, len(list) - 1)
    print list

def quick_help(list, first, last):
    if first < last:
        split = partition(list, first, last)
        quick_help(list, first, split - 1)     
        quick_help(list, split + 1, last)     

def partition(list, first, last):
    pivot = list[first]
    print pivot, 'PivVal'

    leftPt = first+1
    rightPt = last
    done = False

    while not done:
        while leftPt <= rightPt and list[leftPt] <= pivot:
            leftPt = leftPt + 1

        while list[rightPt] >= pivot and rightPt >= leftPt:
            print list[rightPt], rightPt, pivot, 'Right'
            rightPt = rightPt -1

        if rightPt < leftPt:
            done = True
        else:
            list[leftPt], list[rightPt] = list[rightPt], list[leftPt]

    list[first], list[rightPt] = list[rightPt], list[first]

    return rightPt

quick_sort(my_list)
