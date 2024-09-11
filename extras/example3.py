import argparse

parser = argparse.ArgumentParser(description="Some helping description")
parser.add_argument("a", help="First position argument help", type=int, dest="first_arg")  # dest -> remaping variable name
parser.add_argument("b", help="Second position argument help", type=int, dest="second_arg")
parser.add_argument("-f", "--first", help="First kwarg", type=str, required=False)
parser.add_argument("-s", "--second", help="Second kwarg", type=str, required=True)
parser.add_argument("--third", help="Third kwarg", type=int, required=False)

# element lists
parser.add_argument("--sq", help="List of numbers", nargs="*", type=float)  # nargs='*' -> number of elements (possibly empty list), not required 
parser.add_argument("--cu", help="List of numbers", nargs="+", type=float, required=True)  # nargs='+' -> at least one element required


# actions
parser.add_argument("--monty", action="store")  # action is "store" by default
parser.add_argument("--const", action="store_const", const="Python")  # if --const is passed, this variable will be present
parser.add_argument("--default", default="John")  #  default value


# flags
parser.add_argument("-v", "--verbose", action="store_const", default=False, const=True)  # verbose flag example
parser.add_argument("-q", "--quiet", action="store_false")  # if it's not specified, then it's True


# mutually exclusive args
group = parser.add_mutuall_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")


args = parser.parse_args()  # check sys.argv by default

print(args)
