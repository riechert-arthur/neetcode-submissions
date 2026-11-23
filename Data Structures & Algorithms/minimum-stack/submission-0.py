class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        if len(self.items) > 0:
            if self.items[-1] == self.mins[-1]:
                self.mins.pop()
            return self.items.pop()
        return None

    def top(self) -> int:
        return self.items[-1] if len(self.items) > 0 else None

    def getMin(self) -> int:
        return self.mins[-1] if len(self.mins) > 0 else None
        
