import Activity as a
import time

dict_urltime = {}

def get_chrome_url_x():
        detail_full = a.get_active_window_raw()
        detail_list = detail_full.split(' - ')
        if detail_list[-1] == "Google Chrome" or detail_list[-1] == "Mozilla Firefox":
            return detail_list[0]

def runTrackUrl():
    new_url = None
    current_url = get_chrome_url_x()
    urlstart = time.time()
    while(True):
        if new_url != current_url:
            if current_url != None and current_url != "New Tab":
                urlstop = time.time()
                print(current_url)
                
                urlran = int(urlstop-urlstart)

                if current_url in dict_urltime.keys():
                    dict_urltime[current_url] += urlran
                    print(dict_urltime) 
                else:
                    dict_urltime[current_url] = urlran
                    print(dict_urltime)

            current_url = new_url
        new_url = get_chrome_url_x()


runTrackUrl()

