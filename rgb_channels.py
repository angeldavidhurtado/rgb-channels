from PIL import Image
import itertools

path_img = input("Path img: ")
img = Image.open( path_img )
width, heihgt = img.size
canvas = Image.new( 'RGB', (width, heihgt) )

# channel permutation
channel_permutation = list(itertools.permutations(['r', 'g', 'b']))
for permutation in channel_permutation:
	for x in range( width ):
		for y in range( heihgt ):
			r, g, b = img.getpixel( (x, y) )
			channels = { "r":r, "g":g, "b":b }
			canvas.putpixel( (x, y), (
				channels[permutation[0]],
				channels[permutation[1]],
				channels[permutation[2]]
			) )
	canvas.save( permutation[0] + permutation[1] + permutation[2] + ".png" )

# max
for x in range( width ):
	for y in range( heihgt ):
		r, g, b = img.getpixel( (x, y) )
		m = max(r, g, b)
		canvas.putpixel( (x, y), (m, m, m) )
canvas.save( "max.png" )

# min
for x in range( width ):
	for y in range( heihgt ):
		r, g, b = img.getpixel( (x, y) )
		m = min(r, g, b)
		canvas.putpixel( (x, y), (m, m, m) )
canvas.save( "min.png" )

# average
for x in range( width ):
	for y in range( heihgt ):
		r, g, b = img.getpixel( (x, y) )
		average = round(sum([r, g, b]) / 3)
		canvas.putpixel( (x, y), (average, average, average) )
canvas.save( "average.png" )
