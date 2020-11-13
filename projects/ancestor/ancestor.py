from util import Queue

def get_ancestor(ancestors, child):
    heirs = []
    for heir in ancestors:
        if heir[1] == child:
            heirs.append(heir[0])
    return heirs


def earliest_ancestor(ancestors, starting_node):
    #create empty queue
    #add starting node to queue
     #create set to store visited vertices
     #initialize path length
      #sets oldest parent as -1 for if no parent
      
      #while size of q is greater than 0
      #dequeue first path
      #grab the last vertex from the path
      
      #if that vertex has not been visited
      #mark as visited
       
      #check for need to update
      
      #updates path length
       #updates oldest parent
        #then add a path to its parent to the back of the queue
         #copy path
         #append parent to the back
         pass