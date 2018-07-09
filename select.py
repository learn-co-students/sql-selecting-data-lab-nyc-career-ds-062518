def select_all_columns_and_rows():
    return "SELECT * from planets;"

def select_name_and_color_of_all_planets():
    return "SELECT name, color from planets;"

def select_all_planets_with_mass_greater_than_one():
    return "SELECT * from planets WHERE mass>1.00;"

def select_name_and_mass_of_planets_with_mass_less_than_equal_to_one():
    return "SELECT name, mass from planets WHERE mass<=1.00;"

def select_name_and_color_of_planets_with_more_than_10_moons():
    return "SELECT name, color from planets WHERE num_of_moons>10"

def select_all_planets_with_moons_and_mass_less_than_one():
    return "SELECT * from planets WHERE num_of_moons>=1 and mass<1;"

def select_name_and_color_of_all_blue_planets():
    return "SELECT name, color from planets WHERE color LIKE '%blue%';"
