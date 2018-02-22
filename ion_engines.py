#!/usr/bin/python

from kpart import *

Ion = KCat("Ion")
NFP = KMod("Near Future Propulsion")
## Declare techs for category
Ion.add_tech(KTech("earlyElecPropulsion",       1998))
Ion.add_tech(KTech("basicElecPropulsion",       2009))
Ion.add_tech(KTech("improvedElecPropulsion",    2019))
Ion.add_tech(KTech("advancedElecPropulsion",    2035))
Ion.add_tech(KTech("colonization2051ElecProp",  2051))
Ion.add_tech(KTech("colonization2100ElecProp",  2100))
Ion.add_tech(KTech("colonization2150ElecProp",  2150))

## Parts begin here

# This is basically a macro we use to create several similar parts
def NFP_Ion_Engine(name, year):
    # We have no descriptions, costs, or entryCosts for these (presumably they come from NF configs too)
    return KPart(name, "(stored in NearFuture Configs)", None, None, None,
                 mod=NFP, year=year, category=Ion)

NASA_457M_V1    = NFP_Ion_Engine("NASA-457M-V1",    2000)
NASA_457M_V1_X4 = NFP_Ion_Engine("NASA-457M-V1-X4", 2010)
NASA_457M_V2    = NFP_Ion_Engine("NASA-457M-V2",    2014)
NASA_457M_V2_X4 = NFP_Ion_Engine("NASA-457M-V2-X4", 2019)
P5_1            = NFP_Ion_Engine("P5-1",            2014)
P5_2            = NFP_Ion_Engine("P5-2",            2019)
