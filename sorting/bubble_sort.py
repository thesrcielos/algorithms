from typing import List

def sort(list: List[int]) -> List[int]:
    for i in range(len(list)):
        swapped : bool = False
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        if not swapped:
            break

    return list

def main():
    listExample : List[int] = [10,2,5,613,65,345,73,23,67,0]
    sort(listExample)
    print(listExample)

main()