'''
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

    Python: return a list;
    JavaScript: returns an Array;
    C#: returns a string[];
    PHP: returns an array;
    C++: returns a vector<string>;
    Haskell: returns a [String];

Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]

and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]

Build_Tower_Advanced is a more complex version
'''

def tower_builder(n_floors):
    tower = []
    for i, j in enumerate(range(n_floors), start=1):
        if j == 0:
            tower.append(" "*int(n_floors-i) + "*"*i + " "*int(n_floors-i))
        else:
            i += j
            tower.append(" "*int(n_floors-(j+1)) + "*"*i + " "*int(n_floors-(j+1)))
    return tower