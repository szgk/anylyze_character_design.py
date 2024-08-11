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

    chart_data1 = color.color_name_dict_to_chart_data(main_color_name_dict)
    chart_data2 = color.main_color_dict_chart_data(main_color_name_dict)

    chart.create_double_pie_chart(chart_data1, chart_data2)

create_main_colors_pie_chart()
