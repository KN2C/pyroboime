from collections import defaultdict


class keydefaultdict(defaultdict):
    """keydefaultdict(default_factory) --> dict with default factory

    The default factory is called with the key as the only argument
    to produce a new value when a key is not present, in
    __getitem__ only. A keydefaultdict compares equal to a dict 
    with the same items.
    """
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            val = self[key] = self.default_factory(key)
            return val
