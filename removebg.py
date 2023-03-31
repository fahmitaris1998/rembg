from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title="Select image file")
outputPath = easygui.filesavebox(title="Save file to..")

input = Image.open(inputPath)
print(inputPath)
print(input)
output = remove(input)
output.save(outputPath)

print("Python ni boss bisa")

