from PIL import Image
from pathlib import Path
import json

from utils import path
from utils import commindline
from utils import chart

# get data with src\get_avatar_info_for_chart_by_json.py
def get_avatar_info_chart_by_json():
    [output_path] = commindline.get_args()

    attribute_data = json.load(open('./data_text/avatar_data_for_chart/attribute_data_for_pie_chart.json', 'r', encoding="utf-8"))
    category_data = json.load(open('./data_text/avatar_data_for_chart/category_data_for_pie_chart.json', 'r', encoding="utf-8"))

    chart.get_pie_chart(attribute_data, output_path + 'attribute_data_for_pie_chart.png')
    chart.get_pie_chart(category_data, output_path + 'category_data_for_pie_chart.png')

get_avatar_info_chart_by_json()
