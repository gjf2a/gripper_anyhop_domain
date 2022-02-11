from pyhop_anytime import *
from gripper import *


def start(state, goals):
    undelivered = [(ball, destination) 
                   for ball, destination in goals.at 
                   if (ball, destination) not in state.at and destination not in state.at_robby]
    if len(undelivered) == 0:
        return TaskList(completed=True)
    else:
        return TaskList([('select', undelivered), ('start', goals)])
    
    
def select(state, undelivered):
    empty_grippers = [gripper for gripper in state.free]
    if len(empty_grippers) == 0:
        return TaskList([('deliver_gripped', state.carry)])
    else:
        room = state.at_robby.get_first()
        return TaskList([[('pick', obj[0], room, gripper)] for gripper in empty_grippers for obj in undelivered])


def deliver_gripped(state, carried):
    tasks = [('move', 'rooma', 'roomb')]
    for obj, gripper in carried:
        tasks.append(('drop', obj, 'roomb', gripper))
    tasks.append(('move', 'roomb', 'rooma'))
    return TaskList(tasks)
    

def make_gripper_planner():
    planner = Planner()
    planner.declare_operators(drop, move, pick)
    planner.declare_methods(start, select, deliver_gripped)
    return planner


if __name__ == '__main__':
    anyhop_main(make_gripper_planner())