'''
The outside world:
    Hourly electricity prices
    Solar generation curve
    Peak demand periods
'''

import config as cf

class Environment:
    def price(self, hour):
        return cf.e_price[hour]

    def solar_power(self, hour):
        return cf.solar_gen[hour]