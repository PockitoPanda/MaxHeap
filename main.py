from MaxHeap import MaxHeap
import random

def main():
    heap = MaxHeap()
    for i in range(100):
        rand_num = random.randint(1, 100)
        heap.add(rand_num)
    k = int(input("Enter a value for K (between 1 and 100) to find the K largest values in a list: "))
    
    for i in range(k):
        print(heap.pop(), end = " ")

main()
