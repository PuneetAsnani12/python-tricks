import csv
import json

csvfile = open('flipkart_com-ecommerce_sample.csv', 'r',encoding='utf-8',errors='ignore')
jsonfile = open('flipkart.json', 'w')

fieldnames = ("uniq_id","crawl_timestamp","product_url","product_name","product_category_tree","pid","retail_price","discounted_price","image","is_FK_Advantage_product","description","product_rating","overall_rating","brand","product_specifications")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)