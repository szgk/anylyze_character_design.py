## About

Get main colors from image data.

## initialize

```
python -m venv ./analyze_image
```

```
.\analyze_image\\Scripts\activate
```

## How to use

### Get main colors

```python
python ./src/get_main_colors.py input_directory_path output_directory_path
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/main_color.png)

### Get per main colors

```python
python ./src/get_per_mian_colors.py input_directory_path output_directory_path
```

![](https://github.com/szgk/anylyze_image.py/blob/main/images/per_main_colors.png)

### Remove background

```python
python ./src/remove_background. input_path output_directory_path
```

### get_kmeans_colors

```python
python ./src/get_kmeans_colors.py input_directory_path output_directory_path kmeans_num
```

### ge_main_color_names

```python
python ./src/ge_main_color_names.py input_directory_path output_json_path
```
