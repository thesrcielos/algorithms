from typing import List

def sort(list: List[int]) -> List[int]:
    for i in range(len(list) - 1):
        min_element: int = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_element]:
                min_element = j
        list[i], list[min_element] = list[min_element], list[i]

def main():
    listExample : List[int] = [10,2,5,613,65,345,73,23,67,0]
    sort(listExample)
    print(listExample)

main()