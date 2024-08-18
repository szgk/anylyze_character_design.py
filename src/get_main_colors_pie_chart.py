from PIL import Image

from utils import commindline
from utils import chart
from utils import data

def get_main_colors_pie_chart():
    [input_path, output_path, exe] = commindline.get_args()

    main_color_name_dict = data.get_main_color_name_dict_by_path(input_path, exe)

    chart_data1 = data.get_color_name_chart_data(main_color_name_dict)
    chart_data2 = data.get_color_chart_data(main_color_name_dict)

    chart.get_double_pie_chart_width_label(chart_data1, chart_data2, output_path)

get_main_colors_pie_chart()
