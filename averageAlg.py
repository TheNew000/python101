# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(list):
    sum = 0
    list = sorted(list)
    div = 0
    for i in range(1, len(list)-1):
        if list[i] == list[0]:
            div += 0
        elif list[i] == list[i +1]:
            div += 0
        else:
            div += 1
            sum += list[i]
    print sum/(div)

def centered_average(list):
    sum = 0
    list = sorted(list)
    div = 0
    for i in range(1, len(list)-1):
        if list[i] != list[i+1]:
            div += 1
            sum += list[i]
    print sum/div

def centered_average(list):
    sorted_list = sorted(numbers)
    low = min(sorted_list)
    high = max(sorted_list)
    sorted_list.remove(low)
    sorted_list.remove(high)

def centered_average(list):
    list = sorted(list)
    list.pop(0)
    list.pop(len(list)-1)
    return sum(list)/len(list)

def centered_average(list):
    return sum(sorted(list[1:-1]))/len(sorted(list[1:-1]))

    
centered_average([1, 1, 5, 5, 10, 8, 7])
