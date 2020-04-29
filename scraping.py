from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=4ec5718d-76be-4247-beb7-ded45e0a51c5&as-searchtext=iphone"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll("div", {"class" : "_3O0U0u"})
#print(len(containers))

#print(soup.prettify(containers[0]))

container = containers[0]
#print(container.div.img["alt"])

price = container.findAll("div", {"class" : "col col-5-12 _2o7WAb"})
#print(price[0].text)

ratings = container.findAll("div", {"class" : "hGSR34"})
#print(ratings[0].text)

filename = "products.csv"
f = open(filename,"w")

headers = "Product_Name,Pricing,Rating\n"
f.write(headers)

for container in containers:
    product_name = container.div.img['alt']

    price_container = container.findAll("div", {"class" : "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class" : "hGSR34"})
    rating = rating_container[0].text

    # print("product name: " + product_name)
    # print("Price: " + price)
    # print("Ratings: " + rating)

    #string parsing
    trim_price = ''.join(price.split(','))
    #print(trim_price)
    rm_rupee = trim_price.split("₹")
    #print(rm_rupee)
    add_rs_price = "Rs." + rm_rupee[1]
    #print(add_rs_price)
    final_price = add_rs_price[0:]
    #print(final_price)

    print(product_name.replace(",", "|") + "," + final_price + "," + rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + rating + "\n")

f.close()

