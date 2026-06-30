import string
import random 

def random_user_id():
    char= string.ascii_letters+string.digits
    return "".join(random.choice(char) for _ in range(6))
print(random_user_id())

def user_id_gen_by_user():
    char= string.ascii_letters+string.digits
    no_input=int(input("enter no of character:"))
    id_gen=int(input("Enter the id to generate:"))
    for _ in range(id_gen):
        print("".join(random.choice(char) for _ in range(no_input)))
user_id_gen_by_user()

def rgb_color_gen():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())

HEX_CHARS = "0123456789abcdef"

def _hex_color():
    return "#" + "".join(random.choice(HEX_CHARS) for _ in range(6))
print(_hex_color())


def _rgb_color():
    r, g, b = (random.randint(0, 255) for _ in range(3))
    return f"rgb({r},{g},{b})"
print(_rgb_color())


def list_of_hexa_colors(count):
    return [_hex_color() for _ in range(count)]



# 2. List of rgb colors
def list_of_rgb_colors(count):
    return [_rgb_color() for _ in range(count)]


# 3. Generate any number of hexa or rgb colors
def generate_colors(color_type, count):
    """
    color_type : 'hexa' or 'rgb'
    count      : how many colors to generate
    """
    if color_type == "hexa":
        return list_of_hexa_colors(count)
    elif color_type == "rgb":
        return list_of_rgb_colors(count)
    else:
        return f"Unknown type '{color_type}'. Use 'hexa' or 'rgb'."


print(list_of_hexa_colors(3))


print(list_of_rgb_colors(3))


print(generate_colors("hexa", 4))


print(generate_colors("rgb", 4))