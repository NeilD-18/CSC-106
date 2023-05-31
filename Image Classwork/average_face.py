import image

''' This file is the template for averaging faces'''
def main():
    # A list of face images that are available 
    # Face images of men
    face_files = ["alexander.jpg", "alex.jpg", "ambroz.jpg", "alfred.jpg"]
    # Face images of women
    # face_files = ["zelmira.jpg","zita.jpg", "zlata.jpg", "zlatica.jpg", "zora.jpg"]
    base_url = "http://eg.bucknell.edu/~emp017/teaching/203/faces/"

    # Load a list of pics
    face_pics = []
    for face_path in face_files:
        face_pics.append(image.Pic(base_url + face_path))

    print("Modifying images... ")
    average_pics(face_pics)
    # Save the image 
    face_pics[0].save_image("average.jpeg")
    print("Done modifying images")
    print("-------------------")

def average_pics(faces):
    ''' 
    Takes a list of face images and modifies the first 
    image in the list to be the average of the entire list. 
    '''
    # We want to modify the first face, so save it in a variable
    first_face = faces[0]

    # The pics all have the same dimensions, so we'll just use the first
    for row in range(first_face.height):
        for col in range(first_face.width):
            
            total_current_pixel_red = 0
            total_current_pixel_green = 0 
            total_current_pixel_blue = 0 
            
            first_face_pixel = first_face.pixels[row][col] 
           
            for pic in range(0,len(faces)):
                current_pixel = faces[pic].pixels[row][col]

                #total values of red, green, and blue for the same pixel for each image
                total_current_pixel_red += current_pixel.red 
                total_current_pixel_green += current_pixel.green
                total_current_pixel_blue += current_pixel.blue

            avg_red = int(total_current_pixel_red / len(faces))
            avg_green = int(total_current_pixel_green / len(faces))
            avg_blue = int(total_current_pixel_blue / len(faces))

            first_face_pixel.red = avg_red
            first_face_pixel.green = avg_green
            first_face_pixel.blue = avg_blue


            first_face.pixels[row][col] =  first_face_pixel 


            
            # Get the average RGB value at row/col for all our pics
            # We'll need go through each face pic in faces to do this 
            # After we get the RGB average, apply it to row/col in first_face

            # TIP: This looks similar to blur
             # delete this line when you write your code
      

main()
