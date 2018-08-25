import requests
import os
import sys
from PIL import Image


def compressMe(file):

	filepath = os.path.join(os.getcwd(), file)
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath)
	dim = picture.size
	#print file, dim
	#set quality= to the preferred quality. 
	#I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
	picture.save("Mini_"+file,"JPEG",optimize=True,quality=5) 
	
	newsize = os.stat(os.path.join(os.getcwd(),"Mini_"+file)).st_size
	percent = (oldsize-newsize)/float(oldsize)*100
	
	#print "File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent)

	return "Mini_"+file

file_name = 'ESV Scripture Journal: 2 Corinthians'

import re
file_name = re.sub("\\s","_"," ".join(re.sub("[^a-zA-Z\\d\\s]", " ",file_name).split()))

print(file_name)

response = requests.get('http://cway.to/1QbEUbv')

with open(file_name + '.pdf', 'wb') as f:
    f.write(response.content)

from pdf2image import convert_from_path

pages = convert_from_path(file_name + '.pdf', 500) #dpi
file_names = mini_file_names =''
for q,page in enumerate(pages,1):
    page.save(file_name + '_' + str(q+1) + '.jpg', 'JPEG')
    
    file_names += ';' + file_name + '_' + str(q+1) + '.jpg'
    mini_file_names += compressMe(file_name + '_' + str(q+1) + '.jpg')





