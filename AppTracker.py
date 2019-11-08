import Activity as a
import time

dict_time = {}

def get_active_window_x():
    full_detail = a.get_active_window_raw()
    if full_detail != None:
        try:
            detail_list = full_detail.split(" - ")
            new_window_name = detail_list[-1]
            return new_window_name
        except SystemError:
            print("You have closed or opened a file!")

def runApptracker():
    new_window = None
    current_window = get_active_window_x()
    appstart = time.time()
    appran = 0
    while(True):
        if new_window != current_window:
            if new_window != None:
                print(current_window)
                appstop = time.time()
                appran = int(appstop-appstart)
                if current_window in dict_time.keys():
                    dict_time[current_window] += appran
                    print(dict_time)
                else:
                    dict_time[current_window] = appran
                    print(dict_time)
                current_window = new_window       
        new_window = get_active_window_x()
        
runApptracker()        


