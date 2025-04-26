from collections import deque

MAX = 10

def depth_first_search(adj, visited, start, goal, n):
    open_list = [start]  # Stack
    closed_list = []  # Visited nodes
    dfs_path = []
    
    print("\n===== DFS TRAVERSAL =====")
    print(f"{'Step':<10}{'Stack':<40}{'Visited Node':<10}")
    print("-" * 60)
    
    step = 1
    while open_list:
        x = open_list.pop()  # Pop the last element (LIFO)
        print(f"{step:<10}{str(open_list):<40}{x:<10}")  # Print Stack & Visited Node
        dfs_path.append(x)
        
        if x == goal:
            print("\nGoal reached! Final DFS Path:", " -> ".join(map(str, dfs_path)))
            return

        if x not in closed_list:
            closed_list.append(x)
            visited[x] = True  # Mark as visited

            # Generate children in LEFT-to-RIGHT order
            children = [i for i in range(n) if adj[x][i] and not visited[i]]

            # Push children onto stack in REVERSE order (so they appear in correct order when popped)
            for child in reversed(children):
                open_list.append(child)
                visited[child] = True  # Mark as visited when pushed

        step += 1

    print("\nFinal DFS Path:", " -> ".join(map(str, dfs_path)))




def breadth_first_search(adj, visited, start, goal, n):
    queue = deque()
    bfs_path = []
    queue.append(start)
    visited[start] = True
    step = 1
    
    print("\n===== BFS TRAVERSAL =====")
    print(f"{'Step':<10}{'Queue':<40}{'Visited Node':<10}")
    print("-" * 60)
    
    while queue:
        print(f"{step:<10}{str(list(queue)):<40}{queue[0]:<10}")
        start = queue.popleft()
        bfs_path.append(start)
        
        if start == goal:
            print("\nGoal reached! Final BFS Path:", " -> ".join(map(str, bfs_path)))
            return
        
        for i in range(n):
            if adj[start][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
        step += 1
    
    print("\nFinal BFS Path:", " -> ".join(map(str, bfs_path)))

def main():
    n = int(input("\nEnter the number of nodes: "))
    adj = []
    print("\nEnter the adjacency matrix:")
    for _ in range(n):
        adj.append(list(map(int, input().split())))
    
    start = int(input("\nEnter starting node: "))
    goal = int(input("\nEnter goal node: "))
    
    visited = [False] * MAX
    breadth_first_search(adj, visited, start, goal, n)
    
    visited = [False] * MAX
    depth_first_search(adj, visited, start, goal, n)

if __name__ == "__main__":
    main()

