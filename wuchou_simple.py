# -*- encoding=utf8 -*-
__author__ = "tjzg"

from airtest.core.api import *

auto_setup(__file__)
def wait_until(template):
    while True:
        try:
            wait(template)
            sleep(1)
            return 1
        except:
            print('waiting...')

def bubing():
    wait_until(Template(r"tpl1581192212999.png", record_pos=(-0.386, 0.248), resolution=(1600, 900)))
    touch(Template(r"tpl1581192212999.png", record_pos=(-0.386, 0.248), resolution=(1600, 900)))
    sleep(1)
    touch(Template(r"tpl1581192246263.png", record_pos=(0.376, 0.186), resolution=(1600, 900)))
    sleep(1)
    touch(Template(r"tpl1581192265190.png", record_pos=(0.448, -0.258), resolution=(1600, 900)))

def bubing_all():
    wait_until(Template(r"tpl1581192010921.png", record_pos=(-0.483, 0.146), resolution=(1600, 900)))
    touch(Template(r"tpl1581192010921.png", record_pos=(-0.483, 0.146), resolution=(1600, 900)))
    bubing()
    wait_until(Template(r"tpl1581192366666.png", record_pos=(-0.283, 0.146), resolution=(1600, 900)))
    touch(Template(r"tpl1581192366666.png", record_pos=(-0.283, 0.146), resolution=(1600, 900)))
    bubing()
    wait_until(Template(r"tpl1581192381824.png", record_pos=(0.473, -0.264), resolution=(1600, 900)))
    touch(Template(r"tpl1581192381824.png", record_pos=(0.473, -0.264), resolution=(1600, 900)))


def goto_land():
    if not exists(Template(r"tpl1581193791986.png", record_pos=(-0.444, 0.135), resolution=(1600, 900))):
        touch((1400,500))
    wait_until(Template(r"tpl1581193791986.png", record_pos=(-0.444, 0.135), resolution=(1600, 900)))
    touch(Template(r"tpl1581193791986.png", record_pos=(-0.444, 0.135), resolution=(1600, 900)))
    wait_until(Template(r"tpl1581902555196.png", record_pos=(-0.159, 0.147), resolution=(1600, 900)))
    touch(Template(r"tpl1581902555196.png", record_pos=(-0.159, 0.147), resolution=(1600, 900)))
    wait_until(Template(r"tpl1581902580445.png", record_pos=(-0.466, 0.226), resolution=(1600, 900)))
    touch((200,750))
    touch(Template(r"tpl1581193555646.png", record_pos=(0.45, 0.145), resolution=(1600, 900)))
    
    

    
    
    
def find_land():
    
    team = 2
    follow_me = 0
    for j in range(1):
        i = 0
        while i < 60:
            if follow_me == 1:
                touch((800,400))
            else:    
                goto_land()
            home = 0
            while (not exists(Template(r"tpl1581560464687.png", record_pos=(0.336, -0.16), resolution=(1600, 900)))):
                    sleep(10)
            if team > 0:
                touch(Template(r"tpl1581248750697.png", record_pos=(0.476, -0.133), resolution=(1600, 900)))
                    
                if team == 2:
                    touch( (650,800) )
                elif team == 1:
                    touch( (1000,800) )
                if exists(Template(r"tpl1581249584391.png", record_pos=(0.289, 0.109), resolution=(1600, 900))):
                    if   follow_me == 0:   
                            follow_me = 1
                        
                            
                            
                            
                    touch(Template(r"tpl1581249584391.png", record_pos=(0.289, 0.109), resolution=(1600, 900)))

                    if follow_me == 1 and exists(Template(r"tpl1581524118960.png", record_pos=(-0.091, 0.09), resolution=(1600, 900))):
                        touch(Template(r"tpl1581524118960.png", record_pos=(-0.091, 0.09), resolution=(1600, 900)))


                        
                    if team == 1 and follow_me == 1:
                        follow_me = 0
                        touch((800,400))
                        wait_until(Template(r"tpl1581903329891.png", record_pos=(0.198, 0.021), resolution=(1600, 900)))
                        touch(Template(r"tpl1581903329891.png", record_pos=(0.198, 0.021), resolution=(1600, 900)))
                        
                    team = team - 1 
                    if team == 0:
                        sleep(60)
                        close_error()
            elif team == 0:
                while team == 0: 
                    coor_list1 = find_all(Template(r"tpl1581249981273.png", record_pos=(0.336, -0.126), resolution=(1600, 900)))
                    coor_list2 = find_all(Template(r"tpl1581250011457.png", record_pos=(0.338, -0.165), resolution=(1600, 900)))
                    coor_list3 = find_all(Template(r"tpl1581250147819.png", record_pos=(0.337, -0.159), resolution=(1600, 900)))
                    coor_list4 = find_all(Template(r"tpl1581509980794.png", record_pos=(0.334, -0.166), resolution=(1600, 900)))
                    if coor_list1 == None and coor_list2 == None and coor_list3 == None and coor_list4 == None :
                        go_home()
                        into_home()
                        bubing_all()
                        team = 2
                    else:
                        sleep(20)
                        close_error()

            i += 1
                
    j += 1
        
        
