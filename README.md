## About

program for analyze character design.

やっていること・やる事

- 公開されている情報の分析、統計の為の学習
- 分析結果の無償公開

やっていない事・やらない事

- 版権物を使った生成 AI での画像・3D モデル生成、統計の為以外でのデータ生成
- 生成 AI に使うことが目的の学習
- 分析結果の売買

参考: https://www.vn3.org/terms#h.cselzcl2g6w

## initialize

```
python -m venv ./analyze_image
```

```
./analyze_image/Scripts/activate
```

## How to use

### Get main colors

```python
python ./src/get_main_colors.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/main_color.png)

### Get per main colors

```python
python ./src/get_per_mian_colors.py input_directory_path output_directory_path
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/per_main_colors.png)

### Remove background

```python
python ./src/remove_background.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/remove_background.png)

### Get kmeans colors

```python
python ./src/get_kmeans_colors.py input_directory_path output_directory_path kmeans_num
```

### Get main color codes

```python
python ./src/get_main_color_codes.py input_directory_path output_json_path
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/mian_color_codes.png)

### Get main color names

```python
python ./src/ge_main_color_names.py input_directory_path output_json_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/main_color_names.png)

### Get main colors pie chart

```python
python ./src/get_main_colors_pie_chart.py input_directory_path output_file_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/main_colors_pie_chart.png)

### Get color pi chart by path

```python
python ./src/get_color_pi_chart_by_path.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/color_rate_pi_chart.png)

### Get color rgb

```python
python ./src/get_color_rgb.py input_directory_path output_directory_path exe
```

### Get cropped anime face

```python
python ./src/get_cropped_anime_face.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/cropped_anime_face.png)

### Get anime face rect

refference this code. こちらのコードを参考にさせて頂いています
https://github.com/marron-akanishi/AFD/blob/master/sample.py

```python
python ./src/get_anime_face_rect.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/anime_face_rect.png)

### Get anime face landmark

```python
python ./src/get_anime_face_landmark.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/anime_face_landmark.png)

### Get anime face ratio

```python
python ./src/get_anime_face_ratio.py input_directory_path output_json_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/anime_face_ratio.png)

### Analyze face ratio dict

```python
python ./src/analyze_face_ratio_dict.py input_json_path output_json_path
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/analyze_face_ratio_dict.png)
