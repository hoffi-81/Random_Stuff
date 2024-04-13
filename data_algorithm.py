import matplotlib.pyplot as plt

def show_start_data_bar(names, values):
    plt.bar(names, values)
    plt.show()

names = ['group_a', 'group_b', 'group_c']


values_input = input("Enter values separated by spaces: ")
values = list(map(int, values_input.split()))  

show_start_data_bar(names, values)