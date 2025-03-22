import math
def alpha_beta_pruning(depth, node_index, is_max, values, alpha, beta):
    if depth == 3: 
        return values[node_index] 
    if is_max:
        max_eval = -math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            print(f"Max Node: Depth {depth}, Node {node_index}, Alpha {alpha}, Beta {beta}")
            if beta <= alpha:
                print("Pruning occurs")
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            print(f"Min Node: Depth {depth}, Node {node_index}, Alpha {alpha}, Beta {beta}")
            if beta <= alpha:
                print("Pruning occurs")
                break
        return min_eval
values = [3, 5, 6, 9, 1, 2, 0, -1]
result = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf)
print("Final optimal value:", result)
