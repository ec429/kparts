#!/usr/bin/python

import kpart
import engines
import ion_engines

def make_tree_engines():
    mecs = '\n\n'.join(config.make_tree() for config in kpart.AllConfigs)
    ups = '\n'.join(config.make_upgrade() for config in kpart.AllConfigs if config.upgrade)
    return """/* This file is auto-generated from kparts, do not edit directly.
 * Instead, edit the master files and rerun the scripts to regenerate it.
 */

@PART[*]:HAS[@MODULE[ModuleEngineConfigs]]:BEFORE[RealismOverhaulEnginesPost]
{
	@MODULE[ModuleEngineConfigs],*
	{
%s
	}
}

/* Part Upgrades begin here */

%s
""" % (mecs, ups)

if __name__ == '__main__':
    # Just here for testing.  We'll do something more useful with the data later.
    for part in kpart.AllParts:
        print '\t%s' % (part,)
    print '%d parts' % (len(kpart.AllParts),)
    for config in kpart.AllConfigs:
        print '\t%s' % (config,)
    print '%d configs' % (len(kpart.AllConfigs),)
    print make_tree_engines()
