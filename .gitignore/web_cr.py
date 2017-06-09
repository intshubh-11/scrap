import requests
from bs4 import BeautifulSoup
import csv

names=[]
op=[]
np=[]

def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://www.makemydelivery.com/shop/page/' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    


    box_text= soup.findAll('div', attrs={'class' : "box-text"})
    
    for text in box_text:
        title= text.find('div', attrs={'class' : "title-wrapper"})
        name=title.find('a').get_text().encode('utf-8')

        # print name

        price=text.find('span', attrs={'class' : "price"}).findAll('span')

        l = len(price)

        if l == 4:

            old=price[0]
            new=price[2]
            old_price=old.get_text().encode('utf-8')
            new_price=new.get_text().encode('utf-8')
            # print old.get_text().encode('utf-8')
            # print new.get_text().encode('utf-8')

        elif l == 2:


            new = price[0]
            new_price=new.get_text().encode('utf-8')
            old_price="undefined"

            # print "undefined"
            # print new.get_text().encode('utf-8')

        else:
            print "nothing "
       
       
        # slist=[name,old_price,new_price]

        names.append(name)
        op.append(old_price)
        np.append(new_price)

        # flist.append(slist)
        
        #writer.writerow({'name':name,'old':old_price,'new':new_price})

    
    page += 1







trade_spider(1)

fieldnames=['name','old','new']
with open ('filename15.csv','wb') as f:
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    # writer.writeheader()
    for i in range(len(names)):
        writer.writerow({'name':names[i],'old':op[i],'new':np[i]})


