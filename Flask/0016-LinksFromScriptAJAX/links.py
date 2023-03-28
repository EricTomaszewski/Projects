import random
import time
    

links_list = ["https://itoma.co.uk/", "https://vr.itoma.co.uk/", "https://fun.itoma.co.uk/", "https://deals.itoma.co.uk"]
def links_spit():
    try:
        if len(links_list) > 0:
            print(len(links_list))
            print(links_list)
            return links_list.pop(0)
    except:
        pass