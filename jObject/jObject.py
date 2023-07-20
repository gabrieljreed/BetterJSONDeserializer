"""A module for jObjects (JSON deserializable objects). This module is used to identify the object type.

Usage:
    json.load(file, object_hook=loadJObject)

Classes:
    jObject (jObject): A base class for all jObjects (JSON deserializable objects). This class is used to identify the
    object type.

Methods:
    loadJObject (function): Return a jObject from a dictionary. Use this method as the object_hook for json.load.
    listAllJObjects (function): Return a dict of the names of all jObject objects and their classes.

    jObjectType (str): The name of the object type.

"""


class jObject:
    """A base class for all jObjects (JSON deserializable objects). This class is used to identify the object type."""

    def __init__(self) -> None:
        """Initialize the object.

        Parameters:
            jObjectType (str): The name of the object type.
        """
        self.jObjectType = type(self).__name__


def loadJObject(d: dict) -> jObject:
    """Return a jObject from a dictionary. Use this method as the object_hook for json.load.

    Args:
        d (dict): The dictionary to load the jObject from.

    Returns:
        jObject: The jObject loaded from the dictionary.

    Usage:
        json.load(file, object_hook=loadJObject)
    """
    objectType = d.get("jObjectType")
    newObject = listAllJObjects().get(objectType)

    if newObject is None:
        return d

    for var in d:
        if var in vars(newObject):
            setattr(newObject, var, d[var])

    return newObject


def listAllJObjects() -> dict:
    """Return a dict of the names of all jObject objects and their classes."""
    classes = {}

    for cls in jObject.__subclasses__():
        classes[cls.__name__] = cls
        for subClass in cls.__subclasses__():
            classes[subClass.__name__] = subClass

    return classes
