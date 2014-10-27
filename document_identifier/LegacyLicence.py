import re
from . import DocumentBase

"""
Taken from http://adr-inc.com/PDFs/State_DLFormats.pdf
"""


class LegacyLicence(DocumentBase):
    pass


class LegacyAlaskaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{1,7})$'),
    }


class LegacyAlabamaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{1,7})$'),
    }


class LegacyArizonaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{1,8}|[A-Z]{2}\d{2,5}|\d{9})$'),
    }


class LegacyArkansasLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{4,9})$'),
    }


class LegacyCaliforniaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{7})$'),
    }


class LegacyColoradoLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>(\d{7}|[A-Z][A-Z0-9]\d{0,3})\d{2})$'),
    }


class LegacyConnecticutLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{9})$'),
    }


class LegacyDelawareLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{1,7})$'),
    }


class LegacyDistrictOfColumbiaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>([A-Z]{2}\d|\d\d)?\d{7})$'),
    }

class LegacyFloridaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{12})$'),
    }


class LegacyGeorgiaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{7,9})$'),
    }


class LegacyHawaiiLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z0-9]\d{8})$'),
    }


class LegacyIdahoLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]{2}\d{6}[A-Z]|\d{9})$'),
    }


class LegacyIllinoisLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{11,12})$'),
    }


class LegacyIndianaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z0-9]?\d{9})$'),
    }


class LegacyIowaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{3}[A-Z0-9]{2}\d{4})$'),
    }


class LegacyKansasvLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>(([A-Z]\d){2}[A-Z]|[A-Z0-9]\d{8}))$'),
    }


class LegacyKentuckyLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z0-9]\d{8}\d?)$'),
    }


class LegacyLouisianaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{1,9})$'),
    }


class LegacyMaineLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{7}[A-Z0-9]?)$'),
    }


class LegacyMarylandLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{12})$'),
    }


class LegacyMassachusettsLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z0-9]\d{8})$'),
    }


class LegacyMichiganLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{10}(\d{2})?)$'),
    }


class LegacyMinnesotaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{12})$'),
    }


class LegacyMississippiLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{9})$'),
    }


class LegacyMissouriLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{5,9}|[A-Z]\d{6}R|\d{8}([A-Z0-9][A-Z]|\d)?)$'),
    }


class LegacyMontanaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z0-9]\d{8}|\d{13}\d?)$'),
    }


class LegacyNebraskaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{1,7})$'),
    }


class LegacyNevadaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>(X|\d)\d{8}|\d{10}(\d\d)?)$'),
    }


class LegacyNewHampshireLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{2}[A-Z]{3}\d{5})$'),
    }


class LegacyNewJerseyLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{14})$'),
    }


class LegacyNewMexicoLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{8,9})$'),
    }


class LegacyNewYorkLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]([A-Z]{7}|\d{7}(\d{11})?)|\d{8,9}(\d{7})?)$'),
    }


class LegacyNorthCarolinaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{1,12})$'),
    }


class LegacyNorthDakotaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>([A-Z]{3}|\d{3})\d{6})$'),
    }


class LegacyOhioLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z][A-Z0-9]\d{3,7}|\d{8})$'),
    }


class LegacyOklahomaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]?\d{9})$'),
    }


class LegacyOregonlinaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{1,9})$'),
    }


class LegacyPennsylvaniaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{8})$'),
    }


class LegacyRhodeIslandLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z0-9]\d{6})$'),
    }


class LegacySouthCarolinaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{5,11})$'),
    }


class LegacySouthDakotaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{6,10}|\d{12})$'),
    }


class LegacyTennesseeLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{7,9})$'),
    }


class LegacyTexasLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{7,8})$'),
    }


class LegacyUtahLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{4,10})$'),
    }


class LegacyVermontLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{7}[A0-9])$'),
    }


class LegacyVirginiaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{9,11}|\d{9})$'),
    }


class LegacyWashingtonLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z0-9\*]{12})$'),
    }


class LegacyWestVirginiaLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]{1,2}\d{5,6}|\d{7})$'),
    }


class LegacyWisconsinLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>[A-Z]\d{13})$'),
    }


class LegacyWyomingLicence(LegacyLicence):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{9,10})$'),
    }


__all__ = [cls.__name__ for cls in LegacyLicence.__subclasses__()]