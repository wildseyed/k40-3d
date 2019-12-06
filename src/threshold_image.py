#!/usr/bin/python
"""
    K40 Whisperer Proposed Addition - Layered Bitmap Sample Code
	By John Cabrer wildseyed@gmail.com
	
    What does it do?

    This bit of code demonstrates thresholding of a height map image,
    where intensity of the pixel value represents elevation,
    to produce two or more layers that can be raster engraved one over the
    others to produce a 3D engrave result in acrylic or wood, from controllers
    that do not support power modulation of the beam. It can also be used to produce
    lighter and darker burns in wood engraving. 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import cv2

layers = 16 # Number of gradient separations to generate.
threshold_jump = 256 / layers
threshold = 0
titles = []
images = []

img = cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)

for i in range(layers):
	threshold = threshold + threshold_jump
	titles.append("Range 0 - " + str(threshold))
	#images.append(cv2.threshold(img,threshold,255,cv2.THRESH_BINARY_INV)[1]) # Used for 3D height map rater engraving where white areas are engraved the deepest.
	images.append(cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)[1]) # Used for greyscale raster engraving of pictures where black areas receive more burn.
	cv2.imwrite('img'+str(i)+'.bmp',images[i])

for i in range(layers):
	cv2.imshow("Figure",images[i])
	cv2.waitKey(0)