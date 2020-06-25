import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)  # 迭代协议要求__iter__返回一个迭代器


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]  # 获取 self.index 索引位（从0开始）上的单词。
        except IndexError:
            raise StopIteration()  # 如果 self.index 索引位上没有单词，那么抛出 StopIteration 异常
        self.index += 1
        return word

    def __iter__(self):
        return self  # 返回迭代器本身