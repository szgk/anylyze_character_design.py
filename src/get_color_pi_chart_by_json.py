from PIL import Image
from pathlib import Path
import json

from utils import path
from utils import commindline
from utils import chart

def get_color_pi_chart_by_json():
    [chart_data1_dir, chart_data2dir, output_path] = commindline.get_args()

    data1_paths = path.get_file_paths_in_dir(chart_data1_dir, 'json')
    data2_paths = path.get_file_paths_in_dir(chart_data2dir, 'json')

    data_dict = {}

    for data1_path in data1_paths:
        data1 = json.load(open(data1_path, 'r', encoding="utf-8"))
        p_file = Path(data1_path)
        data_dict[p_file.stem] = {'data1': data1}

    for data2_path in data2_paths:
        data2 = json.load(open(data2_path, 'r', encoding="utf-8"))
        p_file = Path(data2_path)
        
        if(p_file.stem in data_dict and 'data1' in data_dict[p_file.stem]):
            data_dict[p_file.stem]['data2'] = data2
        else:
            print(p_file.name+' doesnt have data1')

    for key, data in data_dict.items():
        print(key)
        _output_path = output_path+'/'+key+'.png'
        chart.get_double_pie_chart(data['data1'], data['data2'], _output_path)

get_color_pi_chart_by_json()
