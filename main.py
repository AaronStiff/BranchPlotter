from ete3 import Tree, TreeStyle, Tree, TextFace, add_face_to_node

p_b = dict()
branches = set()
parents = set()

with open('branches_parents.csv', 'r') as csv_branches:
    for line in csv_branches:
        b, p = line.strip('\n').split(',')

        try:
            if p_b[p]:
                p_b[p].append(b)
        except KeyError:
            p_b[p] = [b]

        branches.add(b)
        parents.add(p)

del p_b['Parent']
branches.remove('Branch')
parents.remove('Parent')

branches = sorted(list(branches))
parents = sorted(list(parents))

roots = [p for p in parents if p not in branches]

def get_branch(parent):
    if parent in p_b.keys():
        return '((' + ','.join([get_branch(branch) for branch in p_b[parent]]) + ')' + parent + ')'
    else:
        return parent

hierarchy = [get_branch(root) for root in roots]

tree_string = '(' + ','.join(hierarchy) + ');'

t = Tree(tree_string, format=8)
ts = TreeStyle()

def my_layout(node):
    F = TextFace(node.name, ftype='Calibri')
    add_face_to_node(F, node, column=0, position="branch-right")

ts.layout_fn = my_layout
ts.scale = 200
ts.show_leaf_name = False

t.show(tree_style = ts)
