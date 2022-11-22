import json
import requests
import pandas as pd
from scraper_api import ScraperAPIClient
categoryIds = [
    "100003109",
    "100003070",
    "509",
    "7",
    "44",
    "1509",
    "15",
    "1524",
    "26",
    "18",
    "66",
    "34",
    "1420",
]
catName = [
    "women-clothing",
    "men-clothing",
    "cellphones-telecommunications",
    "computer-office",
    "consumer-electronics",
    "jewelry-accessories",
    "home-garden",
    "luggage-bags",
    "toys-hobbies",
    "sports-entertainment",
    "beauty-health",
    "automobiles-motorcycles",
    "tools",
]


def getProducts(catId, page, catName):
    headers = {
  'authority': 'www.aliexpress.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,ar-SA;q=0.8,ar;q=0.7',
  'bx-v': '2.2.3',
  'cookie': 'xman_t=lFSCyul41Z/ra9uYkfwjaQ2GvdrRJgCuhjdqjUMkTQyW/xaLj3ubFfWxYB1Qw6WU; xman_f=0xTZRJeNCCnUex/Kkf/iIf4A+BOO4tDcJrdh1s0ATJh14s+L/uY2NWXt1QHSJrdnD0i+qkkDRO2vC80w6LogthhKXErU4cUdM98EfzuOtWPTaubs3ZjGhw==; af_ss_a=1; af_ss_b=1; ali_apache_id=11.10.5.11.1665767381704.182929.6; cna=8QWAGxsr5zkCATMkriNgCXqT; _gcl_au=1.1.1391024504.1665767385; _ym_uid=1665767386710329536; _ym_d=1665767386; traffic_se_co=%7B%7D; ali_apache_track=; aep_usuc_f=site=glo&c_tp=SAR&region=SA&b_locale=en_US; e_id=pt60; account_v=1; _bl_uid=h1la296Og2txagzh88qgdjUdtLj3; _gac_UA-17640202-1=1.1668358784.Cj0KCQiAyMKbBhD1ARIsANs7rEHZ7i0V0U3Cs5k09a-_ARhBcYgDUbCM-hqueQncmdkEnRmh2AjD9FYaAlNCEALw_wcB; _fbp=fb.1.1668547878829.1072317895; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005003385349518%094000372496982%091005004008150403%091005003434950072%091005004637641550%091005004949327102%091005004611861291; acs_usuc_t=x_csrf=ov8s3dhzou2h&acs_rt=1e17b58142cf4cf9a7a0a86f709cde0b; intl_locale=en_US; xlly_s=1; _gid=GA1.2.451898769.1668932810; _ym_isad=2; ali_apache_tracktmp=; AKA_A2=A; aeu_cid=4a7e3bfbb15c4b2da43e0aa3e2c9fdcc-1668982163034-04644-_DBDXrxD; _m_h5_tk=99d8ca76ec99e967217127ceb5f6a0a5_1668984415385; _m_h5_tk_enc=27ea9961948ba93a5af9d8f64707bc57; _ym_visorc=b; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&x_as_i=%7B%22aeuCID%22%3A%224a7e3bfbb15c4b2da43e0aa3e2c9fdcc-1668982163034-04644-_DBDXrxD%22%2C%22af%22%3A%225c46e34a30d15%22%2C%22affiliateKey%22%3A%22_DBDXrxD%22%2C%22channel%22%3A%22AFFILIATE%22%2C%22cv%22%3A%221%22%2C%22isCookieCache%22%3A%22N%22%2C%22ms%22%3A%221%22%2C%22pid%22%3A%22171583911%22%2C%22tagtime%22%3A1668982163034%7D&acs_rt=fc358b1213514512bbaee4149a8d005e; XSRF-TOKEN=927e3f09-b5cc-405d-85ba-a34dd2619166; _ga=GA1.1.821934501.1665767385; cto_bundle=tBZYkl9LdnBXbm5hMjdFZXlVMncxM0IzUGZDaG92c0RBejlrUHFBb3U3TVBHeWVEb3oySGpOSkZDWUxpRUlkbkpjdUkySkpSJTJGUlZqaUl1cWtNTkdhZ3B5VVlqVjNVYzdsU0cwU0UxTFJ2VHMyT1lhV1JPVzBuUXhOQ09tY2thQ3FzbUMlMkZYdUJIUGRmckZ1NUQlMkJSMVUyRGpzanclM0QlM0Q; JSESSIONID=CE29CDA8B70DFA99DEA169B0CBE824E6; intl_common_forever=mgFNaMuFu9zeSbzhoTL8GWPXjzs5AKa9Q/naIvk6dGFUrKHAOak0Lg==; _ga_VED1YSGNC7=GS1.1.1668982166.22.1.1668982198.0.0.0; RT="z=1&dm=aliexpress.com&si=1323f375-89b6-49e7-8dad-e39679fbf4af&ss=lapwwitw&sl=1&tt=ihi&rl=1&ld=ihj"; tfstk=cm_VBeswErUVLf1TpUYN8Yu2mPdAaQfcs4RBmRDJGf5mwmxyLsDoBQjL1QRsaAxc.; l=eBPeqjiRTUYT8UmUBO5CFurza779qKRbzsPzaNbMiIncC6X51yJ95NxQmAitNptRRWXVML8p4oV4bMJtHekb8yDXCT2Irdi7i_S9ee8C.; isg=BC0t_DGTMvb-ktYpSDrBX5cvPMmnimFc9Z-MvW86qkV-5k-YNtueLYzw0KIA5nkU',
  'dnt': '1',
  'referer': 'https://www.aliexpress.com/af/category/'+str(catId)+'.html?trafficChannel=af&CatId=' + str(catId) + '&catName=' + str(catName)+'&ltype=affiliate&SortType=default&page='+str(page-1)+'&isrefine=y',
  'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
    # Use ur own Scraper Api key here
    apiKey = "Scraper-Api"
    try:
      client = ScraperAPIClient(api_key=apiKey)
      result = client.get(url='https://www.aliexpress.com/glosearch/api/product?trafficChannel=main&CatId=' + str(catId) + '&catName=' + str(catName)+'&ltype=wholesale&SortType=default&page='+str(page) + '&isrefine=y&origin=y&keep_headers=true',headers=headers,retry=1)
      return result.json()['mods']['itemList']['content']
    except:
      return [];

def main():
      for j in range(0,len( categoryIds)):
        products = []
        products.clear()
        for i in range(1,221):
          products.extend(getProducts(catId=categoryIds[j],page=i,catName=catName[j]))
          print("We are at Category %s at page %d and we have %d products" %(categoryIds[j] ,i , len(products)))
          js =  json.dumps(products)
          with open("raw_20_"+catName[j]+".json", "w") as outfile:
            outfile.write(js)



main()
