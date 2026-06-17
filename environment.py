import config as cf

class Environment:
    # Returns electricity price at a given hour
    def price(self, hour):
        return cf.e_price[hour]

    # Returns solar power generated at a given hour
    def solar_power(self, hour):
        return cf.solar_gen[hour]