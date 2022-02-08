def drop(state, obj, room, gripper):
    if obj in state.ball and room in state.room and gripper in state.gripper and (obj,gripper) in state.carry and room in state.at_robby:
        state.at.add((obj,room))
        state.free.add(gripper)
        state.carry.discard((obj,gripper))
        return state


def move(state, origin, to):
    if origin in state.room and to in state.room and origin in state.at_robby:
        state.at_robby.add(to)
        state.at_robby.discard(origin)
        return state


def pick(state, obj, room, gripper):
    if obj in state.ball and room in state.room and gripper in state.gripper and (obj,room) in state.at and room in state.at_robby and gripper in state.free:
        state.carry.add((obj,gripper))
        state.at.discard((obj,room))
        state.free.discard(gripper)
        return state


