#Creation of Trie - TC:O(1),SC:O(1)
class TrieNode:
    def __init__(self):
        self.children ={}
        self.endOfString = False

class trie:
    def __init__(self):
        self.root=TrieNode()

    #insert a String in trie - TC:O(n),SC:O(n); where n is length of string
    def insertString(self,word):
        current=self.root
        for i in word:
            ch=i;
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endOfString=True
        print("Successfully Inserted")
    #Search for string in trie - TC:O(n),SC:O(1); where n is length of string
    def Search(self,word):
        current=self.root
        for i in word:
            node=current.children.get(i)
            if node == None:
                return "False"
            current=node

        if current.endOfString == True :
            return True
        else:
            return False

#Delete a node
def deleteString(root,word,index):
    ch=word[index]
    currentNode=root.children.get(ch)
    canThisNodeBeDeleted = False

    #Case 1 :
    if len(currentNode.children)>1:
        deleteString(currentNode,word,index+1)
        return False

    #Case 2
    if index ==len(word) -1:
        if len(currentNode.children)>=1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    #Case 3 -
    if currentNode.endOfString == True:
        deleteString(currentNode,word,index+1)
        return False

    #Case 4 -
    canThisNodeBeDeleted = deleteString(currentNode,word,index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

newTrie=trie()
newTrie.insertString("APP")
newTrie.insertString("APPL")
deleteString(newTrie.root,"APP",0)
print(newTrie.Search("APPL"))
