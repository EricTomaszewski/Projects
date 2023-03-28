import random
import time

'''def links_spit():
    links_list = ["https://itoma.co.uk/", "https://vr.itoma.co.uk/", "https://fun.itoma.co.uk/", "https://deals.itoma.co.uk"]
    for i in links_list:
        time.sleep(random.randint(1, 4))
        yield i'''


'''def links_spit():
    links_list = ["https://itoma.co.uk/", "https://vr.itoma.co.uk/", "https://fun.itoma.co.uk/", "https://deals.itoma.co.uk"]
    for link in links_list:
        # time.sleep(random.randint(1, 4))
        time.sleep(3)
        yield link
        # yield from [link]'''
        

links_list = ["https://itoma.co.uk/", "https://vr.itoma.co.uk/", "https://fun.itoma.co.uk/", "https://deals.itoma.co.uk"]
def links_spit():
    try:
        if len(links_list) > 0:
            print(len(links_list))
            print(links_list)
            return links_list.pop()
    except:
        pass