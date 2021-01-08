def plot_scattered_graph(plt=None, data_frame=None, input_series=None):

    if plt is not None and data_frame is not None and input_series is not None:
        filter_referance = data_frame.loc[data_frame['Date'] == input_series]
        x = filter_referance['Activity']
        specific_graph(plt, filter_referance, x, "Minutes")
        specific_graph(plt, filter_referance, x, "Calories")
        specific_graph(plt, filter_referance, x, "AverageHeartRate")

    else:
        pass

def specific_graph(plt, filter_referance, x, variable):
    y = filter_referance[variable]
    plt.xlabel("Activity")
    plt.ylabel("Data")
    if variable == "AverageHeartRate":
        plt.scatter(x, y, color="r")
        plt.plot(x, y, color="r", label="Average Heart Rate")
    elif variable == "Calories":
        plt.scatter(x, y, color="g")
        plt.plot(x, y, color="g", label=variable)
    else:
        plt.scatter(x, y, color="b")
        plt.plot(x, y, color="b", label=variable)
    plt.title("Activity Vs Data")
    plt.legend()