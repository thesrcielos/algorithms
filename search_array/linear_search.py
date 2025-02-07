from typing import List

def linear_search(list: List[int], target: int) -> int:
    for i,elem in enumerate(list):
        if elem == target:
            return i
        
    return -1

def main():
    listExample: List[int] = [10, 2, 5, 613, 65, 345, 73, 23, 67, 0]
    print(linear_search(listExample, 67))
main()