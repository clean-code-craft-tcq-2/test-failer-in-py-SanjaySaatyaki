def get_pair_number(major_num,minor_num):
    return (major_num * 5 + minor_num)+1

def format_row(pair_number,major_colour, minor_color):
    return '{pair_number}\t{major_colour}\t{minor_color}'

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(format_row(get_pair_number(i,j),major,minor))


assert(get_pair_number(0,0)==1)
assert(format_row(1,'White','Blue'=='1\tWhite\tBlue'))
print("All is well (maybe!)\n")
