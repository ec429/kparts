#!/usr/bin/python

import kpart
import engines
import ion_engines

autogen_warning = """\
/* This file is auto-generated from kparts, do not edit directly.
 * Instead, edit the master files and rerun the scripts to regenerate it.
 */
"""

def make_tree_engines():
    mecs = '\n\n'.join(config.make_tree() for config in kpart.AllConfigs)
    ups = '\n'.join(config.make_upgrade() for config in kpart.AllConfigs if config.upgrade)
    return autogen_warning + """
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

def make_ecm_engines():
    ecms = '\n'.join(config.make_ecm() for config in kpart.AllConfigs)
    return autogen_warning + """
//******************************************************************************
//  ENTRY COST MODIFIERS
//	These are the engine configs
//******************************************************************************
@ENTRYCOSTMODS:FOR[xxxRP-0]
{
%s
}
""" % (ecms,)

def make_tree_parts():
    parts = '\n'.join(part.make_tree() for part in kpart.AllParts)
    return "%s\n%s\n" % (autogen_warning, parts)

def make_identical_parts():
    iparts = '\n'.join(part.make_identical() for part in kpart.AllParts if part.identical_parts or part.identical_to)
    return "%s\n%s\n" % (autogen_warning, iparts)

if __name__ == '__main__':
    # Just here for testing.  We'll do something more useful with the data later.
    print make_tree_parts()
    print make_tree_engines()
    print make_ecm_engines()
    print make_identical_parts()
