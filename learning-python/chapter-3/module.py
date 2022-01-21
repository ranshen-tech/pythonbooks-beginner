import myfile
print(myfile.title)

from myfile import title
print(title)

import threenames
print(threenames.a)
print(threenames.b, threenames.c)

from threenames import a, b, c
print(a)
print(b, c)

print(dir(threenames))