def print_names(list_of_names):
    for name in list_of_names:
        print(name)

def print_dictionary(input_dictionary):
    for key, value in input_dictionary.items():
        print("Key: " + key + ", Value: " + str(value))

def _private_function():
    print("I'm a private function!")