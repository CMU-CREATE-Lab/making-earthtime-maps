import matplotlib.colors as mp_colors
def hex_to_rgb(hex_string):
   rgb = mp_colors.hex2color(hex_string)
   r,g,b = tuple([int(255*x) for x in rgb])
   return (r,g,b)

c1 = "#52b947"
#c2 = f3ec19
#c3 = f57e20
#c4 = ed1f24
#c5 = 991b4f

print(hex_to_rgb(c1))