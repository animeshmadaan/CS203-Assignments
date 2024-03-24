import sys
from radial_method import radial_method
from mid_point_method import mid_point_method
from end_point_method import end_point_method

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <method_name>")
        return

    operation = sys.argv[1]

    if operation == 'radial':
        radial_method()
    elif operation == 'mid_point':
        mid_point_method()
    elif operation == "end_point":
        end_point_method()
    elif operation == "all" :
        mid_point_method()
        end_point_method()
        radial_method()
    else:
        print("Invalid operation. Please provide a valid operation.")

if __name__ == "__main__":
    main()
