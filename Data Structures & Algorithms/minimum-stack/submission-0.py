class MinStack:


    def __init__(self):
        
        self.minstack = []
        self.min_values = []

    def push(self, val: int) -> None:
        
        self.minstack.append(val)

        if not self.min_values or val <= self.min_values[-1] :

            self.min_values.append(val)



    def pop(self) -> None:
        
        if self.minstack[-1] == self.min_values[-1]:
               self.min_values.pop()

        if self.minstack:
            self.minstack.pop()
        


    def top(self) -> int:
        
        return self.minstack[-1]

    def getMin(self) -> int:
        
        if self.minstack:

            return self.min_values[-1]
