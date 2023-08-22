from collections import defaultdict;
class Graph:
    def _init_(self):
        self.graph=defaultdict(list);
        self.dfs=" ";
        self.found=False;
    def addEdge(Self,u,v):
        self.graph[u].append(v);
    def DFSUtil(self,root,search,visited):
        visited.add(root)
        self.dfs=self.dfs+root+" ";
        if(root== search):
            self.found=True;
            return;
        for neighbour in self.graph[root]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,search,visited);
    def DFS(Self,root,search):
        visited=set();
        self.DFSUtil(root,search,visited);
g=Graph();
n=int(input("enter no.of nodes"));
root=input("enter root node");
search=input("enter serach element");
print("enter vertices of tree");
for i in range(0,n-1):
    s=input();
    x=s.split(", ");
    g.addEdge(x[0],x[1]);
g.DFS(root,search);
if(g.found):
    print("following is the dfs");
else:
    print("given element not found in tree");