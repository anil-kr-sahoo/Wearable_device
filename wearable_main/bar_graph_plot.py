import numpy as np
def plot_bar_graph(plt=None, data_frame=None, input_series=None):

    if plt is not None and data_frame is not None and input_series is not None:
        bar_width = .2
        filter_referance = data_frame.loc[data_frame['Date'] == input_series]
        activity_list = filter_referance['Activity']
        calories_list = filter_referance['Calories']
        minutes_list = filter_referance['Minutes']
        heart_rate_list = filter_referance['AverageHeartRate']

        cal_bar = np.arange(len(activity_list))
        min_bar = [i+bar_width for i in cal_bar]
        heartrate_bar = [i+bar_width for i in min_bar]
        plt.bar(cal_bar, calories_list, bar_width, color="g", label="Calories")
        plt.bar(min_bar, minutes_list, bar_width, color="b", label="Minutes")
        plt.bar(heartrate_bar, heart_rate_list, bar_width, color="r", label="Average Heart Rate")
        plt.xlabel("Activity")
        plt.ylabel("Data")
        plt.title("Activity Vs Data")
        plt.xticks(cal_bar+bar_width, activity_list)
        plt.legend()
    else:
        pass