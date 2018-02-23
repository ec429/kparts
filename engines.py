#!/usr/bin/python

from kpart import *

Taerobee         = KMod("Taerobee") # These will probably need to live in a central file of their own & be imported into these parts files
StockRO          = KMod("Stock (RO Config)")
RO_Extended      = KMod("RO-Extended")
SXT              = KMod("SXT")
BDB              = KMod("Bluedog DB")
SSTU_RO_Addition = KMod("SSTU (RO Addition)")

LqdTurbo = KTag("ModuleTagEngineLiquidTurbo")
LqdPF    = KTag("ModuleTagEngineLiquidPF")
Toxic    = KTag("ModuleTagToxic")

### Category "Orbital Rocketry"

Orbital = KCat("Orbital Rocketry")

## Declare techs for category
# These four are also used for category RCS, so we'll want to share them
rocketryTesting     = KTech("rocketryTesting",      1945) # Post War
Orbital.add_tech(rocketryTesting)
earlyRocketry       = KTech("earlyRocketry",        1950)
Orbital.add_tech(earlyRocketry)
basicRocketryRP0    = KTech("basicRocketryRP0",     1952)
Orbital.add_tech(basicRocketryRP0)
orbitalRocketry1956 = KTech("orbitalRocketry1956",  1956)
Orbital.add_tech(orbitalRocketry1956)

for year in [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1970, 1972, 1976, 1981, 1986, 1992, 1998, 2004, 2009, 2014]:
    Orbital.add_tech(KTech("orbitalRocketry%d" % (year,), year))
Orbital.add_tech(KTech("orbitalRocketryNF",         2019))
Orbital.add_tech(KTech("colonization2051Orbital",   2051))
Orbital.add_tech(KTech("colonization2100Orbital",   2100))
Orbital.add_tech(KTech("colonization2150Orbital",   2150))

## Parts for category "Orbital Rocketry" begin here

# A-4
A4Config = EngineConfig("A-4", 0, 1, year=0, category=Orbital)
A9Config = EngineConfig("A-9", 550, (20000, 'HydyneFuel'), year=1945, category=Orbital, description="Derivate of the A-4/V-2 engine for use with the A-9 upper stage / spaceplane. Fuel mixture is speculative.")
Bumper_Engine = KPart("Bumper_Engine", "A-4", "Thiel Lox/Alcohol rocket engine. Used on V-2 missile. Work began June 1936. Interim design, but went into production. Used 18 x 1.5 tonne thrust chambers, feeding common mixing chamber. Tested from 1939, mass production 1943-1945. Diameter: [0.76 m]. Plume configured by RealPlume.",
                150, 1,
                mod=Taerobee, year=0, category=Orbital,
                is_conf=RP0Conf, engine_configs=[A4Config, A9Config],
                ecms=['A-4'], tags=[LqdTurbo])
Bumper_Engine_Unclad = Bumper_Engine.clone("Bumper_Engine_Unclad")

# Aerobee
WAC_Corporal = EngineConfig("WAC-Corporal", 0, 1, year=0, category=Orbital)
XASR1        = EngineConfig("XASR-1", 10, 1000, year=1945, category=Orbital)
AJ10_27      = EngineConfig("AJ10-27", 15, (2000, 'XASR-1'), year=1952, category=Orbital)
ROAerobeeSustainer = KPart("ROAerobeeSustainer", "Aerobee", "Small sustainer for WAC Corporal, Aerobee sounding rockets. Pressure-fed. Used after a small solid booster. Diameter: [0.3 m]. Plume configured by RealPlume.",
                30, 1,
                mod=StockRO, year=0, category=Orbital,
                is_conf=RP0Conf, engine_configs=[WAC_Corporal, XASR1, AJ10_27],
                ecms=['WAC-Corporal'], tags=[LqdPF])
taerobee_aerobee = ROAerobeeSustainer.clone("taerobee_aerobee",
                mod=Taerobee, year=1951)

# AJ10_Early
AJ10_37 = EngineConfig("AJ10-37", 0, (8000, 'AJ10-27'), year=1956, category=Orbital, description="Used on Vanguard second stage.")
AJ10_42 = EngineConfig("AJ10-42", -15, (2000, 'AJ10-37'), year=1958, category=Orbital, description="Used on Able I")
# ... TODO more ...
SXTAJ10 = KPart("SXTAJ10", "AJ10 Series (Early)", "Small pressure-fed hypergolic upper stage engine. Derivative of the first US liquid rocket engine, the AJ10 series is perhaps the longest-lived of any engine series, a part of the US's first satellite launch vehicle, Vanguard, the Apollo CSM, and even one projected Orion service module. This is the original Vanguard second stage / Able / Delta configuration, without restart capability. Plume configured by RealPlume.",
                150, 3000,
                mod=SXT, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[AJ10_37, AJ10_42], # ... TODO more ...
                ecms=['AJ10-37'], tags=[LqdPF, Toxic])
bluedog_ableEngine = SXTAJ10.clone("bluedog_ableEngine", mod=BDB)
SSTU_AJ10_CustomEarly = SXTAJ10.clone("SSTU-AJ10-CustomEarly", mod=SSTU_RO_Addition)

SHIP_AJ_10_101_104 = KPart("SHIP_AJ_10_101_104", "AJ-10 101/104", "Flown on the Able, and AbleStar upper stages. Use the 10-101 with the Able upper stage, and the 10-104 with the AbleStar upper stage.",
                None, None,
                mod=RO_Extended, year=1959, category=Orbital,
                is_conf=ROConf, tags=[LqdPF, Toxic])
