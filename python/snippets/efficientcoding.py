#https://gist.github.com/0x4D31/f0b633548d8e0cfb66ee3bea6a0deff9:

Loops:
Looping over a range of numbers:
for i in [0, 1, 2, 3, 4, 5]:
    print i**2

for i in range(6):
    print i**2

for i in xrange(6):
    print i**2

Looping over a collection:
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print colors[i]


for color in colors:
    print color


Looping backwards:
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)-1, -1, -1):
    print colors[i]

for color in reversed(colors):
    print color


Looping over a collection and indices:
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print i, '--->', colors[i]

for i, color in enumerate(colors):
    print i, '--->', color

Looping over two collections:

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print names[i], '--->', colors[i]

for name, color in zip(names, colors):
    print name, '--->', color

for name, color in izip(names, colors):
    print name, '--->', color

Looping in sorted order:
colors = ['red', 'green', 'blue', 'yellow']

# Forward sorted order
for color in sorted(colors):
    print colors

# Backwards sorted order
for color in sorted(colors, reverse=True):
    print colors

Custom Sort Order:
print sorted(colors, key=len)



Distinguishing multiple exit points in loops:
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

Looping over dictionary keys:
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in d:
    print k

for k in d.keys():
    if k.startswith('r'):
        del d[k]

Looping over dictionary keys and values:
# Not very fast, has to re-hash every key and do a lookup
for k in d:
    print k, '--->', d[k]

# Makes a big huge list
for k, v in d.items():
    print k, '--->', v

for k, v in d.iteritems():
    print k, '--->', v


