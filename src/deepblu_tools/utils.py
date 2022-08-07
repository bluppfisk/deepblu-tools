def get_depth(press, airpress, fresh):
    # Gets depth in metres. Formula looks wrong but it is actually
    # compensating for values incorrectly stored by Deepblu
    if not press:
        return None
    r = 1.025 if fresh and fresh == 1 else 1.0

    if not airpress:
        airpress = 1000

    if airpress and airpress >= 400 and airpress <= 1100:
        return (press - airpress) / r / 100


def convert_temp(decicelsius):
    # Deepblu reports temperature values in decicelsius
    # UDDF expects Kelvin
    if decicelsius == None:
        return None

    return (decicelsius / 10) + 273.15  # Decicelsius to Kelvin
