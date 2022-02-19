import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time


# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False


class GanttBar:
    def __init__(self, x_start: float = 0, x_end: float = 1, y: int = 0):
        self.x_start = x_start
        self.x_end = x_end
        self.y = y


def plot_to_file(i_plot):
    bars: [GanttBar] = [
        GanttBar(0, 1, 1), GanttBar(1, 2, 0), GanttBar(1, 3, 2), GanttBar(2 + i_plot, 5, 3),
        GanttBar(4, 50, 1)]
    plt.figure(figsize=(10, 5))
    for bar in bars:
        plt.barh(bar.y, bar.x_end - bar.x_start, left=bar.x_start)
    plt.yticks(ticks=range(0, 6), labels=["Core0", "Core1", "Core2", "Core3", "Core44", "Core555"])
    dir = "../image_gantt"
    plt.savefig(dir + "/" + str(i_plot) + '.jpg')


for i in range(20):
    plot_to_file(i)
