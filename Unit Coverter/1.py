"""
Unit Converter
Unit converter to convert between different units of measurement.


Requirements
Build a simple web page that will have different sections for different units of measurement. The user can input a value to convert, select the units to convert from and to, and view the converted value.

The user can input a value to convert.

The user can select the units to convert from and to.

The user can view the converted value.

The user can convert between different units of measurement like length, weight, temperature, etc (more given below).

You can include the following units of measurement to convert between:

Length: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.

Weight: milligram, gram, kilogram, ounce, pound.

Temperature: Celsius, Fahrenheit, Kelvin.
"""

def length_unit_name(choice):
    if choice == "1":
        return "millimeter"
    elif choice == "2":
        return "centimeter"
    elif choice == "3":
        return "meter"
    elif choice == "4":
        return "kilometer"
    elif choice == "5":
        return "inch"
    elif choice == "6":
        return "foot"
    elif choice == "7":
        return "yard"
    elif choice == "8":
        return "mile"
    return "unknown"


def weight_unit_name(choice):
    if choice == "1":
        return "milligram"
    elif choice == "2":
        return "gram"
    elif choice == "3":
        return "kilogram"
    elif choice == "4":
        return "ounce"
    elif choice == "5":
        return "pound"
    return "unknown"


def temp_unit_name(choice):
    if choice == "1":
        return "Celsius"
    elif choice == "2":
        return "Fahrenheit"
    elif choice == "3":
        return "Kelvin"
    return "unknown"


def length_to_meter(value, unit_choice):
    if unit_choice == "1":
        return value / 1000
    elif unit_choice == "2":
        return value / 100
    elif unit_choice == "3":
        return value
    elif unit_choice == "4":
        return value * 1000
    elif unit_choice == "5":
        return value * (127 / 5000)
    elif unit_choice == "6":
        return value * ((127 / 5000) * 12)
    elif unit_choice == "7":
        return value * ((127 / 5000) * 12 * 3)
    elif unit_choice == "8":
        return value * ((127 / 5000) * 12 * 3 * 1760)
    return None


def meter_to_length(value_in_meter, unit_choice):
    if unit_choice == "1":
        return value_in_meter * 1000
    elif unit_choice == "2":
        return value_in_meter * 100
    elif unit_choice == "3":
        return value_in_meter
    elif unit_choice == "4":
        return value_in_meter / 1000
    elif unit_choice == "5":
        return value_in_meter / (127 / 5000)
    elif unit_choice == "6":
        return value_in_meter / ((127 / 5000) * 12)
    elif unit_choice == "7":
        return value_in_meter / ((127 / 5000) * 12 * 3)
    elif unit_choice == "8":
        return value_in_meter / ((127 / 5000) * 12 * 3 * 1760)
    return None


def weight_to_kilogram(value, unit_choice):
    if unit_choice == "1":
        return value / 1000000
    elif unit_choice == "2":
        return value / 1000
    elif unit_choice == "3":
        return value
    elif unit_choice == "4":
        return value * ((45359237 / 100000000) / 16)
    elif unit_choice == "5":
        return value * (45359237 / 100000000)
    return None


def kilogram_to_weight(value_in_kg, unit_choice):
    if unit_choice == "1":
        return value_in_kg * 1000000
    elif unit_choice == "2":
        return value_in_kg * 1000
    elif unit_choice == "3":
        return value_in_kg
    elif unit_choice == "4":
        return value_in_kg / ((45359237 / 100000000) / 16)
    elif unit_choice == "5":
        return value_in_kg / (45359237 / 100000000)
    return None


def to_celsius(value, unit_choice):
    if unit_choice == "1":
        return value
    elif unit_choice == "2":
        return (value - 32) * 5 / 9
    elif unit_choice == "3":
        return value - (27315 / 100)
    return None


def from_celsius(value_in_celsius, unit_choice):
    if unit_choice == "1":
        return value_in_celsius
    elif unit_choice == "2":
        return (value_in_celsius * 9 / 5) + 32
    elif unit_choice == "3":
        return value_in_celsius + (27315 / 100)
    return None


def show_length_units():
    print("""1. millimeter
2. centimeter
3. meter
4. kilometer
5. inch
6. foot
7. yard
8. mile""")


def show_weight_units():
    print("""1. milligram
2. gram
3. kilogram
4. ounce
5. pound""")


def show_temp_units():
    print("""1. Celsius
2. Fahrenheit
3. Kelvin""")


print("Unit Converter")

while True:
    print("""
Choose type:
1. Length
2. Weight
3. Temperature
4. Exit""")

    category = input("Enter choice: ").strip()

    if category == "4":
        print("Exit")
        break

    if category != "1" and category != "2" and category != "3":
        print("Invalid type choice")
        continue

    value_text = input("Enter value: ").strip()
    try:
        value = float(value_text)
    except ValueError:
        print("Please enter a valid number")
        continue

    if category == "1":
        print("\nLength units:")
        show_length_units()
        from_unit = input("From unit number: ").strip()
        to_unit = input("To unit number: ").strip()

        meter_value = length_to_meter(value, from_unit)
        if meter_value is None:
            print("Invalid length unit")
            continue

        result = meter_to_length(meter_value, to_unit)
        if result is None:
            print("Invalid length unit")
            continue

        print(f"{value} {length_unit_name(from_unit)} = {result:.6f} {length_unit_name(to_unit)}")

    elif category == "2":
        print("\nWeight units:")
        show_weight_units()
        from_unit = input("From unit number: ").strip()
        to_unit = input("To unit number: ").strip()

        kg_value = weight_to_kilogram(value, from_unit)
        if kg_value is None:
            print("Invalid weight unit")
            continue

        result = kilogram_to_weight(kg_value, to_unit)
        if result is None:
            print("Invalid weight unit")
            continue

        print(f"{value} {weight_unit_name(from_unit)} = {result:.6f} {weight_unit_name(to_unit)}")

    elif category == "3":
        print("\nTemperature units:")
        show_temp_units()
        from_unit = input("From unit number: ").strip()
        to_unit = input("To unit number: ").strip()

        celsius_value = to_celsius(value, from_unit)
        if celsius_value is None:
            print("Invalid temperature unit")
            continue

        result = from_celsius(celsius_value, to_unit)
        if result is None:
            print("Invalid temperature unit")
            continue

        print(f"{value} {temp_unit_name(from_unit)} = {result:.6f} {temp_unit_name(to_unit)}")

        