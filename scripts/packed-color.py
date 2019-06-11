# packed-color.py
# turns hex string color into packed color (int)
import matplotlib.colors as mp_colors

hexArr = ["#52b947", "#f3ec19", "#f57e20","#ed1f24","#991b4f"]

def hex_to_rgb(hex_string):
   rgb = mp_colors.hex2color(hex_string)
   r,g,b = tuple([int(255*x) for x in rgb])
   return (r,g,b)

def rgb_to_pack_color(color):
   return color[0] + color[1] * 256.0 + color[2] * 256.0 * 256.0;

def hex_to_pack_color(hex_string):
  return rgb_to_pack_color(hex_to_rgb(hex_string))

def unpack_color(f):
   b = math.floor(f / 256.0 / 256.0)
   g = math.floor((f - b * 256.0 * 256.0) / 256.0)
   r = math.floor(f - b * 256.0 * 256.0 - g * 256.0)
   return [r, g, b]

# convert all colors in hexArr to packed colors
for i in range(len(hexArr)):
  print(hex_to_pack_color(hexArr[i]))