def go_home():
    if not exists(Template(r"tpl1581193791986.png", record_pos=(-0.444, 0.135), resolution=(1600, 900))):
        touch((1400,500))
    wait_until(Template(r"tpl1581193791986.png", record_pos=(-0.444, 0.135), resolution=(1600, 900)))
    touch(Template(r"tpl1581193791986.png", record_pos=(-0.444, 0.135), resolution=(1600, 900)))
    wait_until(Template(r"tpl1581193503808.png", record_pos=(-0.296, 0.15), resolution=(1600, 900)))
    touch(Template(r"tpl1581193503808.png", record_pos=(-0.296, 0.15), resolution=(1600, 900)))
    wait_until(Template(r"tpl1581193535663.png", record_pos=(-0.295, 0.205), resolution=(1600, 900)))
    touch(Template(r"tpl1581193535663.png", record_pos=(-0.295, 0.205), resolution=(1600, 900)))
    touch(Template(r"tpl1581193555646.png", record_pos=(0.45, 0.145), resolution=(1600, 900)))

    
def into_home():
    if  exists(Template(r"tpl1581710570190.png", record_pos=(-0.116, 0.019), resolution=(1600, 900))):
        touch(Template(r"tpl1581710570190.png", record_pos=(-0.116, 0.019), resolution=(1600, 900)))
    elif  exists(Template(r"tpl1581529102563.png", record_pos=(0.094, 0.009), resolution=(1600, 900))): 
        touch(Template(r"tpl1581529102563.png", record_pos=(0.094, 0.009), resolution=(1600, 900)))
    
    
    elif exists(Template(r"tpl1581193713835.png", record_pos=(-0.046, -0.088), resolution=(1600, 900))):
        touch(Template(r"tpl1581193713835.png", record_pos=(-0.046, -0.088), resolution=(1600, 900)))  
        
    wait_until(Template(r"tpl1581193731123.png", record_pos=(-0.001, -0.027), resolution=(1600, 900)))
    touch(Template(r"tpl1581193731123.png", record_pos=(-0.001, -0.027), resolution=(1600, 900)))

def close_error():
    if exists(Template(r"tpl1581754912551.png", record_pos=(0.031, -0.032), resolution=(1600, 900))):
        touch(Template(r"tpl1581754926239.png", record_pos=(0.269, 0.096), resolution=(1600, 900)))    
        
def attact_empty_area():
    coor_list = find_all(Template(r"tpl1581245487703.png", record_pos=(-0.336, 0.009), resolution=(1600, 900)))  
    j=0
    for i in coor_list:
        print(j,"      ",i['result'],"\n\n")
        j +=1
        touch( (i['result'][0] + 10 ,i['result'][1] - 50) )
        sleep(1)

        

go_home()
find_land()

