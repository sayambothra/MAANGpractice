class Node():
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
    def __str__(self):
        string=str(self.value)
        if self.next:
            str += '->'+str(self.next)
        return string
class Stack():
    def __init__(self):
        self.Top=None
        self.minNode=None
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value

    def push(self,value):

