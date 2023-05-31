import image

def main():
    # Load an image from somewhere online
    #pic = image.Pic('https://cs.union.edu/~striegnk/athens_2009.jpg')
    pic = image.Pic('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/NottMemorialPano.jpg/250px-NottMemorialPano.jpg')
    # Modify our image
    print("Modifying image... ")
    boost_red(pic)
    print("Done modifying image")
    print("-------------------")
    # Save the image 
    pic.save_image("myImage-red.jpeg")
  

# BOOST THE RED - DON'T DELETE
# This is ONE example of a function that changes a picture. 
# You will create several other functions that look similar to this. 
def boost_red(pic):
    # Go through each row and column
    for row in range(pic.height):
        for col in range(pic.width):
            # Gets a pixel at row/col
            pixel = pic.pixels[row][col]
          
            # Get the RGB values of this pixel
            red = pixel.red 
            green = pixel.green
            blue = pixel.blue 
          
            # Resave them by altering the red 
            pixel.red = red + 100
            pixel.green = green 
            pixel.blue = blue
          
            # Finally, reset the pixel stored at that spot
            pic.pixels[row][col] = pixel
  

main()
