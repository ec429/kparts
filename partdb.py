#!/usr/bin/python

import kpart
import engines
import ion_engines

if __name__ == '__main__':
    # Just here for testing.  We'll do something more useful with the data later.
    for part in kpart.AllParts:
        print '\t%s' % (part,)
    print '%d parts' % (len(kpart.AllParts),)
