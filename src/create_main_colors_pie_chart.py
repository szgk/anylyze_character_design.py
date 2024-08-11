from PIL import Image
import cv2
import json

from utils import color
from utils import commindline
from utils import chart

def create_main_colors_pie_chart():
    [input_path] = commindline.get_args()

    data_json = {}

    with open(input_path) as f:
        data_json = json.load(f)

    chart_data = color.color_name_dict_to_chart_data(data_json)

    print(chart_data)

    # data = {'values': [1,2,3], 'labels': ['a', 'i', 'u'], 'colors': ['#ffaa00', '#0099dd', '#0000ff']}

    # chart.create_pie_chart(data)

create_main_colors_pie_chart()
