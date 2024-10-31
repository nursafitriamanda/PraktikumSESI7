import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = 'singa2.jpg'
image = img.imread(path)
height, width = image.shape[:2]

horizontal = np.flip(image, axis=1)  
vertical = np.flip(image, axis=0)    
mirrored_image = np.flip(image, axis=(0, 1))  


plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1, 4, 2)
plt.imshow(horizontal)
plt.title("Horizontal Mirror")

plt.subplot(1, 4, 3)
plt.imshow(vertical)
plt.title("Vertical Mirror")

plt.subplot(1, 4, 4)
plt.imshow(mirrored_image)
plt.title("Horizontal + Vertical Mirror")


img.imwrite('mirrored_image.jpg', mirrored_image)
plt.show()