from AbstractCollection import AbstractCollection
from Array import Array

class MaxHeap(AbstractCollection):
    """An array-based implementation of a heap"""
    
    DEFAULT_CAPACITY = 100
    
    def __init__(self):
        self._heap = Array(MaxHeap.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self)
    
    def add(self, item):
        """Adds 'item' to the MinHeap, finding its correct location"""
        self._heap[len(self)] = item
        
        # cur_index will track the index the new item is currently in
        cur_index = len(self)
        while cur_index > 0:
            # Find the current parent of the new item
            parent_index = (cur_index - 1) // 2
            parent_item = self._heap[parent_index]
            if parent_item >= item:
                # Parent is greater than or equal to new item, so stop looping
                # New item is in correct location
                break
            
            # Parent is less than new item. Swap places
            self._heap[cur_index] = parent_item
            self._heap[parent_index] = item
            cur_index = parent_index
        
        self._numitems += 1
        
    
    def peek(self):
        if self._numitems == 0:
            raise ValueError("Heap is empty!")
        return self._heap[0]
    
    def pop(self):
        if self._numitems == 0:
            raise ValueError("Heap is empty!")
        
        top_item = self._heap[0]
        bottom_item = self._heap[len(self) - 1]
        
        # Reheapify: Start by placing bottom item in the root
        self._heap[0] = bottom_item
        
        # Get the index of the new rightmost leaf in the final level
        last_index = len(self) - 2
        
        cur_index = 0
        # In a loop, move the original final leaf (now at the root) down to its correct location
        while True:
            left_child_index = 2 * cur_index + 1
            right_child_index = 2 * cur_index + 2
            
            if left_child_index > last_index: 
                # No left child, so we can break
                break
            
            if right_child_index > last_index:
                # We only have a left child, so it is the smallest by default
                max_child_index = left_child_index
            else:
                # We have two children, see which is bigger
                left_child = self._heap[left_child_index]
                right_child = self._heap[right_child_index]

                if left_child > right_child:
                    max_child_index = left_child_index
                else:
                    max_child_index = right_child_index
            
            max_child = self._heap[max_child_index]

            if bottom_item > max_child:
                # Item being moved down is larger than its biggest child
                break
            else:
                # Item being moved is larger than its smallest child, swap and continue
                self._heap[cur_index] = max_child
                self._heap[max_child_index] = bottom_item
                cur_index = max_child_index
        
        self._numitems -= 1
        return top_item
        
        
    def print_heap(self):
        # Prints the internal data, for testing purposes only
        for i in range(len(self)):
            print(self._heap[i], end = " ")