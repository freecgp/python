#encoding : utf8
import sys


# sys.setrecursionlimit(1000000)


def bubble_sort(param_list):
    """冒泡排序"""
    if len(param_list) <= 1:
        return param_list
    for i in range(len(param_list)):
        for j in range(len(param_list)-1):
            if param_list[j] > param_list[j+1]:
                param_list[j], param_list[j+1] = param_list[j+1], param_list[j]
    return param_list


def insert_sort(param_list):
    """插入排序"""
    if len(param_list) <= 1:
        return param_list
    for i in range(len(param_list)):
        for j in range(i):
            if param_list[i] < param_list[j]:
                param_list[i], param_list[j] = param_list[j], param_list[i]
    return param_list


def divide_sort(param_list, left, right):
    """划分排序"""
    low = left
    high = right
    if len(param_list) <= 1:
        return param_list
    divide_index = partion(param_list, left, right)
    divide_sort(param_list, low, divide_index-1)
    divide_sort(param_list, divide_index+1, high)
    return param_list


def partion(param_list, low, high):

    key = param_list[low]
    while low < high:
         while low < high and param_list[high] >= key:
             high -= 1
         param_list[low] = param_list[high]
         while low < high and param_list[low] <= key:
             low += 1
         param_list[high] = param_list[low]
         param_list[high] = key
    return low


def quick_sort(lists, left, right):
     if left >= right:
         return lists
     key = lists[left]
     low = left
     high = right
     while left < right:
         while left < right and lists[right] >= key:
             right -= 1
         lists[left] = lists[right]
         while left < right and lists[left] <= key:
             left += 1
         lists[right] = lists[left]
     lists[right] = key
     quick_sort(lists, low, left - 1)
     quick_sort(lists, left + 1, high)
     return lists


if __name__ == '__main__':
    param_list = [8, 3, 4, 6, 9, 1, 5, 7, 2, 9]
    # print(bubble_sort(param_list))
    # print(insert_sort(param_list))
    print(divide_sort(param_list, 0, len(param_list)-1))
