import calendar


def plot_scattered_graph(plt=None, data_frame=None, input_series=None):
    if plt is not None and data_frame is not None and input_series is not None:
        filter_referance = data_frame.loc[data_frame['Date'] == input_series]
        x = filter_referance['Activity']
        specific_graph(plt, filter_referance, x, "Minutes")
        specific_graph(plt, filter_referance, x, "Calories")
        specific_graph(plt, filter_referance, x, "AverageHeartRate")
        proper_date = input_series.split('/')[0] + " " + calendar.month_name[int(input_series.split('/')[1])][
                                                         :3] + ". 20" + \
                      input_series.split('/')[2]
        plt.title("Activity Vs Data (" + proper_date + ")")
        plt.legend()

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
