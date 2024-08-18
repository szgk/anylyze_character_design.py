from PIL import Image
from pathlib import Path
import json

from utils import commindline
from utils import chart

# get data with src\get_avatar_info_for_chart_by_json.py
def get_avatar_info_chart_by_json():
    [output_path] = commindline.get_args()

    attribute_data = json.load(open('./data_text/avatar_data_for_chart/attribute_data_for_pie_chart.json', 'r', encoding="utf-8"))
    category_data = json.load(open('./data_text/avatar_data_for_chart/category_data_for_pie_chart.json', 'r', encoding="utf-8"))
    sale_month_data = json.load(open('./data_text/avatar_data_for_chart/sale_month_data_for_pie_chart.json', 'r', encoding="utf-8"))
    sale_year_data = json.load(open('./data_text/avatar_data_for_chart/sale_year_data_for_pie_chart.json', 'r', encoding="utf-8"))
    body_data = json.load(open('./data_text/avatar_data_for_chart/body_data_for_pie_chart.json', 'r', encoding="utf-8"))
    chest_data = json.load(open('./data_text/avatar_data_for_chart/chest_data_for_pie_chart.json', 'r', encoding="utf-8"))
    body_and_chest_data = json.load(open('./data_text/avatar_data_for_chart/body_and_chest_data_for_pie_chart.json', 'r', encoding="utf-8"))

    chart.get_pie_chart(attribute_data, output_path + 'attribute_data_pie_chart.png')
    chart.get_pie_chart(category_data, output_path + 'category_data_pie_chart.png')
    chart.get_pie_chart(sale_month_data, output_path + 'sale_month_data_pie_chart.png')
    chart.get_pie_chart(sale_year_data, output_path + 'sale_year_data_pie_chart.png')
    chart.get_pie_chart(body_data, output_path + 'body_data_pie_chart.png')
    chart.get_pie_chart(chest_data, output_path + 'chest_data_pie_chart.png')
    chart.get_pie_chart(body_and_chest_data, output_path + 'body_and_chest_data_pie_chart.png')

get_avatar_info_chart_by_json()
