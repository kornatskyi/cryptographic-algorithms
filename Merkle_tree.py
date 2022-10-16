import hashlib
import os
 
# Clearing the console
os.system('clear')


# *____Utils____*
# siplify calling sha256 function from hashlib, returns hexidesimal value
def sha256(message):
  return hashlib.sha256(message.encode("utf-8")).hexdigest()


# Verify that two merkle trees are equal



class Node: 
  def __init__(self, value:str, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    pass
pass

leafs = ['leaf0', 'leaf1','leaf2','leaf3','leaf4','leaf5','leaf6','leaf7']


class MerkleTree:
  def __init__(self, leafsValues:list[str]) -> None:

    leafHashes = [sha256(leaf) for leaf in leafsValues]
    currentLevelNodes:list[Node]=[Node(leafHash) for leafHash in leafHashes]
    levelLenght = currentLevelNodes.__len__()
    while(levelLenght > 1):
      if levelLenght % 2 == 1:
        levelLenght = int((levelLenght / 2) +1)
      else:
        levelLenght = int((levelLenght / 2))
      pass

      newLevelNodes=[]

      for i in range(levelLenght):
        leftChild=currentLevelNodes[i * 2]
        # check if number of nodes on the current level is odd(actuall it can apply only for the firs level)
        if currentLevelNodes.__len__() % 2 == 1:
          rigthChild=currentLevelNodes[i * 2]
        else:
          rigthChild=currentLevelNodes[(i * 2) + 1]
        pass
        newLevelNodes.append(Node(sha256(leftChild.value + rigthChild.value), leftChild, rigthChild))
      pass
      currentLevelNodes=newLevelNodes
    pass
    self.root = currentLevelNodes[0]
  pass
pass

tree=MerkleTree(leafs)
print(tree.root.value)
    


