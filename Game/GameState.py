#  Copyright (c) 2022
#
#  MIT License
#
#  Copyright (c) 2022 Sacha
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

num = [1,2,3,4,5,6,7,8,9]

status1 = """
+---+
|   |
|
|
|
|
=========
"""

status2 = """
+---+
|   |
|   O
|
|
|
=========
"""

status3 = """
+---+
|   |
|   O
|   |
|
|
=========
"""

status4 = """
+---+
|   |
|  \O
|   |
|
|
========
"""

status5 = """
+---+
|   |
|  \O/
|   |
|
|
========
"""

status6 = """
+---+
|   |
|  \O/
|   |
|  /
|
=========
"""

status7 = """
+---+
|   |
|  \O/
|   |
|  / \\
|
=========
I will survive!
"""

status8 = """
+---+
|   |
|   |o
|  /|\\
|   ||
|
=========
...
"""

status9 = """
+---+
|   |
|
|   O
|  \|/
|  / \\
=========
phewwww!
"""

def status(num:int):
    """
    :param num: status
    :return: Returns the ascii code related to the number variable
    """
    if num == 1:
        return status1
    elif num == 2:
        return status2
    elif num == 3:
        return status3
    elif num == 4:
        return status4
    elif num == 5:
        return status5
    elif num == 6:
        return status6
    elif num == 7:
        return status7
    elif num == 8:
        return status8
    elif num == 9:
        return status9
    else:
        raise Exception("Error : The number is invalid !")