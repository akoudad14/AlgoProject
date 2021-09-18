

class Keypad:

    keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
              '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}

    @classmethod
    def type_key(cls, key, index_):
        try:
            return cls.keypad[key][index_]
        except KeyError:
            return ''

    @classmethod
    def letter_count(cls, key):
        try:
            return len(cls.keypad[key])
        except KeyError:
            return None


def keypad_string(keys):
    res = ''
    last_key = None
    index_ = 0
    for key in keys:
        if key == last_key:
            if index_ + 1 == Keypad.letter_count(key):
                res += Keypad.type_key(last_key, index_)
                index_ = 0
            else:
                index_ += 1
        elif last_key is not None:
            res += Keypad.type_key(last_key, index_)
            index_ = 0
        last_key = key
    if last_key is not None:
        res += Keypad.type_key(last_key, index_)
    return res
