import parse_funcs as pf
from datetime import datetime
import json 

start_time = datetime.now()

site = pf.BazarstoreParser()

with open('log.json', 'w') as log:
    json.dump(site.get_product_and_its_class(),log)
  
    
print(datetime.now() - start_time)