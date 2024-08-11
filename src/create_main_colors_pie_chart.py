from PIL import Image
import cv2
import json

from utils import color
from utils import commindline
from utils import chart
from utils import data

def create_main_colors_pie_chart():
    [input_path, exe] = commindline.get_args()

    main_color_name_dict = data.get_main_color_name_dict_by_path(input_path, exe)

    chart_data = color.color_name_dict_to_chart_data(main_color_name_dict)

    print(chart_data)

    chart.create_pie_chart(chart_data)

create_main_colors_pie_chart()
