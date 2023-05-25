"""This module is used to contain the enum class with all
acceptable country values for usage in the cleaning module."""
from enum import Enum

class Country(Enum):
    """Accepted Country list"""

    AT = 'AUSTRIA'
    BE = 'BELGIUM'
    BG = 'BULGARIA'
    CH = 'SWITZERLAND'
    CY = 'CYPRUS'
    CZ = 'CZECHIA'
    DK = 'DENMARK'
    EE = 'ESTONIA'
    EL = 'GREECE'
    ES = 'SPAIN'
    FI = 'FINLAND'
    FR = 'FRANCE'
    HR = 'CROACIA'
    HU = 'HUNGARY'
    IS = 'ICELAND'
    IT = 'ITALY'
    LI = 'LIECHTENSTEIN'
    LT = 'LITHUANIA'
    LU = 'LUXEMBOURG'
    LV = 'LATVIA'
    MT = 'MALTA'
    NL = 'NETHERLANDS'
    NO = 'NORWAY'
    PL = 'POLAND'
    PT = 'PORTUGAL'
    RO = 'ROMANIA'
    SE = 'SWEDEN'
    SI = 'SLOVENIA'
    SK = 'SLOVAKIA'
    DE = 'GERMANY'
    AL = 'ALBANIA'
    IE = 'IRELAND'
    ME = 'MONTENEGRO'
    MK = 'NORTH_MACEDONIA'
    RS = 'SERBIA'
    AM = 'ARMENIA'
    AZ = 'AZERBAIJAN'
    GE = 'GEORGIA'
    TR = 'TURKEY'
    UA = 'UKRAINE'
    BY = 'BELARUS'
    UK = 'UNITED_KINGDOM'
    XK = 'KOSOVO'
    FX = 'FRANCE_METROPOLITAN'
    MD = 'MOLDOVA'
    SM = 'SAN_MARINO'
    RU = 'RUSSIA'

    @classmethod
    def get_list(cls):
        """This function is used to return the entire country code list
        for debugging purposes."""
        return [x.value for x in cls]

    def __str__(self):
        return self.name
