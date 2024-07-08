
#? What is Trie and Why we need it
#  A Trie is a tree-based data structure that organizes information in a hierarchy.
# It is often used for strings. It stores characters at each node, making it easy for prefix matxhing.

#* Properties
# It is typically used to store or search steings in a spcae and time efficient way
# Any node in trie can store non repetitive multiple characters
# Every node stores link of the next character of the string
# Every node keeps track of "end of string"

#? If you want to store AIR, then if need to add T, then if BAR
#          AB
#         / \
#        I   A
#       /    /
#     R T    R
#     /  \   /
#    .    .  .

#? Why we need it?
#* Spelling Checker
#* Auto completion

#* google predicting, what you'll type next while searching, might be using advanced technologies.

#? This is how it looks

# # # # # # # # # # # # # # # # # # # 
#             MAP                   # 
# # # # # # # # # # # # # # # # # # # 
# Characters  #  Link to Trie Node  # 
#             #                     # 
#             #                     # 
#             #                     # 
#             #                     # 
# # # # # # # # # # # # # # # # # # # 
#        End of String              # 
# # # # # # # # # # # # # # # # # # # 

#? Common Operations on Trie
#* Creation of Trie
#* Insertion of Trie
#* Search for a string in trie
#* Deletion from Trie


#! Creation of Trie
#* Initialize Trie Calss
#*       (    )
#*       Logical       looks like above table

class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    #! Insertion of a string in a Trie
    #* It has 4 cases:
    #* Case 1: The Trie is Blank
    #* Case 2: New strings prefix is common to another strings prefix
    #* Case 3: String to be inserted is already presented in Trie
        
    def insertString(self, word):          #! ------------> TC = O(m), SC = O(m)
        current = self.rootNode                        # ------------> TC = O(1)
        for i in word:
            char = i
            node = current.children.get(char)
            if node == None:
                node = TrieNode()
                current.children.update({char: node})
            current = node
        current.endOfString = True
        print("Success")
    
    #! Search for a string in trie
    #* Case 1: string doesn't exist in Trie
    #* Case 2: String is a prefix of another string, but it doesn't exist in Trie.
    
    def search(self, word):                #! ------------> TC = O(m), SC = O(1)
        currentNode = self.rootNode
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        
        if currentNode.endOfString == True:
            return True
        else:
            return False
        
#! Deletion from Trie
#* Some other prefix of string is same as the one that we want to delete. (API, APPLE).
#* The string is a prefix of another string. (API, APIS), here won't delete, just set end of string to false
#* Other sting is a prefix of this string. (APIS, AP)
#* Noe any node depends on string
#* Deletion starts from leaf, and go up
        
def deleteString(rootNode, word, index):
    char = word[index]
    currentNode = rootNode.children.get(char)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            rootNode.children.pop(char)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        rootNode.children.pop(char)
        return True
    else:
        return False



newTrie = Trie()                           #! ------------> TC = O(1), SC = O(1)
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.rootNode, "App", 0)
print(newTrie.search("App"))