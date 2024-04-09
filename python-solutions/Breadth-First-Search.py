from queue import Queue

def BFS(graph, visited, start_vertex):
    queue = Queue()
    queue.put(start_vertex)

    while not queue.empty():
        current_vertex = queue.get()
        if not  visited[current_vertex]:
            print(current_vertex, end = "  ")
            visited[current_vertex] = True
            #  Visiting all adjacent vertices of current vertex
            for i in range(len(graph[current_vertex])):
                neighbour = graph[current_vertex][i]
                queue.put(neighbour)





"""
public static void BFS(ArrayList<Edge> graph[], boolean visited[], int starting_vertex) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(starting_vertex);

        while(!queue.isEmpty()) {
            int currentVertex = queue.remove();
            if(visited[currentVertex] == false) {
                System.out.print(currentVertex + " ");
                visited[currentVertex] = true;
                
                // Get all adjacent vertices of the current vertex. 
                // If a neighbor is not yet visited, then add it to the queue.
                for(int i = 0; i < graph[currentVertex].size() ; i++) {
                    Edge e = graph[currentVertex].get(i);
                    queue.add(e.dest);
                }
            }
        }
        
    }

"""


# Example graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4, 5],
    4: [2, 3, 5],
    5: [3, 4, 6],
    6: [5],
}

V = 7                                       # Number of vertices
start_node = 0                              # Starting node for BFS traversal
visited = [False for i in range(V)]         # Initializing with all visited vertex as "False"
print("BFS Traversal:  ", end=' ')
BFS(graph, visited, start_node)