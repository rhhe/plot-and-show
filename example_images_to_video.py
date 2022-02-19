import os
import cv2
import matplotlib.pyplot as plt


class GanttBar:
    def __init__(self, x_start: float = 0, x_end: float = 1, y: int = 0):
        self.x_start = x_start
        self.x_end = x_end
        self.y = y


def make_gantt_chart_files(dir_images: str = "./image_gantt"):
    if not os.path.exists(dir_images):
        os.makedirs(dir_images)
    n_chart: int = 16
    for i_chart in range(n_chart):
        bars: [GanttBar] = [
            GanttBar(0, 1, 1),
            GanttBar(1, 2, 0),
            GanttBar(1, 3, 2),
            GanttBar(2, 5 + i_chart, 3),
            GanttBar(4, 50, 1)
        ]
        plt.figure(figsize=(10, 5))
        for bar in bars:
            plt.barh(bar.y, bar.x_end - bar.x_start, left=bar.x_start)
        plt.yticks(ticks=range(0, 6), labels=["zero", "one", "two", "three", "four", "five"])
        file_name = os.path.join(dir_images, str(i_chart) + '.jpg')
        plt.savefig(file_name)
        print("save fig: {}".format(file_name))


def gantt_charts_to_video(dir_images="./image_gantt", dir_video="./videos", file_video="gantt"):
    # get image file names
    file_names = os.listdir(dir_images)
    file_names = [o for o in file_names if o.split('.')[-1] == 'jpg']
    if not file_names:
        print("warning: no file.")
        return
    file_names = sorted(file_names, key=lambda x: int(x.split('.')[-2]))
    print("file names: ", file_names)

    # get parameter for cv and initialize cv instance
    video_dir = os.path.join(dir_video, file_video + '.avi')
    if not os.path.exists(dir_video):
        os.makedirs(dir_video)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    fps = 4
    shape = cv2.imread(os.path.join(dir_images, file_names[0])).shape
    image_size = (shape[1], shape[0])
    video_writer = cv2.VideoWriter(video_dir, fourcc, fps, image_size)

    # read images and create video file
    for file_name in file_names:
        full_path = os.path.join(dir_images, file_name)
        image = cv2.imread(full_path)
        video_writer.write(image)
    video_writer.release()


if __name__ == '__main__':
    make_gantt_chart_files()
    gantt_charts_to_video()
