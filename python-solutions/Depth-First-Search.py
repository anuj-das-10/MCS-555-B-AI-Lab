def DFS(graph, visited, current_vertex):
    print(current_vertex, end = " ")
    visited[current_vertex] = True

    for i in range(len(graph[current_vertex])):
        neighbour = graph[current_vertex][i]
        if not visited[neighbour]:
            DFS(graph, visited, neighbour)




"""
public static void DFS(ArrayList<Edge> graph[], boolean visited[], int current_vertex) {
        System.out.print(current_vertex + " ");
        visited[current_vertex] = true;
        
        for(int i = 0; i < graph[current_vertex].size(); i++) {
            Edge e = graph[current_vertex].get(i);
            if(visited[e.dest] == false) {
                DFS(graph, visited, e.dest);
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
start_node = 4                              # Starting node for DFS traversal
visited = [False for i in range(V)]         # Initializing with all visited vertex as "False"

print("DFS Traversal:  ", end=' ')
DFS(graph, visited, start_node)