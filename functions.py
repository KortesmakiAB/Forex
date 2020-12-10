from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal

def get_curr_codes():
    """extract curency codes from "List of Supported Currency codes" paragraph found on https://forex-python.readthedocs.io/en/latest/currencysource.html.
    Assumes a "|" delimiter."""
    
    supported_codes_paragraph = "|EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |GBP - United Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint |RON - Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar |HKD - Hong Kong Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi |TRY - Turkey Lira |HRK - Croatia Kuna |NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States Dollar |NOK - Norway Krone |RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic Koruna |BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand"
    code_list = supported_codes_paragraph.split("|")

    curr_codes = [country_description[:3] for country_description in code_list]
    curr_codes.pop(0)
    return curr_codes
 
          
def handle_error_msg(converting_from, converting_to, amount):
    """Handle error messages for invalid currency codes and invalid amounts
    
    >>> handle_error_msg('SPRINGBOARD', 'USD', 999)
    'Please enter a valid "Converting from:" currency code.'

    >>> handle_error_msg('USD', 'SPRINGBOARD', 888)
    'Please enter a valid "Converting to:" currency code.'

    >>> handle_error_msg('USD', 'ILS', -777)
    'Please enter a positive currency "Amount:" to be converted.'
    
    >>> handle_error_msg('USD', 'GBP', 987.65)

    """

    curr_codes = get_curr_codes()

    if converting_from not in curr_codes:
        return 'Please enter a valid "Converting from:" currency code.'

    elif converting_to not in curr_codes:
        return 'Please enter a valid "Converting to:" currency code.'

    elif amount <= 0:
        return 'Please enter a positive currency "Amount:" to be converted.'

    else:
        return None


def handle_conversion(converting_from, converting_to, amount):
    """Make currency conversion and return as a decimal with two places
    
    >>> handle_conversion('USD', 'USD', '100')
    Decimal('100.00')
    """
    
    c = CurrencyRates()   
    conversion = c.convert(converting_from, converting_to, amount)
    TWOPLACES = Decimal(10) ** -2
    return Decimal(conversion).quantize(TWOPLACES)


def get_curr_symbol(converting_to):
    """Get currency symbol
    
    >>> get_curr_symbol('USD')
    'US$'
    """

    c = CurrencyCodes()
    return c.get_symbol(converting_to)    


# def get_curr_name(country_code):
#     """Get currency name"""

#     c = CurrencyCodes()
#     return c.get_currency_name(country_code)
    
