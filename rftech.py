#!/usr/bin/python

from kpart import *
import engines

## Category "RCS"

RCS = KCat("RCS")
RCS.add_tech(engines.rocketryTesting)
RCS.add_tech(engines.earlyRocketry)
RCS.add_tech(engines.basicRocketryRP0)
RCS.add_tech(engines.orbitalRocketry1956)
RCS.add_tech(KTech("earlyFlightControl",        1959))
RCS.add_tech(KTech("stabilityRP0",              1961))
RCS.add_tech(KTech("improvedFlightControl",     1963))
RCS.add_tech(KTech("earlyDocking",              1964))
RCS.add_tech(KTech("advancedFlightControl",     1967))
RCS.add_tech(KTech("dockingCrewTransfer",       1968))
RCS.add_tech(KTech("spaceStationControl",       1972))
RCS.add_tech(KTech("largeSpaceplaneControl",    1981))
RCS.add_tech(KTech("standardDockingPorts",      1986))
RCS.add_tech(KTech("largeStationControl",       1998))
RCS.add_tech(KTech("largeDockingPorts",         2004))
RCS.add_tech(KTech("gridFins",                  2009))
RCS.add_tech(KTech("flightControlNF",           2019))
RCS.add_tech(KTech("colonization2051Control",   2051))
RCS.add_tech(KTech("colonization2100Control",   2100))
RCS.add_tech(KTech("colonization2150Control",    2150))

RCSTech = RFTechFamily('rcs', RCS, 'L*', 'RCS', icon='RCSBlock', desc='RCS Thrusters and Engines')
RFTechLevel(0,    0, RCSTech)
RFTechLevel(1, 1959, RCSTech)
RFTechLevel(2, 1963, RCSTech)
RFTechLevel(3, 1967, RCSTech)
RFTechLevel(4, 1972, RCSTech)
RFTechLevel(5, 1981, RCSTech)
RFTechLevel(6, 1990, RCSTech)
RFTechLevel(7, 2009, RCSTech)

## Category "Solids"

Solids = KCat("Solids")
Solids.add_tech(engines.rocketryTesting)
Solids.add_tech(KTech("earlySolids", 1950))
for year in [1956, 1958, 1959, 1962, 1964, 1966, 1967, 1969, 1972, 1976, 1981, 1986, 1992, 1998, 2009]:
    Solids.add_tech(KTech("solids%d"%(year,), year))
Solids.add_tech(KTech("solidsNF", 2019))
for year in [2051, 2100, 2150]:
    Solids.add_tech(KTech("colonization%dSolid" % (year,), year))

SolidsTech = RFTechFamily('solids', Solids, 'S*', 'Solid Engine', icon='solidBooster', desc='Solid Engines')
RFTechLevel(0, 1958, SolidsTech)
RFTechLevel(1, 1962, SolidsTech)
RFTechLevel(2, 1964, SolidsTech)
RFTechLevel(3, 1967, SolidsTech)
RFTechLevel(4, 1972, SolidsTech)
RFTechLevel(5, 1981, SolidsTech)
RFTechLevel(6, 1986, SolidsTech)
RFTechLevel(7, 1998, SolidsTech)

## TODO Category "NTR"
