#TODO write tests here

from functools import partial

from main.terminal_actions.printing import print_actions

actions = {
    "help": partial(print_actions),
    "look around": partial(print, "get_room_content"),
    "exit": partial(exit, 0)
}
