from pyhop_anytime import *
global state, goals
state = State('state')
state.at = Oset([('ball1','rooma'),('ball2','rooma'),('ball3','rooma'),('ball4','rooma'),('ball5','rooma'),('ball6','rooma')])
state.at_robby = Oset(['rooma'])
state.ball = Oset(['ball1','ball2','ball3','ball4','ball5','ball6'])
state.free = Oset(['left','right'])
state.gripper = Oset(['left','right'])
state.room = Oset(['rooma','roomb'])
state.carry = Oset()

goals = State('goals')
goals.at = Oset([('ball1','roomb'),('ball2','roomb'),('ball3','roomb'),('ball4','roomb'),('ball5','roomb'),('ball6','roomb')])
