from pyhop_anytime import *
from gripper import *


def start(state, goals):
    pass


def make_gripper_planner():
    planner = Planner()
    planner.declare_operators(drop, move, pick)
    planner.declare_methods(start)
    return planner


if __name__ == '__main__':
    anyhop_main(make_gripper_planner())