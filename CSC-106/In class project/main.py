import image

def main():
    # Load an image from somewhere online
    pic = image.Pic('https://cs.union.edu/~striegnk/athens_2009.jpg')
    pic1 = image.Pic("https://process.images.nathab.com/A6dTpd53SmIg0pBfJJhgAz/resize=width:864/quality=value:60/cache=expiry:31536000/compress/https://www.nathab.com/uploaded-files/AdobeStock_115649942.jpg")
    #pic = image.Pic('https://www.planetware.com/photos-large/JPN/japan-mt-fuji-and-cherry-blossoms.jpg')
    # Modify our image
    print("Modifying image... ")
    
    blur(pic1, 8)
    
    print("Done modifying image")
    print("-------------------")
   
    # Save the image 
    pic1.save_image("myImage-blur.jpeg")
  

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
  

def greyscale(pic):
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
          average_rgb = int((red + green + blue) / 3) 
          
          pixel.red = average_rgb
          pixel.green = average_rgb
          pixel.blue = average_rgb
          
          # Finally, reset the pixel stored at that spot
          pic.pixels[row][col] = pixel
    

def greyscale_spot(pic, row1, col1, row2, col2):
    # Go through each row and column
    
   
    for row in range(row1, row2):
        for col in range(col1, col2):
          # Gets a pixel at row/col
          pixel = pic.pixels[row][col]
          
          
          # Get the RGB values of this pixel
          red = pixel.red 
          green = pixel.green
          blue = pixel.blue 
          
          # Resave them by altering the red 
          average_rgb = int((red + green + blue) / 3) 
          
          pixel.red = average_rgb
          pixel.green = average_rgb
          pixel.blue = average_rgb
          
          # Finally, reset the pixel stored at that spot
          pic.pixels[row][col] = pixel

def mirror_half(pic):
    for row in range(pic.height):
        for col in range(int(pic.width/2), pic.width):
            # Gets a pixel at row/col
            pixel = pic.pixels[row][col]
            alt_pixel = pic.pixels[row][-col]
            
            # Get the RGB values of this pixel
            red = pixel.red
            green = pixel.green
            blue = pixel.blue

            alt_pixel.red = red
            alt_pixel.green = green
            alt_pixel.blue = blue

            pic.pixels[row][col] = alt_pixel


def blur(pic,window): 
    for row in range(pic.height):
        for col in range(pic.width):
            adj_red = 0
            adj_green = 0 
            adj_blue = 0 
            
            current_pixel  = pic.pixels[row][col]
            
            for adj in range(window):
                adj_pixel = pic.pixels[row][col - adj]
                

                adj_red +=  adj_pixel.red
                adj_green += adj_pixel.green
                adj_blue += adj_pixel.blue 
        
            current_pixel.red = int((adj_red + current_pixel.red) / window )
            current_pixel.green = int((adj_green + current_pixel.green) / window) 
            current_pixel.blue = int((adj_blue + current_pixel.blue) / window)

            pic.pixels[row][col] = current_pixel

            
main()
