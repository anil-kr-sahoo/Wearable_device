import matplotlib.pyplot as plt
import pandas as pd
from bar_graph_plot import plot_bar_graph
from scattered_graph_plot import plot_scattered_graph
from user_input import input_given

plt.style.use("bmh")
data_frame = pd.read_csv("wearable_data_60.csv")
print(data_frame)
all_series = data_frame['Date']
valid_data_series = list(set(all_series))

print("\nCorrupted Data List \n")
print("\nTotal Valid Data Series We have "+str(len(valid_data_series)))

input_series = input_given(valid_data_series)
if not input_series:
    print("\n Please enter a valid series")
elif input_series not in valid_data_series:
    print("\n Invalid Date Given")
else:
    bar_graph = plt.figure(1)
    plot_bar_graph(plt, data_frame, input_series)
    scattered_graph = plt.figure(2)
    plot_scattered_graph(plt, data_frame, input_series)
    plt.show()