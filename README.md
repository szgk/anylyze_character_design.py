## About

program for analyze image.

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

### get_kmeans_colors

```python
python ./src/get_kmeans_colors.py input_directory_path output_directory_path kmeans_num
```

### get_main_color_codes

```python
python ./src/get_main_color_codes.py input_directory_path output_json_path
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/mian_color_codes.png)

### get_main_color_names

```python
python ./src/ge_main_color_names.py input_directory_path output_json_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/main_color_names.png)

### get_main_colors_pie_chart

```python
python ./src/get_main_colors_pie_chart.py input_directory_path output_file_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/main_colors_pie_chart.png)

### get_color_rate_pi_chart

```python
python ./src/get_color_rate_pi_chart.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/color_rate_pi_chart.png)

### get_color_rgb

```python
python ./src/get_color_rgb.py input_directory_path output_directory_path exe
```

### get_cropped_anime_face

```python
python ./src/get_cropped_anime_face.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/cropped_anime_face.png)

### get_anime_face_rect

refference this code. こちらのコードを参考にさせて頂いています
https://github.com/marron-akanishi/AFD/blob/master/sample.py

```python
python ./src/get_anime_face_rect.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/anime_face_rect.png)

### get_anime_face_landmark

```python
python ./src/get_anime_face_landmark.py input_directory_path output_directory_path exe
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/anime_face_landmark..png)
