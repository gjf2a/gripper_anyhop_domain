from pyhop_anytime import *
global state, goals
state = State('state')
state.at = Oset([('ball1','rooma'),('ball10','rooma'),('ball11','rooma'),('ball12','rooma'),('ball13','rooma'),('ball14','rooma'),('ball15','rooma'),('ball16','rooma'),('ball17','rooma'),('ball18','rooma'),('ball19','rooma'),('ball2','rooma'),('ball20','rooma'),('ball21','rooma'),('ball22','rooma'),('ball23','rooma'),('ball24','rooma'),('ball25','rooma'),('ball26','rooma'),('ball27','rooma'),('ball28','rooma'),('ball29','rooma'),('ball3','rooma'),('ball30','rooma'),('ball31','rooma'),('ball32','rooma'),('ball4','rooma'),('ball5','rooma'),('ball6','rooma'),('ball7','rooma'),('ball8','rooma'),('ball9','rooma')])
state.at_robby = Oset(['rooma'])
state.ball = Oset(['ball1','ball10','ball11','ball12','ball13','ball14','ball15','ball16','ball17','ball18','ball19','ball2','ball20','ball21','ball22','ball23','ball24','ball25','ball26','ball27','ball28','ball29','ball3','ball30','ball31','ball32','ball4','ball5','ball6','ball7','ball8','ball9'])
state.free = Oset(['left','right'])
state.gripper = Oset(['left','right'])
state.room = Oset(['rooma','roomb'])
state.carry = Oset()

goals = State('goals')
goals.at = Oset([('ball1','roomb'),('ball10','roomb'),('ball11','roomb'),('ball12','roomb'),('ball13','roomb'),('ball14','roomb'),('ball15','roomb'),('ball16','roomb'),('ball17','roomb'),('ball18','roomb'),('ball19','roomb'),('ball2','roomb'),('ball20','roomb'),('ball21','roomb'),('ball22','roomb'),('ball23','roomb'),('ball24','roomb'),('ball25','roomb'),('ball26','roomb'),('ball27','roomb'),('ball28','roomb'),('ball29','roomb'),('ball3','roomb'),('ball30','roomb'),('ball31','roomb'),('ball32','roomb'),('ball4','roomb'),('ball5','roomb'),('ball6','roomb'),('ball7','roomb'),('ball8','roomb'),('ball9','roomb')])

