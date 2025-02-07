from typing import List

def ternary_search(list: List[int], target: int):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle1 = left + (right - left) // 3
        middle2 = right - (right - left) // 3

        if list[middle1] == target:
            return middle1
        if list[middle2] == target:
            return middle2

        if target < list[middle1]:
            right = middle1 - 1
        elif target > list[middle2]:
            left = middle2 + 1
        else:
            left = middle1 + 1
            right = middle2 - 1

    return -1  

def main():
    listExample: List[int] = [0, 2, 5, 10, 23, 65, 67, 73, 345, 613]
    print(ternary_search(listExample, 66))
main()
