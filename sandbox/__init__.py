import datetime

import ansible


__version__ = '0.1.0'

if ansible.__version__.startswith('1.'):
    print 'ansible 1.x'
else:
    print 'ansible 2.x'
