# I know we learned about biopython, but it keeps failing to install. I have a work 
# computer so I do not have Root access. Tried the normal way via pip, pip3, 
# downgrade python, create conda enviorment, etc. The closest was with conda enviorment 
# but then it failed to import biopython. Using Bio i would probalby write 
# from Bio import Phylom, from io import StringIO or something like this 
# this way we would have a shorter and cleaner code. 



def newick_distance(tree_str, pair):
    def parse_newick(s):
        stack = []
        node = {}
        current_name = ''
        
        for char in s:
            if char == '(':
                stack.append(node)
                node = {}
            elif char == ',':
                if current_name:
                    node['name'] = current_name.strip()
                    current_name = ''
                if stack:
                    if 'subtrees' not in stack[-1]:
                        stack[-1]['subtrees'] = []
                    stack[-1]['subtrees'].append(node)
                node = {}
            elif char == ')':
                if current_name:
                    node['name'] = current_name.strip()
                    current_name = ''
                if stack:
                    child = node
                    node = stack.pop()
                    if 'subtrees' not in node:
                        node['subtrees'] = []
                    node['subtrees'].append(child)
            elif char == ';':
                if current_name:
                    node['name'] = current_name.strip()
            else:
                current_name += char
        
        return node
    
    def find_path(node, target, path=[]):
        if 'name' in node and node['name'] == target:
            return path + [node['name']]
        if 'subtrees' in node:
            for subtree in node['subtrees']:
                result = find_path(subtree, target, path + [node['name']] if 'name' in node else path)
                if result:
                    return result
        return None

    def find_lca(path1, path2):
        lca_path = []
        for u, v in zip(path1, path2):
            if u == v:
                lca_path.append(u)
            else:
                break
        return lca_path

    tree = parse_newick(tree_str)
    path1 = find_path(tree, pair[0])
    path2 = find_path(tree, pair[1])

    if path1 is None or path2 is None:
        return None

    lca_path = find_lca(path1, path2)

    distance = (len(path1) - len(lca_path)) + (len(path2) - len(lca_path))
    return distance

tree_str = "((A,B),(C,D));"
pair = ("A", "D")
print(newick_distance(tree_str, pair))