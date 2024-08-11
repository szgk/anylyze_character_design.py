from enum import Enum
import math
from decimal import Decimal, ROUND_HALF_UP

class COLOR_NAMES(Enum):
    R = 'Red'
    O = 'Orange'
    Y = 'Yellow'
    YG = 'Yellow Green'
    G = 'Green'
    BG = 'Blue Green'
    LB = 'Light Blue'
    B = 'Blue'
    DB = 'Dark Blue'
    BV = 'Blue Violet'
    V = 'Violet'
    VR = 'Violet Red'
    GREY = 'Grey'
    BLACK = 'Black'
    WHITE = 'White'
class COLOR_CODES(Enum):
    R = '#ff0000'
    O = '#ff7f00'
    Y = '#ffff00'
    YG = '#7fff00'
    G = '#00ff00'
    BG = '#00ff7f'
    LB = '#00ffff'
    B = '#007fff'
    DB = '#0000ff'
    BV = '#7f00ff'
    V = '#ff00ff'
    VR = '#ff007f'
    GREY = '#888888'
    BLACK = '#000000'
    WHITE = '#ffffff'

def get_dict_for_pie_chart():
  return {'values': [], 'labels': [], 'colors': []}

def get_hue_from_RGB(rgb):
    hue = 0
    mx = max(rgb)
    mn = min(rgb)
    [r, g, b] = rgb

    if (r == mx):
      hue = 60 * ((g - b) / (mx - mn))

    elif (g == mx):
      hue = 60 * ((b - r) / (mx - mn)) + 120
    elif(b == mx):
      hue = 60 * ((r - g) / (mx - mn)) + 240

    if (hue > 360):
      hue %= 360

    if (hue < 0):
      hue += 360

    return int(Decimal(str(hue)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

def get_RGB_from_hex(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def get_RGB_from_color_code(color_code):
    hex = color_code.lstrip('#')
    return get_RGB_from_hex(hex)


def get_color_name_from_RGB(rgb):

    if(is_grey_RGB(rgb, 30)):
        if(is_black_RGB(rgb, 0.3)):
            return COLOR_NAMES.BLACK
        if(is_white_RGB(rgb, 0.95)):
            return COLOR_NAMES.WHITE
        return COLOR_NAMES.GREY

    hue = get_hue_from_RGB(rgb)
    color_name = get_name_from_hue(hue)

    return color_name

def get_name_from_hue(hue):
    if 0 <= hue <= 15:
        return COLOR_NAMES.R
    elif 15 < hue <= 45:
        return COLOR_NAMES.O
    elif 45 < hue <= 75:
        return COLOR_NAMES.Y
    elif 75 < hue <= 105:
        return COLOR_NAMES.YG
    elif 105 < hue <= 135:
        return COLOR_NAMES.G
    elif 135 < hue <= 165:
        return COLOR_NAMES.BG
    elif 165 < hue <= 195:
        return COLOR_NAMES.LB
    elif 195 < hue <= 225:
        return COLOR_NAMES.B
    elif 225 < hue <= 255:
        return COLOR_NAMES.DB
    elif 255 < hue <= 285:
        return COLOR_NAMES.BV
    elif 285 < hue <= 315:
        return COLOR_NAMES.V
    elif 315 < hue <= 345:
        return COLOR_NAMES.VR
    elif 345 < hue <= 360:
        return COLOR_NAMES.R
    
def get_saturation_from_RGB(rgb):
    mx = max(rgb)
    mn = min(rgb)
    saturation = (mx - mn) / mx

    return saturation
    
def get_brightness_from_RGB(rgb):
    mx = max(rgb)
    brightness = mx / 255

    return brightness

def is_similer_RGB(rgb1, rgb2, rng=10):
    [r1, g1, b1] = rgb1
    [r2, g2, b2] = rgb2

    return in_range(r1, r2, rng) and in_range(g1, g2, rng) and in_range(b1, b2, rng)

def is_grey_RGB(rgb, rng=10):
    [r, g, b] = rgb
    avarage = sum(rgb) / len(rgb)

    return in_range(avarage, r, rng) and in_range(avarage, g, rng) and in_range(avarage, b, rng)

def is_vivid_RGB(rgb, rng=0.7):
   saturation = get_saturation_from_RGB(rgb)
   return saturation >= rng

def is_black_RGB(rgb, rng=0.2):
   brightness = get_brightness_from_RGB(rgb)
   return brightness <= rng

def is_white_RGB(rgb, rng=0.8):
   brightness = get_brightness_from_RGB(rgb)
   return brightness >= rng

def in_range(num1, num2, rng):
    num1Exist = not num1 and not (num1 == 0)
    num2Exist = not num2 and not (num2 == 0)

    if (not num1Exist and num2Exist):
        return False
    if (num1Exist and not num2Exist):
        return False
    if (num1 == num2):
        return True

    diff = num1 - num2

    abst = abs(diff)
    return abst <= rng

def get_RGB_from_hue(hue):
    """
    get RGB params(ex. [255,255,255]) from hue degree.
    """
    mx = 255
    r, g, b = 0, 0, 0

    if hue is None or hue < 0:
      raise TypeError('invalid value')

    if 0 <= hue <= 60:
      r = mx
      g = math.floor(hue / 60 * mx)
    elif 60 < hue <= 120:
      r = math.floor((120 - hue) / 60 * mx)
      g = mx
    elif 120 < hue <= 180:
      g = mx
      b = math.floor((hue - 120) / 60 * mx)
    elif 180 < hue <= 240:
      g = math.floor((240 - hue) / 60 * mx)
      b = mx
    elif 240 < hue <= 300:
      r = math.floor((hue - 240) / 60 * mx)
      b = mx
    elif 300 < hue <= 360:
      r = mx
      b = math.floor((360 - hue) / 60 * mx)

    [r, g, b] = map(lambda n: n if 0 <= n <= 255 else 0, [r, g, b])

    return [r, g, b]

def get_color_code_from_rgb(rgb):
    [r, g, b] = rgb
    return '#%02x%02x%02x' % (r, g, b)

def get_color_code_by_color_name(name):
    value = '#000000'

    for element in COLOR_NAMES:
      if(name == element.value): value = COLOR_CODES[element.name].value

    return value
   

def get_color_code_average(color_code_arr):
  hex_arr = [code.replace('#', '') for code in color_code_arr]
  hex_average = get_hex_average(hex_arr)
  color_code = '#' + hex_average.replace('0x', '').zfill(6)

  return color_code

def get_hex_average(hex_arr):
  total_oct = 0
  for _hex in hex_arr:
      total_oct += int(_hex, 16)
  average_oct = math.floor(total_oct / len(hex_arr))

  return hex(average_oct)

def get_base_color_code():
    print(get_color_code_from_rgb(get_RGB_from_hue(0)))
    print(get_color_code_from_rgb(get_RGB_from_hue(30)))
    print(get_color_code_from_rgb(get_RGB_from_hue(60)))
    print(get_color_code_from_rgb(get_RGB_from_hue(90)))
    print(get_color_code_from_rgb(get_RGB_from_hue(120)))
    print(get_color_code_from_rgb(get_RGB_from_hue(150)))
    print(get_color_code_from_rgb(get_RGB_from_hue(180)))
    print(get_color_code_from_rgb(get_RGB_from_hue(210)))
    print(get_color_code_from_rgb(get_RGB_from_hue(240)))
    print(get_color_code_from_rgb(get_RGB_from_hue(270)))
    print(get_color_code_from_rgb(get_RGB_from_hue(300)))
    print(get_color_code_from_rgb(get_RGB_from_hue(330)))
