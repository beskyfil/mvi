from os import listdir
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from numpy import savez_compressed
 
# load all images in a directory into memory
def load_images(path, size=(256,256)):
	data_list = list()
	for filename in listdir(path):
		# load and resize the image
		pixels = load_img(path + filename, target_size=size)
		pixels = img_to_array(pixels)
		data_list.append(pixels)
	return asarray(data_list)

path = 'data/'
# load dataset A
dataA = load_images(path + 'A/')
print('Loaded dataA: ', dataA.shape)
# load dataset B
dataB = load_images(path + 'B/')
print('Loaded dataB: ', dataB.shape)
# save
filename = 'data_256.npz'
savez_compressed(filename, dataA, dataB)
print('Saved dataset: ', filename)
