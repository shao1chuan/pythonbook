import re

line = 'asdf fjdk;   afed,  fjek,asdf,   foo'

print(re.split(r'[;,\s]\s*', line))
# 正则模式表示 ;或,或空白字符且它们的后面再跟0个或多个空白字符
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

