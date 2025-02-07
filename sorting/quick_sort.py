from typing import List

def sort(list: List[int]) -> List[int]:
    if len(list) < 2:
        return list
    pivot: int = list[len(list) // 2]
    smaller: List[int] = []
    greater: List[int] = []
    print(list)
    for i in range(0, len(list) // 2):
        if pivot >= list[i]:
            smaller.append(list[i])
        else:
            greater.append(list[i])
        
    for i in range(len(list) // 2 + 1, len(list)):
        if pivot >= list[i]:
            smaller.append(list[i])
        else:
            greater.append(list[i])
    
    return sort(smaller) + [pivot] + sort(greater)

def main():
    listExample : List[int] = [10,2,5,613,65,345,73,23,67,0]
    listExample = sort(listExample)
    print(listExample)

main()