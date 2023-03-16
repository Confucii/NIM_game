import PySimpleGUI as gui
import Game as play
import MinMax

first_heap = play.gt.val1
second_heap = play.gt.val2
third_heap = play.gt.val3
turn = False
in_turn = False

gui.theme("Topanga")


def make_pre_window():
    p_layout = [[gui.Text("Who starts the game?")],
                [gui.Button("Computer")], [gui.Button("Player")],
                [gui.Button("Exit")]]
    pre_window = gui.Window(title="Who starts", layout=p_layout, margins=(50, 50))
    return pre_window


def make_main_window():
    m_layout = [[gui.Text("Game of Nim")],
                [gui.Text(first_heap, key='-FIRST-'), gui.Text(second_heap, key="-SECOND-"),
                gui.Text(third_heap, key='-THIRD-')],
                [gui.Text("Subtract any number"), gui.Input(key='-SUB-', enable_events=True)],
                [gui.Button("Subtract from first."), gui.Button("Subtract from second."),
                gui.Button("Subtract from third."), ],
                [gui.Output(key='-LOG-', size=(60, 5))],
                [gui.Button("Exit")]]
    window = gui.Window(title="NIM", layout=m_layout, margins=(75, 75))
    return window


def make_end_window(winner):
    e_layout = [[gui.Text(winner)],
                [gui.Button("Play again")],
                [gui.Button("Exit")]]
    end_window = gui.Window(title="End", layout=e_layout)
    return end_window


window, pre_window = make_main_window(), make_pre_window()

while True:
    event, values = pre_window.read()
    if event == gui.WIN_CLOSED or event == 'Exit':
        exit()
    if event == 'Computer':
        in_turn = True
        comp = 'MAX'
        break
    else:
        comp = 'MIN'
        break
pre_window.close()


while True:
    event, values = window.read()

    if in_turn:
        (first_heap, second_heap, third_heap) = play.computer_turn(comp)
        print("Computer turn:", first_heap, second_heap, third_heap)
        window['-FIRST-'].update(first_heap)
        window['-SECOND-'].update(second_heap)
        window['-THIRD-'].update(third_heap)
        in_turn = False

    if event == gui.WIN_CLOSED or event == 'Exit':
        break

    if event == '-SUB-' and values['-SUB-'] and values['-SUB-'][-1] not in str([1, 2, 3, 4, 5, 6, 7, 8, 9]) or len(values['-SUB-']) > 1:
        window['-SUB-'].update(values['-SUB-'][:-1])

    if event == "Subtract from first." and len(values['-SUB-']) == 1 and first_heap > 0 and len(values['-SUB-']) == 1:
        turn = False
        first_heap = first_heap - int(values['-SUB-'])
        if first_heap < 0:
            first_heap = 0
        window['-SUB-'].update('')
        window['-FIRST-'].update(first_heap)
        play.curr_node.change_node(play.gt.NIM, play.sc.find_node(play.curr_node.access, first_heap, second_heap, third_heap))
        print("Player turn:", first_heap, second_heap, third_heap)
        if first_heap != 0 or second_heap != 0 or third_heap != 0:
            turn = True
            (first_heap, second_heap, third_heap) = play.computer_turn(comp)
            print("Computer turn:", first_heap, second_heap, third_heap)
            window['-FIRST-'].update(first_heap)
            window['-SECOND-'].update(second_heap)
            window['-THIRD-'].update(third_heap)

    if event == "Subtract from second." and len(values['-SUB-']) == 1 and second_heap > 0 and len(values['-SUB-']) == 1:
        turn = False
        second_heap = second_heap - int(values['-SUB-'])
        if second_heap < 0:
            second_heap = 0
        window['-SUB-'].update('')
        window['-SECOND-'].update(second_heap)
        play.curr_node.change_node(play.gt.NIM, play.sc.find_node(play.curr_node.access, first_heap, second_heap, third_heap))
        print("Player turn:", first_heap, second_heap, third_heap)
        if first_heap != 0 or second_heap != 0 or third_heap != 0:
            turn = True
            (first_heap, second_heap, third_heap) = play.computer_turn(comp)
            print("Computer turn:", first_heap, second_heap, third_heap)
            window['-FIRST-'].update(first_heap)
            window['-SECOND-'].update(second_heap)
            window['-THIRD-'].update(third_heap)

    if event == "Subtract from third." and len(values['-SUB-']) == 1 and third_heap > 0 and len(values['-SUB-']) == 1:
        turn = False
        third_heap = third_heap - int(values['-SUB-'])
        if third_heap < 0:
            third_heap = 0
        window['-SUB-'].update('')
        window['-THIRD-'].update(third_heap)
        play.curr_node.change_node(play.gt.NIM, play.sc.find_node(play.curr_node.access, first_heap, second_heap, third_heap))
        print("Player turn:", first_heap, second_heap, third_heap)
        if first_heap != 0 or second_heap != 0 or third_heap != 0:
            turn = True
            (first_heap, second_heap, third_heap) = play.computer_turn(comp)
            print("Computer turn:", first_heap, second_heap, third_heap)
            window['-FIRST-'].update(first_heap)
            window['-SECOND-'].update(second_heap)
            window['-THIRD-'].update(third_heap)

    if first_heap == 0 and second_heap == 0 and third_heap == 0:
        if not turn:
            e_w = make_end_window('Computer won!')
        else:
            e_w = make_end_window('Player won!')
        while True:
            event, value = e_w.read()

            if event == gui.WIN_CLOSED or event == 'Exit':
                exit()

            if event == 'Play again':
                first_heap = play.gt.val1
                second_heap = play.gt.val2
                third_heap = play.gt.val3
                window['-FIRST-'].update(first_heap)
                window['-SECOND-'].update(second_heap)
                window['-THIRD-'].update(third_heap)
                print('- - - - - - - - - - - - -')
                print('New Game')
                pre_window = make_pre_window()
                while True:
                    event, values = pre_window.read()
                    if event == gui.WIN_CLOSED or event == 'Exit':
                        exit()
                    if event == 'Computer':
                        in_turn = True
                        comp = 'MAX'
                        break
                    else:
                        comp = 'MIN'
                        break
                play.curr_node = play.sc.CN(play.gt.NIM)
                play.curr_node.change_node(play.gt.NIM, play.curr_node.current_node)
                pre_window.close()
                break
        e_w.close()
window.close()
