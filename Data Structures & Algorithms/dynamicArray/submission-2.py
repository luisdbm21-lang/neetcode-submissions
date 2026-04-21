class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array.append(n)
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.array.pop()

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity