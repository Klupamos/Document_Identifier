# -*- coding: utf-8 -*-

import re
import datetime
from . import DocumentBase

"""
Parts from http://www.highprogrammer.com/alan/numbers/mrp.html
Parts from http://www.icao.int/publications/Documents/9303_p3_v1_cons_en.pdf
Parts from http://www.icao.int/Security/mrtd/Downloads/Supplements%20to%20Doc%209303/Supplement%20to%20ICAO%20Doc%209303%20-%20Release_14.pdf

ISO Standard 1073-2:1976
"""

"""
While the MRTD Spec (ICAO DOC 9303) get specific length requirements and restricts the characters alLowed in the 'document type' field, I have found many documents (particularly US) do not follow these requirements. To improve the flexibility and usefulness of this module, It will also not follow the above requirements
"""

__all__ = ["Passport", "PassportCard", "Visa", "GreenCard", "PermanentResident"]


class MachineReadableTravelDocument(DocumentBase):
    def __init__(self, **kwargs):
        super(MachineReadableTravelDocument, self).__init__(**kwargs)

        self.number = self.validate_checkdigit(self.raw_number).strip('<')
        self.issuer = self._parse_country_code(self.issuer)
        self.expiration = datetime.datetime.strptime(self.validate_checkdigit(self.raw_expiration), "%y%m%d").date()

        self.name_parts = self.name_parts.split('<<')
        gender_map = {
            'F': "Female",
            'M': "Male",
        }
        self.gender = gender_map.get(self.gender, "Unspecified")
        self.nationality = self._parse_country_code(self.nationality)

        try:
            self.birthday = datetime.datetime.strptime(self.validate_checkdigit(self.raw_birthday), "%y%m%d").date()

            while self.age < 0:
                self.birthday = self.birthday.replace(year=self.birthday.year-100)

        except TypeError:
            self.birthday = None
        
        self.optional = []
        self.optional.append(self.optionalA)
        if hasattr(self, 'optionalB'):
            self.optional.append(self.optionalB)
                    
    @staticmethod
    def _parse_country_code(alpha3):
    
        astrik_map = {
                'D<<': "DEU",
                'GBD': "GBR",
                'GBN': "GBR",
                'GBO': "GBR",
                'GBP': "GBR",
                'GBS': "GBR",
            }
        py_alpha3 = astrik_map.get(alpha3, alpha3)
    
        try:
            import pycountry
        except ImportError:
            return alpha3.strip('<')
            
        try:
            return pycountry.countries.get(alpha3=py_alpha3)
        except KeyError:
            try:
                return pycountry.historic_countries.get(alpha3=py_alpha3)
            except KeyError:
                non_nations_map = {
                    'UNO': " United Nations",
                    'UNA': " United Nations specialized agency",
                    'UNK': " United Nations Interim Administration Mission in Kosovo",
                    'XOM': " Sovereign Military Order of Malta",
                    'XCC': " Caribbean Community",
                    'XXA': " Stateless",
                    'XXB': " Refugee",
                    'XXC': " Refugee",
                    'XXX': " Unspecified",
                    '<<<': " Unspecified",
                }
                return non_nations_map.get(alpha3, alpha3)
        return alpha3
            
    @staticmethod
    def validate_checkdigit(field):

        check_map = {"<": 0}
        check_map.update({str(i): i for i in range(0,10)})
        check_map.update({ch: ord(ch)-55 for ch in "ABCDEFGHIJKLMNOPKRSTUVWXYZ"})
        maped_field = map(check_map.get, field[:-1])
        check = field[-1]
    
        product = 0
        for ch, mul in zip(maped_field, [7,3,1]*len(field)):
            product +=  ch * mul
            
        if product % 10 != int(check):
            raise ValueError("Invalid check digit for sequence '{0}' expected '{1}'".format(field, product % 10))
        return field[:-1]

    @property
    def name(self):
        first_name = self.name_parts[1]
        last_name = self.name_parts[0]
        return ' '.join([first_name.replace('<', ' '), last_name.replace('<', ' ')])

    @property
    def age(self):
        born = self.birthday
        if not born:
            return -1

        today = datetime.date.today()
        try:
            birthday = born.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = born.replace(year=today.year, month=born.month+1, day=1)
            
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    def __str__(self):
        parent = super(MachineReadableTravelDocument, self).__str__()
        
        additional = "({0})\n".format(', '.join(self.optional))
        additional += "{0.name} {0.gender} {0.age} {0.birthday:%A, %B %d, %Y}\n"
        if isinstance(self.nationality, str):
            additional += "Nationality: {0.nationality}\n"
        else:
            additional += "Nationality: {0.nationality.name}\n"
            
        if isinstance(self.issuer, str):
            additional += "Issued by {0.issuer}\n"
        else:
            additional += "Issued by {0.issuer.name}\n"
        additional += "Expires: {0.expiration}\n"
        
        return parent + '\t'+'\n\t'.join(additional.format(self).split('\n'))
        

