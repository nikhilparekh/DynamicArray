import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n

    def __getItem__(self,index):
        if not 0 <=index<=self.n:
            return IndexError("Index out of bounds")
        return self.A[index]

    def append(self,element):
        # check if we insert in the last index then increase the size of array by double
        if(self.capacity == self.n):
            self._resize(self.capacity*2)

        self.A[self.n] = element
        self.n+=1

    def _resize(self, new_capacity):
        # create a new array with double the capacity the we got from append method
        B = self.make_array(new_capacity)

        #assign all the elements from A to B
        for i in range(self.n):
            B[i] = self.A[i]

        #rename the new array to old array
        self.A = B
        self.capacity = new_capacity
    
    def  make_array(self,new_capacity):
        return (new_capacity*ctypes.py_object)()


arr = DynamicArray()

arr.append(10)
print(arr.__len__())
arr.append(20)
print(arr.__len__())
print(arr.__getItem__(1))