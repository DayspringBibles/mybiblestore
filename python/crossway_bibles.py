# - *- coding: utf- 8 - *-
import requests
from lxml import html
import re
from pdf2image import convert_from_path
import os
from PIL import Image

class bible_properties(object):
    def __init__(self,url):
        self.tree = html.fromstring(requests.get(url).content)

        keys = [a.strip() for a in self.tree.xpath('//div/table/tr/td[1]/text()')][:-1]
        values = [a.strip() for a in self.tree.xpath('//div/table/tr/td[2]/text()')]

        self.dict = dict(zip(keys+values[len(keys):], values))
        

    def in_stock(self):
        try:
            return self.tree.xpath('//div[@id="add-to-cart-details"]/p/text()')[0].strip()
        except:
            return 'error'

    def price(self):
        try:
            return self.tree.xpath('//div[@id="add-to-cart-details"]/p/text()')[2].strip()
        except:
            return 'error'

    def price_value(self):
        try:
            return float(self.tree.xpath('//div[@id="add-to-cart-details"]/p/text()')[2].strip()[1:])
        except:
            return 999

    def title(self):
        try:
            return self.tree.xpath('//div[@class="product-detail"]/div/h1/text()')[0].replace(u'\u2013','-').encode('ascii','ignore')
        except:
            return 'error'

    def description(self):
        try:
            return self.tree.xpath('string(//div[@class="product-detail"][2]/div[2]/p)').replace(u'\xa0',u' ').replace(u'\u2019','\'').replace(u'\u2013','-').encode('ascii','ignore')
        except:
            return 'error'
        
    def pdf_url(self):
        try:
            return self.tree.xpath('//div[@id="related-media"]/a')[0].attrib['href']
        except:
            try:
                #print "media pack " + self.tree.xpath('//a[text()="Download Media Pack"]')[0].attrib['href']
                #return self.tree.xpath('//a[text()="Download Media Pack"]')[0].attrib['href']
                return None
            except:
                return None

    def pages(self):
        try:
            return self.dict['Page Count:']
        except:
            return 'error'
        
    def size(self):
        try:
           return re.match("(\\d+(\\.\\d+)?)", self.dict['Trim Size:'].split('x')[0].strip()).group(0),re.match("(\\d+(\\.\\d+)?)", self.dict['Trim Size:'].split('x')[1].strip()).group(0)
        except:
           return 'error'
        
    def font_size(self):
        try:
            return re.match("(\\d+(\\.\\d+)?)", self.dict['Type Size:']).group(1)
        except:
            return None        

    def columns(self):
        try:
            return self.dict['Page Layout:']
        except:
            return 'Double Column'
        
    def binding(self):
        try:
            return self.dict['Sewn Binding']
        except:
            return 'error'
        
    def words_of_Christ(self):
        try:
            return self.dict['Words of Christ Red']
        except:
            return 'Words of Christ Black'

    def reference(self):
        try:
            #print("reference")
            reference =  re.match("ref", self.title(self)).group(1)
            return True
        except:
            return False

    def study(self):
        try:
            #print("study")
            study =  re.match("study", self.title(self)).group(1)
            return True
        except:
            return False      


class image_properties(object):
    def __init__(self,url,name):

        if url == None:
            print "bad url"
            return None
        # name PDF
        file_name = re.sub("\\s","_"," ".join(re.sub("[^a-zA-Z\\d\\s]", " ",name).split()))

        # save PDF
        with open(file_name + '.pdf', 'wb') as f:
            f.write(requests.get(url).content)

        pages = convert_from_path(file_name + '.pdf', 1000) #dpi
        
        self.file_names_array = self.mini_file_names_array = self.thumb_file_names_array = ''
        
        for q,page in enumerate(pages,1):
            
            file = file_name + '_' + str(q) + '.jpg'

            page.save(file, 'JPEG')
            
    
            print(file)

            self.file_names_array = self.file_names_array + file + ';'
            self.mini_file_names_array = self.mini_file_names_array + self.compressMe(file) + ';'
            if q == 1:
                self.thumb_file_names_array = self.thumb_file_names_array + self.thumbMe(file) + ';'    

        os.remove(file)

    def compressMe(self,file):

        filepath = os.path.join(os.getcwd(), file)
        oldsize = os.stat(filepath).st_size
        picture = Image.open(filepath)
        #dim = picture.size
        #print file, dim
        #set quality= to the preferred quality. 
        #I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
        picture.save("mini_"+file,"JPEG",optimize=True,quality=5) 
        
        #newsize = os.stat(os.path.join(os.getcwd(),"Mini_"+file)).st_size
        #percent = (oldsize-newsize)/float(oldsize)*100
        
        #print "File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent)

        return "mini_"+file

    def thumbMe(self,file):
        picture = Image.open(file)
        # convert to thumbnail image
        picture.thumbnail((250, 250), Image.ANTIALIAS)
        # don't save if thumbnail already exists
        if file[0:2] != "thumb_":
            # prefix thumbnail file with T_
            picture.save("thumb_" + file, "JPEG")
        return "thumb_"+file

    def file_names(self):
        try:
            return self.file_names_array
        except:
            return None

    def mini_file_names(self):
        try:
            return self.mini_file_names_array

        except:
            return None
    def thumb_file_names(self):
        
        try:
            return self.thumb_file_names_array

        except:
            return None

# get list of all bibles from crossway.org
r = requests.get('https://www.crossway.org/bibles/?all=on')
tree = html.fromstring(r.content)
bible_url_details = ['https://www.crossway.org' + a.attrib['href'] for a in tree.xpath('//a[@class="thumb-cover"]')]

my_bibles =[]
i = 0

#bible_url_details = ['https://www.crossway.org/bibles/esv-large-print-compact-bible-tru-6/']
for url in bible_url_details:
    i+=1
    this_bible = bible_properties(url)
    print this_bible.title()

    if this_bible.in_stock() == 'In Stock' and this_bible.binding() =='Sewn Binding' and this_bible.price_value() < 100:
        
        #language, translation, columns, reference_bible, study_bible, verse_style, concordance, maps, width, height, size_range, source, price, labor, text, images, leadtime, name, keywords

        print(this_bible.pdf_url())
        my_bibles.append([
                            'EN',
                            'ESV',
                            this_bible.columns(),
                            this_bible.reference(),
                            this_bible.study(),
                            'verse style',
                            'concordance',
                            'maps',
                            this_bible.size()[0],
                            this_bible.size()[1],
                            'mid',
                            url,
                            this_bible.price(),
                            1,
                            this_bible.description(),
                            'img',
                            10,
                            this_bible.title(),
                            this_bible.pdf_url(),
                            this_bible.pages(),
                            this_bible.size(),
                            this_bible.font_size(),
                            this_bible.binding(),
                            this_bible.words_of_Christ()
                        ])

    #if i >6:
    #    break

bible_list = list(set([a[17] for a in my_bibles]))
final_bible_list = []
for bible in bible_list:
    bible_matches = [a for a in my_bibles if a[17] == bible]       
    current_bible = bible_matches[17]
    for a in bible_matches:
        print(float(a[12][1:]))
        if float(a[12][1:]) < float(current_bible[12][1:]):
            current_bible = a
            print(a[12])

    print a[18],a[17]
    images = image_properties(current_bible[18],current_bible[17])
    file_names = images.file_names()
    print(file_names)
    print(images.mini_file_names())
    print(images.thumb_file_names())

    final_bible_list.append(current_bible)
   
import csv    
with open('crossway_bible_data.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')

    for bible in final_bible_list:
        filewriter.writerow(bible)


