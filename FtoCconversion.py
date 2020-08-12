print("Welcome to fahrenheit to degree conversion App")

f = float(input('Enter temperature in Fahrenheit: '))

c = round(((f - 32) * 5 / 9), 4)

k = round((c + 273.15), 4)
print("Degrees Fahrenheit: ", f, "deg F")
print("Degrees Celcius: ", c, "deg C")
print("Degrees Kelvin: ", k, "deg K")
