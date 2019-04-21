import os
import re


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


print(find('03-D and F Block E-2.tex', '.'))


text_to_search = '''

543.\includegraphics[width=91pt]{img-2.eps} In the figure, a vector x satisfies
the equation \({\bf{x}} - {\bf{w}} = {\bf{v}}\). Then x =

(a)\(2{\bf{a}} + {\bf{b}} + {\bf{c}}\)(b)\({\bf{a}} + 2{\bf{b}} + {\bf{c}}\)

(c)\({\bf{a}} + {\bf{b}} + 2{\bf{c}}\)(d)\({\bf{a}} + {\bf{b}} + {\bf{c}}\)

'''
position_hits = []
pattern = re.compile('\\\includegraphics.+\{.+\}')
matches = pattern.finditer(text_to_search)
for match in matches:
    position_hits.append(match.span())


x = text_to_search.split("{")

print(x[1].replace('}', ''))
