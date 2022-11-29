class Stack:
    def __init__(self,exp):
        self.openingBraces=[]
        self.exp=list(exp)
    def __str__(self):
        values=[str(x) for x in self.exp]
        return ''.join(values)

    def str1(self):
        values=[str(x) for x in self.openingBraces]
        return ''.join(values)

    def push(self):
        print(self.exp)
        for i in range(len(self.exp)):
            print(self.exp[i])
            if self.exp[i] =="{" or self.exp[i] == "(" or self.exp[i] =="[":
                self.openingBraces.append(self.exp[i])
        self.openingBraces.reverse()
        return self.openingBraces

    def pop(self):
        for i in range(len(self.exp)):
            if self.exp[i] == "}" or self.exp[i] == ")" or self.exp[i] =="]":
                if self.openingBraces[0] == "{" and self.exp[i] =="}":
                    self.openingBraces.pop(0)
                elif self.openingBraces[0] == "(" and self.exp[i] ==")":
                    self.openingBraces.pop(0)
                elif self.openingBraces[0] == "[" and self.exp[i] =="]":
                    self.openingBraces.pop(0)
            return "Balanced"
        return "Not Balanced"




custStack=Stack("[(])")
print(custStack.push())
print(custStack.pop())
