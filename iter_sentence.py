import re
import reprlib

RE_WORD = re.compile('\w+')

# -------v1-------


class Sentence1:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))


# -------v2-------


class Sentence2:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))


class SentenceIterator:
    def __init__(self, words):
        self.index = 0
        self.words = words

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


# -------v3-------


class Sentence3:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))


# -------v4-------

class Sentence4:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        # `finditer` construct a generator
        for match_obj in RE_WORD.finditer(self.text):
            yield match_obj.group()


# -------v5-------

class Sentence5:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        # `finditer` construct a generator
        return (match_obj.group() for match_obj in RE_WORD.finditer(self.text))

if __name__ == '__main__':
    # generate new obj which is iterable
    s = Sentence5('I have a dream.')

    # generate a iterator on iterable obj
    # first call `__iter__` method if the obj has this method which return the iterator itself
    # or create a iterator if the obj has `__getitem__` method
    # otherwise raise TypeError like object is not iterable
    it = iter(s)

    # the standard iterator must have two method: `__next__` and '__iter__'
    # '__iter__' return the iterator itself
    # '__next__' return next item or raise StopIteration
    assert hasattr(it, '__next__') is True
    assert hasattr(it, '__iter__') is True

    # the follow code block is the same as `for`
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break

