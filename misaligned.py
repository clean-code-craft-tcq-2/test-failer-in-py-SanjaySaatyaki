def print_color_map():
    all_color_codes = []
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            all_color_codes.append(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors),all_color_codes


result,all_color_codes = print_color_map()
assert(result == 25)
assert('White' in  all_color_codes[0])
assert('Blue' in  all_color_codes[0])
assert('1' in  all_color_codes[0])
index_of_seperator = all_color_codes[0].index("|")
for color in all_color_codes:
    assert(index_of_seperator == color.index("|"))
print("All is well (maybe!)\n")
