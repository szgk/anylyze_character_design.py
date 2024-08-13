import json
from utils import commindline
from datetime import datetime as dt

# get data from src\merge_avatar_data_and_face_raito_data.py

# avatar data with face ratio
# {
#  "aaa": {
#     "about_sale_date": "2021/8/13",
#     "name": "aaa",
#     "data_id": "aaa",
#     "author": "aaa",
#     "like": "7741",
#     "url": "aaa",
#     "category": "少女",
#     "about_polygon": "56699",
#     "body": "中",
#     "bust": "中",
#     "kemomimi": "",
#     "tail": "",
#     "horn": "",
#     "wing": "",
#     "elfmimi": "",
#     "hairo": "",
#     "robo": "",
#     "face_raito": [
#         {
#             "face_width": 107,
#             "face_height": 107,
#             "eye_count": 2,
#             "eye_height": 0.17757009345794392,
#             "eye_width": 0.22429906542056074,
#             "eye_to_eye": -0.6355140186915887,
#             "eye_to_side": 0.17757009345794392,
#             "eye_to_jaw": 0.5607476635514018,
#             "eye_to_forehead": 0.38317757009345793
#         }
#     ]
# },

def get_avatar_info_for_chart_by_json():
    [input_data, output_path] = commindline.get_args()
    avatar_data = json.load(open(input_data, encoding="utf-8"))

    category_data_for_pie_chart = {
        'labels': ['少女', '少年', 'ケモノ', 'ちびキャラ'],
        'values': [0, 0, 0, 0],
    }

    attribute_data_for_pie_chart = {
        'labels': [
            'けもみみ+しっぽ+角',
            'けもみみ+しっぽ',
            'けもみみ＋角',
            'しっぽ+角',
            'けもみみ',
            'しっぽ',
            'ヘイロー',
            'エルフみみ',
            '角',
            'ロボ',
            'なし',
        ],
    }
    attribute_data_for_pie_chart['values'] = [0] * len(attribute_data_for_pie_chart['labels'])

    sale_date_dict = {
        'year': {},
        'month': {},
    }
    sale_year_data_for_pie_chart = {
        'labels': [],
        'values': []
    }
    sale_month_data_for_pie_chart = {
        'labels': [],
        'values': []
    }

    ##############################################

    for value in avatar_data.values():
        cat = value['category']
        # 少女
        if cat == '少女':
            category_data_for_pie_chart['values'][0] += 1
        # 少年
        elif cat == '少年':
            category_data_for_pie_chart['values'][1] += 1
        # ケモノ
        elif cat == 'ケモノ':
            category_data_for_pie_chart['values'][2] += 1
        # ちびキャラ
        elif cat == 'ちびキャラ':
            category_data_for_pie_chart['values'][3] += 1

        ##############################################

        # けもみみ+しっぽ+角
        if len(value['kemomimi']) > 0 and len(value['tail']) > 0 and len(value['horn']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('けもみみ+しっぽ+角')] += 1
        # けもみみ+しっぽ
        elif len(value['kemomimi']) > 0 and len(value['tail']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('けもみみ+しっぽ')] += 1
        # けもみみ+角
        elif len(value['kemomimi']) > 0 and len(value['horn']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('けもみみ＋角')] += 1
        # しっぽ+角
        elif len(value['tail']) > 0 and len(value['horn']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('しっぽ+角')] += 1
        # けもみみ
        elif len(value['kemomimi']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('けもみみ')] += 1
        # しっぽ
        elif len(value['tail']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('しっぽ')] += 1
        # 角
        elif len(value['horn']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('角')] += 1
        # ヘイロー
        elif len(value['hairo']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('ヘイロー')] += 1
        # エルフみみ
        elif len(value['elfmimi']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('エルフみみ')] += 1
        # ロボ
        elif len(value['robo']) > 0:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('ロボ')] += 1
        # なし
        else:
            attribute_data_for_pie_chart['values'][attribute_data_for_pie_chart['labels'].index('なし')] += 1

        ##############################################

        sale_date = value['about_sale_date']

        sale_year = dt.strptime(sale_date, '%Y/%m/%d').year
        sale_month = dt.strptime(sale_date, '%Y/%m/%d').month

        if(sale_year in sale_date_dict['year']):
            sale_date_dict['year'][sale_year] += 1
        else:
            sale_date_dict['year'][sale_year] = 1

        if(sale_month in sale_date_dict['month']):
            sale_date_dict['month'][sale_month] += 1
        else:
            sale_date_dict['month'][sale_month] = 1

            

    sorted_year_dict = sorted(sale_date_dict['year'].items(), key=lambda x:x[0])
    for key, value in sorted_year_dict:
        sale_year_data_for_pie_chart['labels'].append(key)
        sale_year_data_for_pie_chart['values'].append(value)
    
    sorted_month_dict = sorted(sale_date_dict['month'].items(), key=lambda x:x[0])
    for key, value in sorted_month_dict:
        sale_month_data_for_pie_chart['labels'].append(key)
        sale_month_data_for_pie_chart['values'].append(value)

    print(category_data_for_pie_chart)
    with open(output_path+'category_data_for_pie_chart.json', 'w', encoding="utf-8") as f:
        print('save json')
        json.dump(category_data_for_pie_chart, f, ensure_ascii=False)

    print(attribute_data_for_pie_chart)
    with open(output_path+'attribute_data_for_pie_chart.json', 'w', encoding="utf-8") as f:
        print('save json')
        json.dump(attribute_data_for_pie_chart, f, ensure_ascii=False)

    print(sale_year_data_for_pie_chart)
    with open(output_path+'sale_year_data_for_pie_chart.json', 'w', encoding="utf-8") as f:
        print('save json')
        json.dump(sale_year_data_for_pie_chart, f, ensure_ascii=False)

    print(sale_month_data_for_pie_chart)
    with open(output_path+'sale_month_data_for_pie_chart.json', 'w', encoding="utf-8") as f:
        print('save json')
        json.dump(sale_month_data_for_pie_chart, f, ensure_ascii=False)

get_avatar_info_for_chart_by_json()