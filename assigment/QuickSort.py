

class QuickSort:
    def __init__(self, arr):
        self.arr = arr
    
    def partition(self, beg, end):
        pivot = self.arr[end]
        i = beg - 1
        for j in range(beg, end):
            if self.arr[j] < pivot:  
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[end] = self.arr[end], self.arr[i + 1]
        return i + 1
    
    def quick_sort(self, beg, end):
        if beg < end:
            pi = self.partition(beg, end)
            self.quick_sort(beg, pi - 1)
            self.quick_sort(pi + 1, end)
    
    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)
        return self.arr


arr = [17,-4,0,2,21,0]
qs = QuickSort(arr)
sorted_arr = qs.sort()
print("Sorted Array:", sorted_arr)