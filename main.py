import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
population_std_deviation = statistics.stdev(data)
print("The Mean of Population is: ", population_mean)
print("The Standard Deviation of Population is: ", population_std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset) 
    return mean

def show_fig(mean_list):
    sampling_mean = statistics.mean(mean_list)
    sampling_std_deviation = statistics.stdev(mean_list)
    print("Mean of Sampling Distribution: ",sampling_mean)
    print("Standard Deviation of Sampling Distribution: ",sampling_std_deviation)
    fig = ff.create_distplot([mean_list], ["Temperature"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()


