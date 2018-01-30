
"""
build a calculator that provides the
amount of miles per gallon

miles per gallon = miles driven/gallons used
"""
miles_driven = 240
gallons_used = 4

print("This program calulates mpg.")
miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons used: "))
mpg= miles_driven / gallons_used

print("Your miles per gallon is", mpg)
