from PIL import Image
import pandas as pd


imageName = str(input("Please Input Image File name or relative path"))
def column(matrix, i): # to chop out just the grayscale color pixel value
    return [row[i] for row in matrix]
def binary(array): #pixel value ranges from 0-255, which is baised here to be 0/1
    binarr=[]
    for pixel in array:
        if(pixel<(255/2)):
            binarr.append(0)
        else:
            binarr.append(1)
    return binarr

img = Image.open(imageName).convert('LA') #loading image file as grayscale image
pix =list(img.getdata()) # variable is of the form (pixelValue,225)
justPixelValue = column(pix,0)# data modified to be linear
binary1darr = binary(justPixelValue) # converted to binary
#setting up dataframe to be inserted in excel file
yourData = pd.DataFrame(binary1darr,columns = ['pixel binary values'])
#setting excel writter
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

# Write your DataFrame to a file     
yourData.to_excel(writer, 'Sheet1')

# Save the result 
writer.save()
print(binary1darr)# remove this line in production

