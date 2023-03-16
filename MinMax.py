import GameTree as gt


def leaf_evaluation(gtr):
    for i in gtr.nodes_list:
        if i.h1 == 0 and i.h2 == 0 and i.h3 == 0:
            if i.depth % 2 == 0:
                i.val = 1
            else:
                i.val = -1


def tree_eval(gtr, node):
    depth = node.depth
    if node.h1 > 0 or node.h2 > 0 or node.h3 > 0:
        if depth % 2 == 0:
            for i in gtr.arcs_dict[node.id]:
                temp_node = gtr.get_node(i)
                if temp_node.val == -2:
                    tree_eval(gtr, temp_node)
                if temp_node.val > node.val:
                    node.val = temp_node.val
        else:
            for i in gtr.arcs_dict[node.id]:
                temp_node = gtr.get_node(i)
                if temp_node.val == -2:
                    tree_eval(gtr, temp_node)
                if temp_node.val < node.val or node.val == -2:
                    node.val = temp_node.val
    else:
        return

leaf_evaluation(gt.NIM)
tree_eval(gt.NIM, gt.NIM.nodes_list[0])
