
import json
from os import path
class FileDict(dict):
    def __init__(self , filename):
        self.filename = filename
        if path.exists( self.filename + '.json'):
            with open(self.filename + '.json', 'r') as f:
                self.__dict__ = json.load(f)
        else:
            with open(self.filename + '.json', 'w') as f:
                json.dump(self.__dict__, f)

    def __setitem__(self, key, item):
        self.__dict__[key] = item


    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def __del__(self):
        with open(self.filename + '.json', 'w') as f:
            json.dump(self.__dict__, f)

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))


