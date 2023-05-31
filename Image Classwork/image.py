from PIL import Image
import requests
from io import BytesIO


class Pic:

  def __init__(self, url):
    self.img = self.load_image(url)
    self.width = self.img.size[0]
    self.height = self.img.size[1]

    self.img_pix = self.img.load()
    self.pixels = self.pixels_to_list()

  def load_image(self, url):
    print("Loading image from the internet...")
    response = requests.get(url)
    img = Image.open( BytesIO(response.content) )
    print("Successfully loaded image")
    print("-------------------")
    return img

  def pixels_to_list(self):
    data = []
    for row in range(self.height):
      one_row = []
      for col in range(self.width):
        pix = self.img_pix[col, row]
        one_row.append( Pixel(row, col, pix[0], pix[1], pix[2]) )
      data.append(one_row)
    return data 

  def get_pixel(self, row, col):
    return self.pixels[row][col]

  def get_width(self):
    return self.width

  def get_height(self):
    return self.height

  def save_image(self, filename):
    print("Saving image... ")

    for x in range(self.width):
      for y in range(self.height):
        pix = self.pixels[y][x]
        self.img_pix[x, y] = (pix.red, pix.green, pix.blue)
    
    try:
      self.img.save(filename)
    except IOError:
      print("Cannot save image")
        
    print(filename, "now saved")


class Pixel:

  def __init__(self, row, col, r, g, b):
    self.row = row
    self.col = col
    self.red = r
    self.green = g
    self.blue = b
