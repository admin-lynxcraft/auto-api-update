#############
###Modules###
#############
from os import system, name 
import glob
import os
import time


#######################
### Global Variables###
#######################
global count
global vaild_folder_location
global advanced_api_version
count = -1

###############
###Main Code###
###############

#########
###API###
#########
def api():
    global advanced_api_version
    print (""""
API Version:
---------------------------------------------------------------
Please enter the latest/your choice of API:
For Example if you want to upgrade from 2.0.0 to 2.1.3
simply type '2.1.3'.(No quotes) (The code does the rest for you)
---------------------------------------------------------------
Taking User Input....""")
    baisc_api_version = input()
    advanced_api_version = "api: " + "[" + baisc_api_version + "]"
    print ("""
API Confirmation:
----------------------------------------------------------------
Is this """, advanced_api_version,"""the API Version you want.
Please Note:The code has been changed so the plugin will run 
correctly.
----------------------------------------------------------------
Please answer 'y' for yes 'n' for no (without quotes) at input.
----------------------------------------------------------------
Taking Input Now....""")
    location_confirmation = input()
    if 'y' in location_confirmation:
        print ("""
Sucess
---------------------------------
Moving to plugin folder location.
---------------------------------
....""")
        time.sleep(5)
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear')
        location()

    elif 'n' in location_confirmation:
        print ("""
Fail:
-------------------------
Moving back to API Input.
Try Again....
-------------------------
....""")
        time.sleep(5)
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear')
        api()

    else:
        print (""""
Error:
------------------------------------------------------------
Please only 'y' for yes 'n' for no (without quotes) at input.
Do not use CAPITALS.
------------------------------------------------------------
Going Back To API Version....""")
        time.sleep(5)
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear') 
        api()

##############
###Location###
##############
def location():
    global vaild_folder_location
    print ("""
Plugins Folder Location:
----------------------------------------------------------------------
Please Type in the location of your PocketMine Server Plugins Folder. 
For Example C:/Users/ben/Documents/PocketMine/plugins.
You can use backwards slash or fowards \ / .
You need to include the Drive Letter C:/ or sda1.
---------------------------------------------------------------------
Taking Input Now....""")
    invaild_folder_location = input()
    vaild_folder_location = os.path.normpath(invaild_folder_location)
    print ("""
Vaild Location:
---------------------------------------------------------------
Is this """, vaild_folder_location, """The location you want.
Please Note:The code has changed your input so the location is 
vaild for your system.
---------------------------------------------------------------
Please answer 'y' for yes 'n' for no (without quotes) at input.
---------------------------------------------------------------
Taking Input Now....""")
    location_confirmation = input()
    if 'y' in location_confirmation:
        print ("""
Success:
-------------------------------
Moving to file searh and wirte.
-------------------------------
Going to Files....""")
        time.sleep(5)
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear')
        files()

    elif 'n' in location_confirmation:
        print ("""
Fail:
------------------------------
Moving back to location input.
Try again....
------------------------------
Going to Location Input....""")
        time.sleep(5)
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear')
        location()

    else:
        print (""""
Error:
-------------------------------------------------------------
Please only 'y' for yes 'n' for no (without quotes) at input.
Do not use CAPITALS.
-------------------------------------------------------------
Going to Location Input....""")
        time.sleep(5)
        location()
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear') 
###########
###Files###
###########

def files():
    global advanced_api_version
    global vaild_folder_location
    global count
    sub_folders = os.listdir(vaild_folder_location)
    while True:
        count = count + 1
        try:
            current_folder = os.path.join(vaild_folder_location, sub_folders[count])
            current_folder_str = str(current_folder)
            print ("Found:", current_folder_str)
            os.chdir(current_folder)
            f = open("plugin.yml", "r")
            lines = f.readlines()
            f.close()
            lines[3] = advanced_api_version
            f = open("plugin.yml", "w")
            f.writelines(lines)
            f.close()
        except (IOError):
            print ("Not a folder...Skipping")
            pass
        except (IndexError):
            print ("""
Working Done...:
-------------------------------------------------------------------------
The porgram has completed and has checked all the sub folders of plugins.
Each plugin file should now contain the requested API you slected.
Thank You for Using this Code :).
-------------------------------------------------------------------------
Exiting....
""")
            time.sleep(5)
            break
            exit()

###########
###Start###
###########   

api()
