import requests
from bs4 import BeautifulSoup
import csv

# exlist = []
# flist = []
def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://www.makemydelivery.com/shop/page/' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    '''paras = soup.findAll('p', attrs={'class' : "name product-title"})
    for para in paras:
        print para.find('a').get_text().encode('utf-8')'''


    text= soup.find('div', attrs={'class' : "box-text"})
    
    
    title= text.find('div', attrs={'class' : "title-wrapper"})
    name=title.find('a').get_text().encode('utf-8')

    print name

    price=text.find('span', attrs={'class' : "price"}).findAll('span')

    l = len(price)

    if l == 4:

        old=price[0]
        new=price[2]
        old_price=old.get_text().encode('utf-8')
        new_price=new.get_text().encode('utf-8')
        print old.get_text().encode('utf-8')
        print new.get_text().encode('utf-8')

    elif l == 2:


        new = price[0]

        print "undefined"
        print new.get_text().encode('utf-8')

    else:
        print "nothing "

        

            

            
        '''price= soup.find('div', attrs={'class' : "price-wrapper"}).find('span', attrs={'class':"price"}).findAll('span')
    #for price in price_list:
    p1= price[0]
    print p1.get_text().encode('utf-8')
    p2=price[2]
    print p2.get_text().encode('utf-8')'''


    
        
    

       
    page += 1

    

    fieldnames=['name','old','new']
    with open ('filename.csv','w') as file:
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name':name,'old':old_price,'new':new_price})


            

       



trade_spider(1)

# fieldnames=['name','old','new']
# with open ('filename3.csv','w') as file:
#     writer=csv.DictWriter(file,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'name':name,'old':old,'new':new})
