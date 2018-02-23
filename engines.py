#!/usr/bin/python

from kpart import *

# These will probably need to live in a central file of their own & be imported into these parts files
BDB              = KMod("Bluedog DB")
FASA             = KMod("FASA")
RealEngines      = KMod("RealEngines")
RNUSRockets      = KMod("RN US Rockets")
RO_Extended      = KMod("RO-Extended")
RSB              = KMod("Real Scale Boosters")
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

# Gamma family (British HTP/kero, Black Arrow)
Gamma2Config = EngineConfig("Gamma-2", 0, (4000, 'GammaTP'), year=1956, category=Orbital)
SXTBlackAdder2 = KPart("SXTBlackAdder2", "Gamma 2", "A two chamber version of Gamma, used for the second stage of the Black Arrow satellite launch vehicle. As the only Gamma not required to operate at sea level, the nozzles were extended to allow better expansion. Diameter: [1.37 m]. Plume configured by RealPlume.",
                250, 4000,
                mod=SXT, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[Gamma2Config],
                ecms=['Gamma-2'], tags=[LqdTurbo])
Gamma8Config = EngineConfig("Gamma-8", 0, (5000, 'GammaTP'), year=1956, category=Orbital)
SXTBlackAdder = KPart("SXTBlackAdder", "Gamma 8", "This was an 8 chamber development of Gamma, used for the first stage of the Black Arrow satellite launch vehicle. Gamma thrust chambers were mounted in pairs radially, each pair on a one-axis tangential gimbal. Collective movement gave roll control, differential movement pitch. Diameter: [1.98 m]. Plume configured by RealPlume.",
                300, 10000,
                mod=SXT, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[Gamma8Config],
                ecms=['Gamma-8'], tags=[LqdTurbo])

# LR79 (Thor)
S3Config = EngineConfig("S-3", 0, (10000, 'Navaho-TP'), year=1956, category=Orbital, description="Development version of the LR79 engine. Used on Thor R&D missiles.")
FASADeltaMB3LFE = KPart("FASADeltaMB3LFE", "LR79 Series", "Long-lasting US Kerolox gas-generator booster engine. The same components and broadly the same performance as the LR89, the LR79 (also known as S-3D in Jupiter / Juno II) powered Jupiter, Thor, and Thor-Delta (Delta) rockets. Diameter: [1.53 m]. Plume configured by RealPlume.",
                300, 13000,
                mod=FASA, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[S3Config],
                ecms=['S-3'], tags=[LqdTurbo])
liquidEngine1_2 = FASADeltaMB3LFE.clone("liquidEngine1-2", mod=StockRO)
bluedog_Juno_EngineS3D = FASADeltaMB3LFE.clone("bluedog_Juno_EngineS3D", title="S-3D Liquid Engine", mod=BDB)
bluedog_thorEngine = FASADeltaMB3LFE.clone("bluedog_thorEngine", title="Thor/Delta LR-79", mod=BDB)
SHIP_LR_71 = FASADeltaMB3LFE.clone("SHIP_LR_71", title="LR-79 Series", description="Engine used in a variety of launch vehicles, most notibly the Thor/Delta", mod=RO_Extended, year=1957)
rn_lr79 = FASADeltaMB3LFE.clone("rn_lr79", title="LR79/MB-3 Rocket Engine", description="A Lox/Kerosene rocket engine used on Thor-Able and early Delta launch vehicles. Plume configured by RealPlume.", mod=RNUSRockets, year=1958, engine_configs=[], ecms=['S-3D'])
rn_s3 = rn_lr79.clone("rn_s3", title="S-3", description="A Lox/Kerosene rocket engine used on Juno II and Saturn A-2. Plume configured by RealPlume.", ecms=[]) # should this have S-3 ecm?

## LR79 Turbopump Exhaust.
rn_lr79_tp = KPart("rn_lr79_tp", "LR79/MB-3 Turbopump Exhaust Nozzle", "Turbopump exhaust for the Thor-Able/Delta launch vehicles. Plume configured by RealPlume.",
                5, 1000,
                mod=RNUSRockets, year=1958, category=Orbital,
                is_conf=RP0Conf,
                ecms=['S-3D'], tags=[LqdTurbo])
