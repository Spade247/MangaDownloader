import shutil
import requests
from fpdf import FPDF
import os

# define the name of the directory to be created
path = "C:\\Users\\Spade\\Desktop\\Manga"
try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)

# num = 1
# pgNum = '0'
# chapter = []
# url = None
# while num < 18:
#     if num < 10:
#         url = 'https://i1.wp.com/jaiminisbox.com/reader/content/comics/one-piece-2_58650da78040f/933-0-a-samurai-s-mercy_5c6645a03c1bb/'+str(pgNum)+str(num)+'.png?quality=100&strip=all'
#     else:
#         url = 'https://i1.wp.com/jaiminisbox.com/reader/content/comics/one-piece-2_58650da78040f/933-0-a-samurai-s-mercy_5c6645a03c1bb/'+str(num)+'.png?quality=100&strip=all'

#     response = requests.get(url, stream=True)
#     with open('OP-933-Pg-'+str(num)+'.png', 'wb') as out_file:
#         shutil.copyfileobj(response.raw, out_file)
#     chapter.append('OP-933-Pg-'+str(num)+'.png')
#     num+=1

# pdf = FPDF()
# # pdf.add_page()
# # pdf.image('OnePiece.png', 10, 8, 33)
# # pdf.output("manga.pdf", "F")

# for image in chapter:
#     pdf.add_page()
#     pdf.image(image, x = None, y = None, w = 200, h = 250)
# pdf.output("OP-Chapter-933.pdf", "F")



num = 1
count = 1
missedPages = []
chapLen = 81
pgNum = '0'
chapter = []
url = None
while num < chapLen:
    if num < 10:
        url = 'https://i0.wp.com/jaiminisbox.com/reader/content/comics/edens-zero_5b2ff035693d7/1-0-in-a-sakura-filled-sky_5b30d6852896d/'+str(pgNum)+str(num)+'.png?quality=100&strip=all'
    else:
        url = 'https://i0.wp.com/jaiminisbox.com/reader/content/comics/edens-zero_5b2ff035693d7/1-0-in-a-sakura-filled-sky_5b30d6852896d/'+str(num)+'.png?quality=100&strip=all'

    response = requests.get(url, stream=True)
    if response.headers['Content-Type'] == 'image/png':

        with open(str(path)+'/Edens-Zero-Pg-'+str(num)+'.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            print("Page "+str(num)+"/"+str(chapLen)+" downloaded.")
        chapter.append('Edens-Zero-Pg-'+str(num)+'.png')
    else:
        missedPages.append('Edens-Zero-Pg-'+str(num)+'.png')
    num+=1

pdf = FPDF()
# pdf.add_page()
# pdf.image('OnePiece.png', 10, 8, 33)
# pdf.output("manga.pdf", "F")
for page in missedPages:
    print("missed page: "+ page)

for image in chapter:
    pdf.add_page()
    pdf.image(image, x = None, y = None, w = 200, h = 250)
    print("Page "+str(count)+"/"+str(chapLen)+" added.")
    count+=1
pdf.output(str(path)+"Edens-Zero-Chapter-01.pdf", "F")