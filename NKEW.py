import re

class TreeNode:
    def __init__(self, name='', weight=None):
        self.name = name
        self.weight = weight
        self.descendants = []

def parse_newick(newick_str):
    def parse_subtree(subtree_str):
        subtree_str = subtree_str.strip()
        if not subtree_str:
            return None, ''
        if subtree_str[0] == '(':
            subtree_str = subtree_str[1:]
            node = TreeNode()
            stack = [node]
            while stack:
                current = stack[-1]
                if subtree_str[0] == '(':
                    descendant, subtree_str = parse_subtree(subtree_str)
                    current.descendants.append(descendant)
                    stack.append(descendant)
                elif subtree_str[0] == ')':
                    stack.pop()
                    subtree_str = subtree_str[1:]
                elif subtree_str[0] == ',':
                    subtree_str = subtree_str[1:]
                elif subtree_str[0] == ';':
                    subtree_str = subtree_str[1:]
                    break
                else:
                    match = re.match(r'[^(),;]+', subtree_str)
                    name = match.group()
                    subtree_str = subtree_str[match.end():]
                    current.name = name
            return node, subtree_str
        else:
            match = re.match(r'[^(),;]+', subtree_str)
            name = match.group()
            subtree_str = subtree_str[match.end():]
            return TreeNode(name=name), subtree_str

    tree, _ = parse_subtree(newick_str)
    return tree

def add_edge_weights(root, starting_weight=1):
    weights = []
    
    def assign_weights(node, current_weight):
        for descendant in node.descendants:
            weights.append(current_weight)
            assign_weights(descendant, current_weight + 1)
            current_weight += 1
    
    assign_weights(root, starting_weight)
    return weights

newick_str_rome = "((A,B)C,(D,E)F)G;"
root_rome = parse_newick(newick_str_rome)
weights_rome = add_edge_weights(root_rome)
print("Rome's edge weights:", ' '.join(map(str, weights_rome)))

newick_str_brussels = "((X,Y)Z,(P,Q)R)S;"
root_brussels = parse_newick(newick_str_brussels)
weights_brussels = add_edge_weights(root_brussels)
print("Brussels' edge weights:", ' '.join(map(str, weights_brussels)))