rn_s3_vernier = rn_lr79_tp.clone("rn_s3_vernier", title="S-3 Turbopump Exhaust Nozzle", description="A Lox/Kerosene vernier rocket engine used on the S-3 engine for Juno II and Saturn A-2. Plume configured by RealPlume.", cost=50, ecms=[]) # should this have S-3 ecm?

# LR89 (Atlas booster)
LR43NA3 = EngineConfig("LR43-NA-3", 0, (12000, 'Navaho-TP'), year=1956, category=Orbital, description="First version of the LR89 booster for Atlas.")
bluedog_Atlas_LR89 = KPart("bluedog_Atlas_LR89", "LR89 Series", "Kerolox gas-generator engine that served as booster for Atlas. Late model LR89s were upgraded with RS-27 components for higher efficiency. Very similar to LR79 (this was the pure-booster variant). Diameter: [1.0 m]. Plume configured by RealPlume.",
                300, 6000,
                mod=BDB, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[LR43NA3],
                ecms=['LR43-NA-3'], tags=[LqdTurbo])
FASAMercuryAtlasEngBooster = bluedog_Atlas_LR89.clone("FASAMercuryAtlasEngBooster", mod=FASA)
RO_LR_89 = bluedog_Atlas_LR89.clone("RO-LR-89", mod=StockRO)

# LR101 (Atlas/Thor vernier)
LR101NA3 = EngineConfig("LR101-NA-3", 0, (8000, 'Navaho-PhaseIII-TP'), year=1956, category=Orbital)
bluedog_Atlas_LR101_Radial = KPart("bluedog_Atlas_LR101_Radial", "LR101 Series", "Pump or pressure-fed kerolox vernier engine. Used for attitude control and final velocity adjustment in the MA-x system (2x LR89 + LR105 + 2x LR101) on Atlas, and MB-x system (LR79 or RS-27 + 2xLR101) on Thor-Able / Thor-Agena / Thor-Delta / Delta. Plume configured by RealPlume.",
                15, 1000,
                mod=BDB, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[LR101NA3],
                ecms=['LR101-NA-3'], tags=[LqdTurbo])
FASAMercuryAtlasVernierEngine = bluedog_Atlas_LR101_Radial.clone("FASAMercuryAtlasVernierEngine", mod=FASA)
RSBengineLR101 = bluedog_Atlas_LR101_Radial.clone("RSBengineLR101", mod=RSB)
radialEngineMini = bluedog_Atlas_LR101_Radial.clone("radialEngineMini", mod=StockRO)
rn_lr79_vernier = bluedog_Atlas_LR101_Radial.clone("rn_lr79_vernier", title="LR101 Thor Vernier", description="Pump or pressure-fed kerolox vernier engine. Used for attitude control and final velocity adjustment in the MB-x system (LR79 or RS-27 + 2xLR101) on Thor-Able / Thor-Agena / Thor-Delta / Delta. Plume configured by RealPlume.", mod=RNUSRockets, year=1958)

# LR105 (Atlas sustainer)
LR43NA5 = EngineConfig("LR43-NA-5", 0, (15000, 'Navaho-TP'), year=1956, category=Orbital, description="First version of the LR105 sustainer for Atlas.")
bluedog_Atlas_LR105 = KPart("bluedog_Atlas_LR105", "LR105 Series", "Kerolox gas-generator sustainer engine used in the Atlas launch vehicle. It, like the Atlas's booster engines (LR89s) are lit on the ground, but after a bit over 2 minutes' flight the boosters are dropped and the Atlas core continues to orbit under the power of the sustainer engine (and the verniers for roll control and final adjustment). The final configuration of the LR105 (like the LR89) uses RS-27 components for increased performance. As a sustainer engine, the LR105 has relatively poor sea level specific impulse compared to most boosters, but somewhat better vacuum specific impulse--though the difference in both is nowhere near as pronounced as when comparing a booster to an upper stage engine. Diameter: [1.5 m]. Plume configured by RealPlume.",
                275, 5500,
                mod=BDB, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[LR43NA5],
                ecms=['LR43-NA-3'], tags=[LqdTurbo])
FASAMercuryAtlasEng = bluedog_Atlas_LR105.clone("FASAMercuryAtlasEng", mod=FASA)
liquidEngine = bluedog_Atlas_LR105.clone("liquidEngine", mod=StockRO)

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
