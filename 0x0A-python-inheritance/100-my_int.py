#!/usr/bin/python3
# 100-my_int.py
"""actually it is defining  a class MyInt that inherits from int."""


class MyInt(int):
    """operators == and != are inverted."""
    def __eq__(self, value):
        """Overriding == operator with != behavuior."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Overriding != operator with == behavior."""
        return self.real == value
