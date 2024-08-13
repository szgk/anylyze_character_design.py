from PIL import Image
from pathlib import Path

from utils import path
from utils import commindline
from utils import chart
from utils import color
from utils import image
from utils import data

def get_color_pi_chart_by_path():
    [input_path, output_path, exe] = commindline.get_args()

    image_paths = path.get_file_paths_in_dir(input_path, exe)

    for image_path in image_paths:
        p_file = Path(image_path)
        _output_path = output_path+p_file.name

        # compress image
        rgb_arr = image.get_color_from_path(image_path, 700)

        color_name_dict = data.get_color_name_dict_by_rgb(rgb_arr)

        chart_data1 = data.get_color_name_chart_data(color_name_dict)
        chart_data2 = data.get_color_chart_data(color_name_dict)

        chart.get_double_pie_chart(chart_data1, chart_data2, _output_path)

get_color_pi_chart_by_path()
