modules contains definitions and statements
the module's name is available as the value of the global variable __name__
import pythontut
pythontut.fib(100)
from pythontut import fib, fib2
#executin modules as scripts
if __name__ == "__main__":
import sys
fib(int(sys.argv[1]))

