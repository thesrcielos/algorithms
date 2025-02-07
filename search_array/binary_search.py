from typing import List

def binary_search(list: List[int], target: int) -> int:
    left: int = 0
    right: int = len(list) - 1

    while left <= right:
        middle: int = (right + left) // 2
        
        if list[middle] == target:
            return middle
        
        if list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

def main():
    listExample: List[int] = [0, 2, 5, 10, 23, 65, 67, 73, 345, 613]
    print(binary_search(listExample, 66))
main()