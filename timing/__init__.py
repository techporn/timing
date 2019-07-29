from .diagram import Diagram
from .parser import TimingParser, read_timing

__version__ = '0.1.0'

# test
# data = read_timing("./test_chart")
# d = Diagram()
# for i in data:
#     print(i)
#     d.add_timing(*i)

# d.plot()