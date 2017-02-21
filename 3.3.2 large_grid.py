def print_horizontal():

    print('+ - - - -', end=' ')


def print_vertical():

    print('|        ', end = ' ')


def print_twice(f):

    f()

    f()


def print_v_frice(f):

    print_twice(f)

    print_twice(f)


def print_h_frice(f):

    print_twice(f), print_twice(f)


def print_row():

    print_h_frice(print_horizontal), print('+')


def print_vertical_row():

    print_h_frice(print_vertical), print('|')


def print_frice_vertical(f):

    print_h_frice(f)


def print_four_verticals():

    print_v_frice(print_vertical_row)


def print_the_box():

    print_row()

    print_four_verticals()


def print_the_whole_thing():

    print_v_frice(print_the_box)

    print_row()


print_the_whole_thing()