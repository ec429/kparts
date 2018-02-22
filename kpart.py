#!/usr/bin/python

class KMod(object):
    def __init__(self, name):
        self.name = name
        self.parts = []
    def __str__(self):
        return self.name

class KTag(object):
    def __init__(self, name):
        self.name = name
        self.parts = []
    def __str__(self):
        return self.name

class KTech(object):
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def __str__(self):
        return self.name

unlockParts = KTech("unlockParts", 0)

class KCat(object):
    def __init__(self, name):
        self.name = name
        self.parts = []
        self.techs = {0: unlockParts}
    def add_tech(self, tech):
        if tech.year in self.techs:
            raise Exception("Two techs in year", tech.year, "for category", self, self.techs[tech.year], tech)
        self.techs[tech.year] = tech
    def tech(self, year):
        k = max(y for y in self.techs.keys() if y <= year)
        return self.techs[k]
    def __str__(self):
        return self.name

class IsConf(object):
    def __init__(self, ro, rp0, costed):
        self.ro = ro
        self.rp0 = rp0
        self.costed = costed
    def __str__(self):
        return 'RO:%s, RP-0:%s, costed:%s' % (self.ro, self.rp0, self.costed)

NoConf = IsConf(False, False, False)
ROConf = IsConf(True, False, False)
RP0NoCost = IsConf(True, True, False)
RP0Conf = IsConf(True, True, True)

class EngineConfig(object):
    def __init__(self, name, cost, entry_cost, year=0, category=None, description=None):
        self.name = name
        self.cost = cost
        self.entry_cost = entry_cost
        self.year = year
        self.category = category
        self.description = description
    @property
    def tech(self):
        if self.category:
            return self.category.tech(self.year)
        return unlockParts
    def __str__(self):
        return self.name

AllParts = [] # Later we can make this a magic object capable of doing indexing for us, but a list will do for now

class KPart(object):
    def __init__(self, name, title, description, cost, entry_cost, mod=None, year=0, category=None, is_conf=NoConf, engine_configs=[], ecms=[], tags=[]):
        self.name = name
        self.title = title
        self.description = description
        self.cost = cost
        self.entry_cost = entry_cost
        self.mod = mod
        if mod:
            mod.parts.append(self)
        self.year = year
        self.category = category
        self.ro = is_conf.ro
        self.rp0 = is_conf.rp0
        self.costed = is_conf.costed
        self.engine_configs = engine_configs
        if engine_configs:
            for i,ec in enumerate(engine_configs):
                ec.upgrade = bool(i)
        self.upgrades = []
        self.ecms = ecms
        self.tags = tags
        for tag in tags:
            tag.parts.append(self)
        self.identical_to = None
        self.identical_parts = []
        AllParts.append(self)
    def clone(self, name, **kwargs):
        not_identical = kwargs.pop('not_identical', False)
        k = {'title': self.title,
             'description': self.description,
             'cost': self.cost,
             'entry_cost': self.entry_cost,
             'mod': self.mod,
             'year': self.year,
             'category': self.category,
             'is_conf': IsConf(self.ro, self.rp0, self.costed),
             }
        k.update(kwargs)
        new = self.__class__(name, **k)
        if not not_identical:
            new.identical_to = self
            self.identical_parts.append(new)
        return new
    @property
    def tech(self):
        if self.category:
            return self.category.tech(self.year)
        return unlockParts
    def __str__(self):
        return self.name
