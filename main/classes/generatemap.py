import random

class Node:
    def __init__(self, id, value, neighbors=None):
        self.id = id
        self.value = value
        if neighbors is Node:
            self.neighbors = []
        else:
            self.neighbors = neighbors

    def add_neighboor(self, neighboor):
        self.neighbors.append(neighboor)
    
    def count_neighbors(self):
        return(len(self.neighbors))    
        
        
#https://python.plainenglish.io/graph-data-structure-theory-and-python-implementation-ee8c9795eae7        
        
class MapGraph:
    def __init__(self, nodes=None):
        
        if nodes is None:
            self.nodes = []
            
        else:
            self.nodes = nodes
            
    def add_node(self, id, value, neighboor=None):
        self.nodes.append(Node(id, value, neighboor))
        
    def find_node(self, id):
        for node in self.nodes:
            if node.id == id:
                return node
            return None   
        
    def add_edge(self, id1, id2):
        node1 = self.find_node(id1)
        node2 = self.find_node(id2)
        
        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor(node2)
            node2.add_neighboor(node1)
            
    def createmap(self, size):
        choices = ["nothing", "nothing", "nothing", "stats", "lore", "score", [random.randint(1, 3), random.randint(0, 5)], "heal"]
        
        for i in range(size):
            self.add_node(i, random.choice(choices))
            
        for i in range(size):
            #roll 1-2, pegar aleatorio  1-quantos nodos temos (size), ver se o nodo tem < 3
            #se sim criar edge desse nodo para o nosso nodo, se não voltar para step 2, adicionar uma lista de nodos já selecionados (se a lista tiver todos os números, break (começa com o nodo atual))
            node = self.find_node(i)
            j = random.randint(1, 2)
            already = [i]
            
            if len(node.neighbors) >= 2:
                    continue
            else:
                while len(node.neighbors) < j:
                    target = self.find_node(random.randint(0, size-1))
                    if len(target.neighbors) < 3:
                         self.add_edge(target, node)
                    else:
                        already.append(target)
                        if len(already) is len(size):
                            break
                        else:
                            continue
    
                
             
    
    
    
        