from __future__ import annotations


class Quantity:
    def __init__(self, value):
        self.value = value

    def __call__(self, *args, **kwargs):
        return self.value

    def __repr__(self):
        return str(self.value)
