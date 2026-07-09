class Solution:
    def add(self, a,b) -> int:
        return a+b
    def subtract(self, a,b) -> int:
        return a-b
    def multiply(self, a,b) -> int:
        return a*b
    def divide(self, a,b) -> int:
        return int(a / b)
    
    def evalRPN(self, tokens: List[str]) -> int:
        temp=0
            
        stack=[]
        operators = {"+": self.add, "-":self.subtract, "*":self.multiply, "/":self.divide}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            
            else:

                a= stack.pop()
                b= stack.pop()
                
                temp = operators[i](b,a)

                stack.append(temp)

        return stack[0]