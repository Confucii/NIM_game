class Node:
    def __init__(self, nid, h1, h2, h3, depth):
        self.id = nid
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.depth = depth
        self.val = -2


class GameTree:
    def __init__(self):
        self.nodes_list = list()
        self.arcs_dict = dict()

    def add_node(self, node):
        self.nodes_list.append(node)

    def add_arc(self, in_node, rec_node):
        self.arcs_dict[in_node] = self.arcs_dict.get(in_node, []) + [rec_node]

    def get_node(self, node_num):
        return self.nodes_list[int(node_num[1:]) - 1]


def moves(gt, heap, num, node_gen, current_node):
    if current_node[heap] - num >= 0:
        global nodenum
        new_heap_val = current_node[heap] - num
        new_id = "N" + str(nodenum)
        nodenum += 1
        new_node = [new_id, current_node[1], current_node[2], current_node[3], current_node[4] + 1]
        new_node[heap] = new_heap_val
        exists = False

        for i in range(len(gt.nodes_list)):
            if gt.nodes_list[i].h1 == new_node[1] and gt.nodes_list[i].h2 == new_node[2] and gt.nodes_list[i].h3 == new_node[3] and gt.nodes_list[i].depth == new_node[4]:
                exists = True
                nodenum -= 1
                gt.add_arc(current_node[0], gt.nodes_list[i].id)

        if not exists:
            node_gen.append([new_node[0], new_node[1], new_node[2], new_node[3], new_node[4]])
            gt.add_node(Node(new_node[0], new_node[1], new_node[2], new_node[3], new_node[4]))
            gt.add_arc(current_node[0], new_node[0])


def difference(in_node, rec_node):
    return abs(in_node.h1 - rec_node.h1 + in_node.h2 - rec_node.h2 + in_node.h3 - rec_node.h3)


NIM = GameTree()
temp_list = list()
val1 = 3
val2 = 5
val3 = 7
NIM.add_node(Node('N1', val1, val2, val3, 0))
temp_list.append(['N1', val1, val2, val3, 0])

nodenum = 2

while len(temp_list) > 0:
    for i in range(NIM.nodes_list[0].h1):
        moves(NIM, 1, i + 1, temp_list, temp_list[0])
    for i in range(NIM.nodes_list[0].h2):
        moves(NIM, 2, i + 1, temp_list, temp_list[0])
    for i in range(NIM.nodes_list[0].h3):
        moves(NIM, 3, i + 1, temp_list, temp_list[0])
    temp_list.pop(0)
