import json

import j_classify


class character(j_classify.j_object):
    def __init__(self, name="Character", age=0):
        super().__init__()
        self.name = name
        self.age = age

        self.rigs = []


class rig(j_classify.j_object):
    def __init__(self, name="Rig"):
        super().__init__()
        self.name = name
        self.modules = {}


class motionModule(j_classify.j_object):
    def __init__(self, name="Module"):
        super().__init__()
        self.name = name
        self.joints = []
        self.something = "something"


if __name__ == "__main__":
    # Create a character
    char = character("John", 25)
    # Create a rig
    r = rig("Rig1")
    # Create a module
    mm = motionModule("Module1")
    # Add the module to the rig
    r.modules[mm.name] = motionModule
    # Add the rig to the character
    char.rigs.append(r)

    # Dump the character to JSON
    characterData = json.dumps(char, cls=j_classify.j_object_encoder, indent=4)
    print(characterData)

    # Load the character from JSON
    loaded_char = json.loads(characterData, object_hook=j_classify.load_j_object)
    print(type(loaded_char))
    print(type(loaded_char.rigs[0]))
