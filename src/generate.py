from PIL import Image
import os
import sys

dir = os.path.dirname(__file__)
img_path = os.path.join(dir, "img/img.png")

def hidden_keys(text):
	b_text_arr = [bin(ord(t)) for t in text]
	keys = []
	index = 0
	for uc in b_text_arr:
		index = 0
		for c in list(str(uc)):
			if index > 1:
				keys.append(int(c))
			index = index + 1

	return keys


def generate(text):
	keys = hidden_keys(text)
	im = Image.open(img_path)
	rgb_im = im.convert("RGB")
	im_size = rgb_im.size

	im2 = Image.new("RGB", im_size)

	i = 0
	for x in range(im_size[0]):
		for y in range(im_size[1]):
			r, g, b = rgb_im.getpixel((x, y))
			if i < len(keys):
				new_rb = bin(r)[:-1] + str(keys[i])
				r = int(new_rb, 2)
				i = i + 1

			if i < len(keys):
				g = int(bin(g)[:-1] + str(keys[i]), 2)
				i = i + 1

			if i < len(keys):
				b = int(bin(b)[:-1] + str(keys[i]), 2)
				i = i + 1

			im2.putpixel((x,y),(r,g,b,0))

	im2.save(os.path.join(dir, "img/output.png"))

if __name__ == '__main__':
	args = sys.argv
	generate(args[1])
