from bs4 import BeautifulSoup 
import requests 
import json
import pandas as pd 
import streamlit as st 

#cat = "tv-audio-entertainment"

all_cat = ['makropropoint-19apr-to-2may','makropro-hottest-promotion','professional-solution','trending-items-to-sell','makro-housebrands'
           ,'meat','fish-seafood','fruit-vegetables','eggs-dairy-products','bakery-bakery-ingredients','beverages','condiments-sauces-puree',
           'frozen-appetizers','snacks-confectionery','dry-grocery','kitchen-dining',
           'electronic-appliances','furniture','hardware','health-beauty','household-supplies','luggage-bags','mom-baby','office-supplies','pet-supplies','tv-audio-entertainment','uniforms-clothings'
           ]

#cat = input("Enter your category name : ")
title_lis = []
barcode_lis = []
cat_lis = []
prod_lis = []
price_lis = []
unit_lis = []
quant_lis = []
image_lis = []
desc_lis = []
inv_quant_lis = []
for d in all_cat: 

    url = "https://www.makro.pro/en/c/{}".format(d)
    #res = requests.get("https://www.makro.pro/en/c/tv-audio-entertainment")
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    #print(soup.prettify())

    data = soup.find_all('script')
    ext_data = str(data[-1]).replace('<script id="__NEXT_DATA__" type="application/json">',"").replace('</script>','')
    print(ext_data)

    raw_data = json.loads(ext_data)
    print("-----------------------")
    #print(raw_data)

    #print(raw_data['props']['pageProps']['initialSearchResult']['hits'])


    for i in raw_data['props']['pageProps']['initialSearchResult']['hits']: 
        try:
            print(i['document'].keys())
            for j in i['document'].keys(): 
                
                if j == "title":
                    name = i['document'][j]
                    print(name)
                    title_lis.append(name)
                elif j == "categories":
                    cat = i['document']['categories'][0]
                    print(cat)
                    cat_lis.append(cat)     
                
                elif j == "displayPrice":
                    price = i['document'][j]
                    print(price)
                    price_lis.append(price)

                elif j == "id":
                    prod_id = i['document'][j]
                    print(prod_id)
                    prod_lis.append(prod_id)  

                elif j == "unitSize": 
                    unit_size = i['document'][j]
                    print(unit_size)
                    unit_lis.append(unit_size)

                elif j == "inventoryQuantity": 
                    quant = i['document'][j]
                    print(quant)
                    quant_lis.append(quant)       

                elif j == 'images': 
                    image = i['document'][j]
                    print(image)
                    image_lis.append(image)  

                elif j == 'shortDescription': 
                    desc = i['document'][j]
                    print(desc)
                    desc_lis.append(desc)
                

            #item = i['document'].keys()[7]
            #print(item)

            #name = i['document']['title']
            #print(name)
            #title_lis.append(name)

            #cat = i['document']['categories'][0]
            #print(cat)
            #cat_lis.append(cat)


            print("------")
        except: 
            pass

    #with open('raw_data.txt','w',encoding="utf-8") as f: 
    #    f.write(ext_data)

print(title_lis)
print(cat_lis)
print(prod_lis)

print(price_lis)
print(image_lis)
print(quant_lis)
print(unit_lis)
print(inv_quant_lis)
print(desc_lis)
df = pd.DataFrame()

df['Product Name'] = title_lis 
df['Category'] = cat_lis 
df['Product ID'] = prod_lis 
df['Price'] = price_lis 
df['Link'] = image_lis 
df['Quantity'] = quant_lis 
df['unit'] = unit_lis 
df['desc'] = desc_lis 

st.dataframe(df[:45])

st.success("ตัวอย่างข้อมูล 45 แถวแรก")
df.to_excel("Testx.xlsx")