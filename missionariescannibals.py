from collections import deque

def is_valid(state, total_missionaries, total_cannibals):
    missionaries, cannibals, _ = state
    return (0 <= missionaries <= total_missionaries) and (0 <= cannibals <= total_cannibals) and (missionaries >= cannibals or missionaries == 0)

def get_next_states(current_state, total_missionaries, total_cannibals):
    states = []
    missionaries, cannibals, boat = current_state
    
    for move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
        if boat == 'left':
            new_state = (missionaries - move[0], cannibals - move[1], 'right')
        else:
            new_state = (missionaries + move[0], cannibals + move[1], 'left')
        
        if is_valid(new_state, total_missionaries, total_cannibals):
            states.append(new_state)
    
    return states

def solve(total_missionaries, total_cannibals):
    initial_state = (total_missionaries, total_cannibals, 'left')
    goal_state = (0, 0, 'right')

    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [current_state]
        
        visited.add(current_state)
        
        for next_state in get_next_states(current_state, total_missionaries, total_cannibals):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
                visited.add(next_state)
    
    return None

def main():
    total_missionaries = int(input("Enter the total number of missionaries: "))
    total_cannibals = int(input("Enter the total number of cannibals: "))
    
    result = solve(total_missionaries, total_cannibals)

    if result:
        for state in result:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
