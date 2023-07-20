# j_classify

Improved JSON deserializer for Python that allows for remapping to custom object types and nested objects. This allows for saving/loading complex Python objects, like using `pickle` while still preserving them in a human-readable format.

Example Usage:

``` python
import json

import j_classify


class character(j_object.j_object):
    def __init__(self, name="Character", age=0):
        super().__init__()
        self.name = name
        self.age = age

        self.rigs = []

class rig(j_object.j_object):
    def __init__(self, name="Rig"):
        super().__init__()
        self.name = name
        self.modules = {}

class motionModule(j_object.j_object):
    def __init__(self, name="Module"):
        super().__init__()
        self.name = name
        self.joints = []
        self.something = "something"

# Create a character
char = character("John", 25)
# Create a rig
rig = rig("Rig1")
# Create a module
motionModule = motionModule("Module1")
# Add the module to the rig
rig.modules[motionModule.name] = motionModule
# Add the rig to the character
char.rigs.append(rig)

# Dump the character to JSON
characterData = json.dumps(char, cls=j_object.j_object_encoder, indent=4)

# Load the character from JSON
char = json.loads(characterData, object_hook=j_object.load_j_object)
```
