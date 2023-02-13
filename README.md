# BetterJSONDeserializer
Improved JSON deserializer for Python that allows for remapping to custom object types and nested objects. This allows for saving/loading complex Python objects while still preserving them in a human-readable format.

Example Usage:
``` py
import json

import jObject


class character(jObject.jObject):
    def __init__(self, name="Character", age=0):
        super().__init__()
        self.name = name
        self.age = age

        self.rigs = []

class rig(jObject.jObject):
    def __init__(self, name="Rig"):
        super().__init__()
        self.name = name
        self.modules = {}

class motionModule(jObject.jObject):
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
characterData = json.dumps(char, cls=jObject.jObjectEncoder, indent=4)

# Load the character from JSON
char = json.loads(characterData, object_hook=jObject.loadJObject)


```
