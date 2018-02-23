#!/usr/bin/python

from kpart import *

# These will probably need to live in a central file of their own & be imported into these parts files
BDB              = KMod("Bluedog DB")
FASA             = KMod("FASA")
RealEngines      = KMod("RealEngines")
RO_Extended      = KMod("RO-Extended")
StockRO          = KMod("Stock (RO Config)")
SSTU_RO_Addition = KMod("SSTU (RO Addition)")
SXT              = KMod("SXT")
Taerobee         = KMod("Taerobee")
VSR              = KMod("Ven Stock Revamp")

# The same might go for these tags
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

# A-6/Redstone
A6Config = EngineConfig("A-6", 0, (3000, 'Navaho-PhaseIII-TP'), year=1952, category=Orbital, description="The production version of the NAA75-110 engine as used on Redstone and the Mercury-Redstone Launch Vehicle.")
A7Config = EngineConfig("A-7", 200, (5000, 'HydyneFuel'), year=1956, category=Orbital, description="NAA75-110 using Hydyne fuel for increased thrust and specific impulse. Used on the Redstone-derivative Jupiter-C sounding rocket and Juno I launch vehicle.")
bluedog_redstone = KPart("bluedog_redstone", "NAA-75-110 A-Series", "Used on the Redstone missile.  Designed for Ethanol/LOx (A-6) (1.5 O/F Ratio), it was later adapted to burn Hydyne/LOx (A-7) (1.73 O/F Ratio)(higher performance (12%) yet more toxic) for use in Jupiter C / Juno I.  When Redstone MRLV was adapted from Jupiter C for manned use the A7 was switched back to Ethanol, accepting slightly lower performance for lack of toxicity. Thrust Vector Control was provided by carbon thrust vanes (add the Redstone Fin / Thrust vane part in 4x symmetry), and additional attitude control was provided by actuating fins. Mass includes thrust frame. Diameter: [1.77 m]. Plume configured by RealPlume.",
                400, 16000,
                mod=BDB, year=1952, category=Orbital,
                is_conf=RP0Conf, engine_configs=[A6Config, A7Config],
                ecms=['A-6'], tags=[LqdTurbo])
FASA_Mercury_Redstone_Eng = bluedog_redstone.clone("FASA_Mercury_Redstone_Eng", mod=FASA, year=1955)
# not an engine, but still in class Orbital for some reason
FASAMercuryRedstoneFin = KPart("FASAMercuryRedstoneFin", "A-7 Fin / Thrust Vane", "The Redstone / Jupiter-C / Juno engine could not gimbal.  Instead TVC was obtained by use of carbon thrust vanes. Apply in 4x symmetry to A7 engine unit.",
                5, 100,
                mod=FASA, year=1955, category=Orbital, is_conf=RP0Conf)

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
AJ10_118 = EngineConfig("AJ10-118", -30, (1000, 'AJ10-142'), year=1962, category=Orbital, description="Used on Delta A")
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

# RD-100 series
RD100Config = EngineConfig("RD-100", 0, 0, year=0, category=Orbital)
RD102 = EngineConfig("RD-102", 120, (10000, 'RD102-TP'), year=1950, category=Orbital)
RD103 = EngineConfig("RD-103", 300, (7000, 'RD-102', 'RD-103TP'), year=1952, category=Orbital)
RD103M = EngineConfig("RD-103M", 350, (5000, 'RD-103'), year=1956, category=Orbital)
rd100 = KPart("rd100", "RD-100 Series (Early)", "The RD-100 engine series were the first large scale Ethalox Russian liquid propellant rocket engines ever developed and fired. The original RD-100 engine was a 1:1 copy of the German Model 39 engine (used on the A-4 ballistic missile), with later variants (RD-101 and RD-103/M) featuring ever increasing performance to satisfy the needs of the larger R-2 and R-5 IRBMs. Diameter: 1.65 m. Plume configured by RealPlume.",
                150, 1,
                mod=RealEngines, year=0, category=Orbital,
                is_conf=RP0Conf, engine_configs=[RD100Config, RD102, RD103, RD103M],
                ecms=['RD-100'], tags=[LqdTurbo])
LVT15 = rd100.clone("LVT15", mod=VSR)
