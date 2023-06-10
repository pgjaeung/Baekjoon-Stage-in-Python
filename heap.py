class Heap:
    def __init__(self,list):
        if list == None:
            self.__A = []
        else:
            self.__A = list

    def insert(self,x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)

    def __percolateUp(self,i:int):
        parent = (i- 1)//2
        if i > 0 and self.__A[i] < self.__A[parent]:
            self.__A[i],self.__A[parent] = self.__A[parent],self.__A[i]
            self.__percolateUp(parent)

    def deleteMax(self):
        if(not self.isEmpty()):
            max = len(self.__A)-1
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)

    def __percolateDown(self,i:int):
        child = i*2 + 1
        right = i*2 + 2
        if(child <= len(self.__A)-1):
            if(right <= len(self.__A)-1 and self.__A[right] > self.__A[child]):
                child = right
            if self.__A[i] < self.__A[child]:
                self.__A[i],self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)
    def buildHeap(self):
        for i in range((len(self.__A)-2)//2,-1,-1):
            self.__percolateDown(i)