#!/usr/bin/python

import kpart
import engines
import ion_engines
import rftech

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
\t@MODULE[ModuleEngineConfigs],*
\t{
%s
\t}
}

/* Part Upgrades begin here */

%s
""" % (mecs, ups)

def make_ecm_engines():
    ecms = '\n'.join(config.make_ecm() for config in kpart.AllConfigs)
    return autogen_warning + """
//******************************************************************************
//\tENTRY COST MODIFIERS
//\tThese are the engine configs
//******************************************************************************
@ENTRYCOSTMODS:FOR[xxxRP-0]
{
%s
}
""" % (ecms,)

def make_ecm_parts():
    ecms = '\n'.join(part.make_ecm() for part in kpart.AllParts if part.ecms)
    return autogen_warning + """
//*****************************************************************************
//\tENTRY COST MODIFIERS
//\tThese are the actual parts with the tags attached
//*****************************************************************************
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

def make_rftech_levels():
    tls = '\n'.join(tl.make_tree() for tl in kpart.AllRFTLs)
    ups = '\n'.join(tl.make_upgrade() for tl in kpart.AllRFTLs)
    return autogen_warning + """
@RFSETTINGS:FOR[RP-0]
{
\t@RF_TECHLEVELS
\t{
%s
\t}
}

%s
""" % (tls, ups)

if __name__ == '__main__':
    # Just here for testing.  We'll do something more useful with the data later.
    print make_tree_parts()
    print make_tree_engines()
    print make_ecm_engines()
    print make_identical_parts()
    print make_ecm_parts()
    print make_rftech_levels()
