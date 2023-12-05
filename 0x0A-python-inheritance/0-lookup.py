#!/usr/bin/python3
def lookup(obj):
	
    """
        Returns a list of attributes and methods of the given object.

        Parameters:
       - obj: The object to inspect.

    Returns:
    - List of attributes and methods.
    """
    return dir(obj)
