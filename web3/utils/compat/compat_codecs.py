
import codecs
import sys


def backslashreplace(ex):
    # The error handler receives the UnicodeDecodeError, which contains arguments of the
    # string and start/end indexes of the bad portion.
    bstr, start, end = ex.args[1:4]

    # The return value is a tuple of Unicode string and the index to continue conversion.
    # Note: iterating byte strings returns int on 3.x but str on 2.x
    return (
        u''.join(
            '\\x{:02x}'.format(c if isinstance(c, int) else ord(c))
            for c in bstr[start:end]
        ),
        end,
    )


def setup_backslashreplace():
    if sys.version_info[:2] < (3, 5):
        codecs.register_error('backslashreplace', backslashreplace)
