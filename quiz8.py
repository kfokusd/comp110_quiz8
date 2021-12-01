import image

##
## Function: getRGB_diff()
## - Returns an average of RGB value between two pixels (arguments) , pix1, and pix2.
##
def getRGB_diff(pix1, pix2):
    (r1, g1, b1) = pix1.getColorTuple()
    (r2, g2, b2) = pix2.getColorTuple()
    avg = ( abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2) ) / 3
    return avg
# End of getRGB_diff

##
## Function: weird_edge_detection()
## - Parameter, img, is an image object
## - Detects edge (surrounding pixel - horizontal and vertical) and if the average surrounding RGB difference is less than 10, 
##   then set the pixel to black.  Otherwise, set it to white
## - Change the pixel of the parameter, img, directly  (i.e., no need to return)
##
def weird_edge_detection(img):
    black_pix = image.Pixel(0, 0, 0)
    white_pix = image.Pixel(255, 255, 255)
    ##
    ## TODO: Implement your code here
    ##
## End of weird_edge_detection()

##
## Function: rotate_left()
## - Parameter, img, is an image object
## - Rotate the image object to left 90 degree and return the new image 
##
def rotate_left(img):
    nWidth = img.getWidth()
    nHeight = img.getHeight()

    ##
    ## TODO: Implement your code here
    ##
    return img          ## TODO: You will need to modify this line
## End of rotate_left()

##
## Please do NOT change the following code ##
##
img = image.Image("updown_babyyoda.jpg")

newimg = rotate_left(img)
newimg = rotate_left(newimg)

weird_edge_detection(newimg)

# Create a window to hold the image
win = image.ImageWin(newimg.getWidth(), newimg.getHeight())
newimg.draw(win)
win.exitonclick()