class td1_MRTD(MachineReadableTravelDocument):
    # Spec defined name to be 30 symbols long, optionalA to be 15 symbols long, and optionalB to be 11 symbols long
    Format = {
        'MRTD_line1': re.compile(r'^(?P<doc_type>[A-Z0-9<]{2})(?P<issuer>[A-Z][A-Z<]{2})(?P<raw_number>[A-Z0-9<]{10})(?P<optionalA>[A-Z0-9<]*)$'),
        'MRTD_line2': re.compile(r'^(?P<raw_birthday>[0-9<]{7})(?P<gender>[MF<])(?P<raw_expiration>\d{7})(?P<nationality>[A-Z][A-Z<]{2})(?P<optionalB>[A-Z0-9<]*)(?P<check_digit>[0-9])$'),
        'MRTD_line3': re.compile(r'^(?P<name_parts>[A-Z0-9<]*)$'),
    }
    
    def __init__(self, **kwargs):
        if kwargs.get('raw_input'):
            kwargs['MRTD'] = kwargs['raw_input']

        if kwargs.get('MRTD'):
            # td1 proper length = 90
            split = len(kwargs['MRTD']) / 3
            kwargs.update({
                'MRTD_line1': kwargs['MRTD'][:split],
                'MRTD_line2': kwargs['MRTD'][split:split*2],
                'MRTD_line3': kwargs['MRTD'][split*2:],
                })

        if 'MRTD_line3' not in kwargs:
            raise ValueError('Missing line3')

        if (len(kwargs['MRTD_line1']) != len(kwargs['MRTD_line2']) or
            len(kwargs['MRTD_line2']) != len(kwargs['MRTD_line3'])):
            raise ValueError('Line length mismatch')

        super(td1_MRTD, self).__init__(**kwargs)

        # Not everone listens to the requirements
        #if self.doc_type[0] not in ['I', 'A', 'C']:
        #    raise ValueError('Wrong document type')
        #if self.doc_type[1] in ['P', 'V']:
        #    raise ValueError('Wrong document subtype')

        self.validate_checkdigit("{0.raw_number}{0.optionalA}{0.raw_birthday}{0.raw_expiration}{0.optionalB}{0.check_digit}".format(self))
        

class CrewMemberCertificate(td1_MRTD):
    def __init__(self, **kwargs):
        super(CrewMemberCertificate, self).__init__(**kwargs)
        if self.doc_type != "AC":
            raise ValueError('Wrong document type')


class PassportCard(td1_MRTD):
    def __init__(self, **kwargs):
        super(PassportCard, self).__init__(**kwargs)
        if self.doc_type != "IP":
            raise ValueError('Wrong document type')


class GreenCard(td1_MRTD):
    def __init__(self, **kwargs):
        super(GreenCard, self).__init__(**kwargs)
        if self.doc_type not in ["C1", "C2"]:
            raise ValueError('Wrong document type')


class td2_MRTD(MachineReadableTravelDocument):
    # Spec defined name to be 31 symbols long and optionalA to be 7 symbols long,
    #  but many documents, including Passports, have a 39 length name and 15 length optionalA
    Format = {
        'MRTD_line1': re.compile(r'^(?P<doc_type>[A-Z0-9<]{2})(?P<issuer>[A-Z][A-Z<]{2})(?P<name_parts>[A-Z0-9<]*)$'),
        'MRTD_line2': re.compile(r'^(?P<raw_number>[A-Z0-9<]{10})(?P<nationality>[A-Z][A-Z<]{2})(?P<raw_birthday>[0-9<]{7})(?P<gender>[MF<])(?P<raw_expiration>\d{7})(?P<optionalA>[A-Z0-9<]*)(?P<check_digit>[0-9])$'),
    }
    
    def __init__(self, **kwargs):
        if kwargs.get('raw_input'):
            kwargs['MRTD'] = kwargs['raw_input']

        if kwargs.get('MRTD'):
            # td2 proper length = 72
            # td2 common length = 88

            split = len(kwargs['MRTD']) / 2
            kwargs.update({
                'MRTD_line1': kwargs['MRTD'][:split],
                'MRTD_line2': kwargs['MRTD'][split:],
                })

        if len(kwargs['MRTD_line1']) != len(kwargs['MRTD_line2']):
            raise ValueError('Line length mismatch')

        super(td2_MRTD, self).__init__(**kwargs)

        self.validate_checkdigit("{0.raw_number}{0.raw_birthday}{0.raw_expiration}{0.optionalA}{0.check_digit}".format(self))
    
 
class Passport(td2_MRTD):
    def __init__(self, **kwargs):
        super(Passport, self).__init__(**kwargs)
        if self.doc_type[0] != "P":
            raise ValueError('Wrong document type')


class Visa(td2_MRTD):
    def __init__(self, **kwargs):
        super(Visa, self).__init__(**kwargs)
        if self.doc_type[0] != "V":
            raise ValueError('Wrong document type')


class PermanentResident(td2_MRTD):
    def __init__(self, **kwargs):
        super(PermanentResident, self).__init__(**kwargs)
        if self.doc_type[0] != "C":
            raise ValueError('Wrong document type')