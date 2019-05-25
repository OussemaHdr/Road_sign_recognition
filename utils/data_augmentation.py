from PIL import Image, ImageFilter, ImageChops
import os

#prints number of pic in every folder
labels = os.listdir(".../data/train")
for label in labels: 
	number_files = len(os.listdir(".../data/train/" + label))
	print ("number of files in ", label, number_files) 
	
def augment_data(label_path):
	label = label_path.split('/')[-1]
	if label == "120":
		files = os.listdir(label_path)
		for file in files:
			file_name = file.split(".")[0]
			file_ext = file.split(".")[1]
			img = Image.open(label_path + "/" + file)
			img_rotate_90 = img.rotate(90)
			img_rotate_90.save(label_path + "/" + file_name + "rotate_90." + file_ext)
	if label == "Stop":
			files = os.listdir(label_path)
			for file in files:
				file_name = file.split(".")[0]
				file_ext = file.split(".")[1]
				img = Image.open(label_path + "/" + file)
				img_rotate_90 = img.rotate(90)
				img_rotate_120 = img.rotate(120)
				img_rotate_90.save(label_path + "/" + file_name + "rotate_90." + file_ext)
				img_rotate_120.save(label_path + "/" + file_name + "rotate_120." + file_ext)
	if label == "Right":
			files = os.listdir(label_path)
			for file in files:
				file_name = file.split(".")[0]
				file_ext = file.split(".")[1]
				img = Image.open(label_path + "/" + file)
				img_enhance = img.filter(ImageFilter.EDGE_ENHANCE())
				img_edge = img.filter(ImageFilter.FIND_EDGES())
				img_enhance.save(label_path + "/" + file_name + "enhance." + file_ext)
				img_edge.save(label_path + "/" + file_name + "edge." + file_ext)
	if label == "Left":
			files = os.listdir(label_path)
			for file in files:
				file_name = file.split(".")[0]
				file_ext = file.split(".")[1]
				img = Image.open(label_path + "/" + file)
				img_enhance = img.filter(ImageFilter.EDGE_ENHANCE())
				img_edge = img.filter(ImageFilter.FIND_EDGES())
				img_gaussian = img.filter(ImageFilter.GaussianBlur(radius = 3))
				img_invert = ImageChops.invert(img)
				img_enhance.save(label_path + "/" + file_name + "enhance." + file_ext)
				img_edge.save(label_path + "/" + file_name + "edge." + file_ext)
				img_gaussian.save(label_path + "/" + file_name + "gaussian." + file_ext)
				img_invert.save(label_path + "/" + file_name + "invert." + file_ext)

for label in labels:
	print("augmenting data in ", label)
	label_path = "../data/train/" + label
	try:
		augment_data(label_path)
	except:
		print("bug in ", label)
