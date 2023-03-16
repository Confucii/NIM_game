import Search_Current as sc
import GameTree as gt

curr_node = sc.CN(gt.NIM)
curr_node.change_node(gt.NIM, curr_node.current_node)


def computer_turn(dec):
    temp_list = list()
    temp_dict = dict()
    bad = False
    if dec == 'MAX':
        for i in curr_node.access:
            if i.val == 1:
                temp_list.append(i)
        if len(temp_list) == 0:
            for i in curr_node.access:
                temp_list.append(i)
                bad = True
        for i in temp_list:
            temp_dict[i] = gt.difference(curr_node.current_node, i)
        if bad:
            turn = min(temp_dict.values())
        else:
            turn = max(temp_dict.values())
        for node, val in temp_dict.items():
            if val == turn:
                curr_node.change_node(gt.NIM, node)
        return curr_node.current_node.h1, curr_node.current_node.h2, curr_node.current_node.h3
    else:
        for i in curr_node.access:
            if i.val == -1:
                temp_list.append(i)
        if len(temp_list) == 0:
            for i in curr_node.access:
                temp_list.append(i)
                bad = True
        for i in temp_list:
            temp_dict[i] = gt.difference(curr_node.current_node, i)
        if bad:
            turn = min(temp_dict.values())
        else:
            turn = max(temp_dict.values())
        for node, val in temp_dict.items():
            if val == turn:
                curr_node.change_node(gt.NIM, node)
        return curr_node.current_node.h1, curr_node.current_node.h2, curr_node.current_node.h3
