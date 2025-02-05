import sys

PY3 = sys.version_info[0] == 3

string_types = str
int_types = (int,)
izip = zip
imap = map
long = int
unicode = str
iteritems = dict.items
xrange = range


def with_metaclass(mcls):
    def decorator(cls):
        body = vars(cls).copy()
        # clean out class body
        body.pop('__dict__', None)
        body.pop('__weakref__', None)
        return mcls(cls.__name__, cls.__bases__, body)
    return decorator
