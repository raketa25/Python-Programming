"""
This code defines a class `TempConvert` that provides methods to convert temperatures between Celsius, Fahrenheit, and Kelvin. The class takes a temperature value as input and has methods to perform the conversions. The example usage demonstrates how to use the class to convert temperatures in different units.
"""

class TempConvert:
    def __init__(self, temp):
        self.temp = temp
    # ------------------------ Methods to convert temperatures ------------------------------ #

    # Celsius to Kelvin and vice versa: C = K - 273.15, K = C + 273.15
    def celsius_to_kelvin(self):
        K_temp = self.temp + 273.15
        return K_temp

    def kelvin_to_celsius(self):
        C_temp = self.temp - 273.15
        return C_temp

    # Celsius to Fahrenheit and vice versa: F = (C * 9/5) + 32, C = (F - 32) * 5/9
    def celsius_to_fahrenheit(self):
        F_temp = (self.temp * 9/5) + 32
        return F_temp

    def fahrenheit_to_celsius(self):
        C_temp = (self.temp - 32) * 5/9
        return C_temp

    # Kelvin to Fahrenheit and vice versa: F = (K - 273.15) * 9/5 + 32, K = (F - 32) * 5/9 + 273.15
    def kelvin_to_fahrenheit(self):
        F_temp = (self.temp - 273.15) * 9/5 + 32
        return F_temp   

    def fahrenheit_to_kelvin(self):
        K_temp = (self.temp - 32) * 5/9 + 273.15
        return K_temp


# Example usage:
if __name__ == "__main__":

    temp_c = TempConvert(25)
    print(f"{temp_c.temp}°C is equal to {temp_c.celsius_to_fahrenheit()}°F")
    print(f"{temp_c.temp}°C is equal to {temp_c.celsius_to_kelvin()}K")
    print("\n")

    temp_f = TempConvert(77)
    print(f"{temp_f.temp}°F is equal to {temp_f.fahrenheit_to_celsius()}°C")
    print(f"{temp_f.temp}°F is equal to {temp_f.fahrenheit_to_kelvin()}K")
    print("\n")

    temp_k = TempConvert(300)
    print(f"{temp_k.temp}K is equal to {temp_k.kelvin_to_celsius()}°C")
    print(f"{temp_k.temp}K is equal to {temp_k.kelvin_to_fahrenheit()}°F")
