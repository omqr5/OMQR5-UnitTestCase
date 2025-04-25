import unittest
from stock_api import validate_symbol, validate_time_series
from chart_generator import validate_chart_type
from utils import validate_date

# Validate functions 
def get_valid_symbol(symbol):
    return validate_symbol(symbol)

def get_valid_chart_type(chart_type):
    return validate_chart_type(chart_type)

def get_valid_time_series(time_series):
    return validate_time_series(time_series)

def get_valid_date(date_str):
    return validate_date(date_str)

class TestInputValidation(unittest.TestCase):

#valid syy=mbol, invalid symbol with lowercase, invalid symbol contains numbers, invalid smbol length, invalid symbol null
    def test_valid_symbol(self):
        self.assertTrue(get_valid_symbol("GOOGL"))  
        self.assertFalse(get_valid_symbol("appl"))  
        self.assertFalse(get_valid_symbol("GOOG1234"))  
        self.assertFalse(get_valid_symbol("GOOGLEEE"))  
        self.assertFalse(get_valid_symbol(None))  
    
# valid chart, valid chart, invalid chart, invalid chart, invalid chart
    def test_valid_chart_type(self):
        self.assertTrue(get_valid_chart_type("1"))  
        self.assertTrue(get_valid_chart_type("2"))  
        self.assertFalse(get_valid_chart_type("3")) 
        self.assertFalse(get_valid_chart_type("4b")) 
        self.assertFalse(get_valid_symbol(None)) 

# valid time series, valid time series, invalid time series, invalid time series, invalid time series
    def test_valid_time_series(self):
        self.assertTrue(get_valid_time_series("1"))  
        self.assertTrue(get_valid_time_series("4"))  
        self.assertFalse(get_valid_time_series("5"))  
        self.assertFalse(get_valid_time_series("a"))  
        self.assertFalse(get_valid_time_series(None))  
    
# valid date, invalid date, invalid date, invalid date, invalid date, invalid date, invalid date
    def test_valid_date(self):
        self.assertTrue(get_valid_date("2025-04-25"))  
        self.assertFalse(get_valid_date("2025-04-31"))  
        self.assertFalse(get_valid_date("2025-13-25"))  
        self.assertFalse(get_valid_date("2025-04-2"))  
        self.assertFalse(get_valid_date("04-05-05"))  
        self.assertFalse(get_valid_date("2025-6-07"))  
        self.assertFalse(get_valid_date(None))  

if __name__ == "__main__":
    unittest.main()