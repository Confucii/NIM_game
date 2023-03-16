def find_node(access, h1, h2, h3):
    for i in access:
        if i.h1 == h1 and i.h2 == h2 and i.h3 == h3:
            return i
    else:
        return "No such node"


class CN:
    def __init__(self, tree):
        self.current_node = tree.nodes_list[0]
        self.access = list()

    def change_node(self, tree, node):
        self.current_node = node
        if node.h1 != 0 or node.h2 != 0 or node.h3 != 0:
            self.access.clear()
            for i in range(len(tree.arcs_dict[node.id])):
                self.access.append(tree.nodes_list[int(tree.arcs_dict[node.id][i][1:]) - 1])