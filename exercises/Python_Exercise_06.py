'''
Write a function named isLandscape that takes 2 numbers (image width and height) as arguments and returns Landscape
if the image width is higher than height, otherwise returns Portrait.
'''

def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"

# Example 01
width = 1920
height = 1080
print(isLandscape(width, height))

# Example 02
width = 1920
height = 2400
print(isLandscape(width, height))