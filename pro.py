from PIL import Image
import pandas as pd
def column(matrix, i):
    return [row[i] for row in matrix]
def binary(array):
    binarr=[]
    for pixel in array:
        if(pixel<(255/2)):
            binarr.append(1)
        else:
            binarr.append(1)
    return binarr
def imbin(array):
    binarr=[]
    for pixel in array:
        if(pixel[0]<(255/2)):
            binarr.append((0,pixel[1]))
        else:
            binarr.append((255,pixel[1]))
    return binarr


img = Image.open('image.jpg').convert('LA')
img.save('greyscale.png')
pix =list(img.getdata())
justPixelValue = column(pix,0)
binary1darr = binary(justPixelValue)
bin2darr= imbin(pix)
im2 = Image.new('LA', img.size)
im2.putdata(bin2darr)
im2.save('magic.png')
yourData = pd.DataFrame(binary1darr,columns = ['pixel binary values'])
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

# Write your DataFrame to a file     
yourData.to_excel(writer, 'Sheet1')

# Save the result 
writer.save()
print(bin2darr)

