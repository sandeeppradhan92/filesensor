class ObjectFactory(object):

    def __init__(self):
        self._actions = {}

    def register_action(self, key, action):
        self._actions[key] = action

    def register_action_all(self, function_dict):
        for key, value in function_dict.items():
            self._actions[key] = value

    def get_actions(self):
        return self._actions

class ActionFactory:

    def run(self, path, details):
        pass