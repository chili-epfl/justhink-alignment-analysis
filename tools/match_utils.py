
class Edge(object):
    def __init__(self, u, v):
        self.u = int(u) if u is not None else u
        self.v = int(v) if v is not None else v

    def __eq__(self, other):
        if isinstance(other, Edge):
            return (self.u == other.u and self.v == other.v) \
                or (self.u == other.v and self.v == other.u)

    def __hash__(self):
        return hash((self.u, self.v))

    def __str__(self):
        if self.v is None:
            v = '?'
        else:
            v = self.v
        return '{},{}'.format(self.u, v)


class Action(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __eq__(self, other):
        if isinstance(other, Action):
            return self.name == other.name \
                and self.content == other.content

    def partial_equals(self, other):
        assert isinstance(self.content, Edge) and isinstance(
            other.content, Edge), 'not implemented'
        if self.name != other.name:
            return False
        u, v = self.content.u, self.content.v
        ou, ov = other.content.u, other.content.v
        if v is None or ov is None:
            return u == ou or u == ov or v == ou or v == ov
        else:
            return (u == ou or u == ov) and (v == ou or v == ov)

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return hash((self.name, self.content))

    def __repr__(self):
        return '{}({})'.format(self.name, self.content)


class AddAction(Action):
    def __init__(self, edge):
        self.name = 'ADD'
        self.edge = edge
        super().__init__(self.name, self.edge)


class RemoveAction(Action):
    def __init__(self, edge):
        self.name = 'REMOVE'
        self.edge = edge
        super().__init__(self.name, self.edge)


class Act(object):
    def __init__(self, name, content, agent='X'):
        self.name = name
        self.content = content
        self.agent = agent

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '{}_{}({})'.format(self.name, self.agent, self.content)

    def __hash__(self):
        return hash((self.name, self.content, self.agent))

    def __eq__(self, other):
        if isinstance(other, Act):
            return self.name == other.name \
                and self.content == other.content \
                and self.agent == other.agent


class Instruction(Act):
    def __init__(self, action, agent='X'):
        self.name = 'INSTRUCT'
        self.action = action
        self.agent = agent
        super().__init__('{}'.format(self.name), action, agent)


class Do(Act):
    def __init__(self, action, agent='X'):
        self.name = 'DO'
        self.action = action
        self.agent = agent
        super().__init__('{}'.format(self.name), action, agent)


class Match(Act):
    def __init__(self, instruct_act, agent='X'):
        self.name = 'MATCH'
        self.instruct_act = instruct_act
        super().__init__('{}'.format(self.name), instruct_act, agent)


class Mismatch(Act):
    def __init__(self, instruct_act, agent='X'):
        self.name = 'MISMATCH'
        self.instruct_act = instruct_act
        super().__init__('{}'.format(self.name), instruct_act, agent)


class Nonmatch(Act):
    def __init__(self, action, agent='X'):
        self.name = 'NONMATCH'
        self.action = action
        self.agent = agent
        super().__init__('{}'.format(self.name), action, agent)


def make_edit_action(action_name, action_edge):
    action = None
    u, v = action_edge
    edge = Edge(u, v)
    if action_name == 'ADD':
        action = AddAction(edge)
    elif action_name == 'REMOVE':
        action = RemoveAction(edge)
    return action
