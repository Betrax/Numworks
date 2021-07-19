from math import *


# Accessing shapes will happen by their index number
# The list is formed in the following structure [Name or "Mother", formula 1, formula 2, ...]
list_shapes = [
    ["cilinder", ["V", "pi*r^2*h"], ["M", "2*pi*r*h"], ["A", "2*pi*r*h + 2*pi*r^2"]],
    ["kegel", "1/3*pi*r^2*h", "pi*r*a", "pi*r*a + pi*r^2"],
    [
        "afgeknokte kegel",
        "1/3*pi*h*((r_1)^2+(r_2)^2+(r_1)*(r_2))",
        "pi*(r_1+r_2)*a",
        "pi*a*(r_1+r_2) + pi*((r_1)^2+(r_2)^2)",
    ],
    ["bol", "4/3*pi*r^3", "4*pi*r^2"],
    ["bolzone", "pi*(r_1)^2*h/2+pi*(r_2)^2*h/2+pi*h^3/6", "2*pi*r*h"],
    ["bolkap", "1/3*pi*h^2*(3*r-h)", "2*pi*r*h"],
    ["bolschil", "1/6*pi*h*k^2"],
    ["bolsector", "2/3*pi*r^2"],
    ["piramide", "1/3*G*h"],
    ["afgeknotte priamide", "1/3*h*(G+B+sqrt(B*G))"],
    ["torus", "(pi*r^2)*(2*pi*R)"],
    ["trapezium", "(b_1+b_2)*h/2"],
    ["ruit", "d_1*d_2/2"],
    ["cirkel", ["V", "r^2*hoek/2"], ["bol buiten 3hoek", "r^2/2*(alpha - sin(alpha))"]]
]


def main():
    for x in range(len(list_shapes)):  # Prints the name of all contained shapes
        print(x, list_shapes[x][0])

    figur_num = int(input("Figuur= "))  # Select the number of the shape
    print_shape_name(figur_num)
    print_formulas(figur_num)

    # If the mother contains 1 formula, it directly starts executing it
    if (len(list_shapes[figur_num]) - 1) == 1:
        formula_num = 1
    else:
        formula_num = int(input("Formule= "))
        print("\n{}".format(return_formula(figur_num, formula_num)))

    solver(figur_num, formula_num)


# Prints the shapes name centered
def print_shape_name(figur_num):
    shape_name = list_shapes[figur_num][0]  # Takes the shape name
    # Centers the Mother value while printing, screen width (amount of chars that go into 1 line from left to right is 42)
    print("{:^42}".format(shape_name.upper()))


# Prints all the availible formulas of the shape
def print_formulas(figur_num):
    # Starts counting by skipping the name
    for x in range(len(list_shapes[figur_num][1:])):

        # Fixes the array order by adding +1 to x (Number 0 is the mother already)
        # Needed a modified version of return_formula to also print the name of the formula that's in [0]
        if isinstance(list_shapes[figur_num][x + 1], str):
            print("{}. {}".format(x + 1, list_shapes[figur_num][x + 1]))
        else:
            print(
                "{}. {}: {}".format(
                    x + 1,
                    list_shapes[figur_num][x + 1][0],
                    list_shapes[figur_num][x + 1][1],
                )
            )


# Checks if the formula is a array dimension (I store names of formulas in a separate dimension)
def return_formula(figur_num, formula_num):
    if isinstance(list_shapes[figur_num][formula_num], str):
        return list_shapes[figur_num][formula_num]
    else:
        return list_shapes[figur_num][formula_num][1]


def solver(figur_num, formula_num):
    # "^" for powers in math means something else in Python, thereby we need to change all of them to "**" which is the right operator for this
    formula = return_formula(figur_num, formula_num).replace("^", "**")

    while True:
        try:
            print("Antwoord: {}".format(eval(formula)))
            break  # Will break the function if the line above doesn't outputs error

        except Exception as error:
            variable = str(error).split("'")[1]
            variable_equal = variable + "=" + input(variable + "= ")
            exec(variable_equal)


main()
