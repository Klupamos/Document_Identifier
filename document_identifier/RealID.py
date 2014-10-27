import re
import datetime
from . import DocumentBase

__all__ = ["PennsylvaniaLicence", "PensylvaniaAltLicence", "RealID"]


class RealID(DocumentBase):
    Format = {
        'mag_track1': re.compile(r'^%(?P<state>[A-Z]{2})(?P<city>.*)\^(?P<name_parts>.*)\^(?P<street_parts>.*)\^(?P<other>.*)\?'),
        'mag_track2': re.compile(r'^;(?P<issuer_code>[0-9]{6})(?P<number>[0-9]{8})=(?P<expiration>[0-9]{4})(?P<birthday>[0-9]{8})=\?'),
    }
    
    def __init__(self, **kwargs):
        if kwargs.get('raw_input'):
            kwargs['mag_strip'] = kwargs['raw_input']

        if kwargs.get('mag_strip'):
            kwargs.update({
                'mag_track1': kwargs['mag_strip'][7:116],
                'mag_track2': kwargs['mag_strip'][117:226],
                })

        super(RealID, self).__init__(**kwargs)

        self.name_parts = self.name_parts.split('$')
        self.street_parts = self.street_parts.split('$')

        self.birthday = datetime.datetime.strptime(self.birthday, "%Y%m%d").date()
        self.expiration = datetime.datetime.strptime(self.expiration, "%y%m").date()
    
    def __str__(self):
        parent = super(RealID, self).__str__() + "\n"
        child = "Expires: {0.expiration}\n"
        child += "{0.name} ({0.age}) {0.birthday:%A, %B %d, %Y}\n"
        child += "{0.street_address}"
        
        return parent + '\t'+'\n\t'.join(child.format(self).split('\n'))
    
    @property
    def name(self):
        if len(self.name_parts) > 2:
            return " ".join([self.name_parts[1], " ".join(self.name_parts[2:]), self.name_parts[0]])
        else:
            return " ".join([self.name_parts[1], self.name_parts[0]])

    @property
    def street_address(self):
        s = self.street_parts[0] + "\n"
        if self.street_parts[1]:
            s += self.street_parts[1] +"\n"
        s += "{0.city} {0.state}".format(self)
        return s

    @property
    def age(self):
        born = self.birthday
        today = datetime.date.today()
        try:
            birthday = born.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = born.replace(year=today.year, month=born.month+1, day=1)
            
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year


class PennsylvaniaLicence(RealID):
    def __init__(self, **kwargs):
        super(PennsylvaniaLicence, self).__init__(**kwargs)

        if self.state != 'PA':
            raise ValueError('Invalid state')


class PensylvaniaAltLicence(PennsylvaniaLicence):
    Format = {
        'mag_track1': re.compile(r'^%(?P<state>[A-Z]{2})(?P<city>.*) (?P<name_parts>.*)\^(?P<street_parts>.*)\^(?P<other>.*)\?'),
        'mag_track2': re.compile(r'^;(?P<issuer_code>[0-9]{6})(?P<number>[0-9]{8})=(?P<expiration>[0-9]{4})(?P<birthday>[0-9]{8})=\?'),
    }
    
    @property
    def name(self):
        if len(self.name_parts) > 2:
            return " ".join([self.name_parts[0], self.name_parts[1], self.name_parts[2]])
        else:
            return " ".join([self.name_parts[0], self.name_parts[2]])