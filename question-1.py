# Author: ATN 12/14/21

import random

def assign_id():
    number = str(random.randint(0, 9999))
    clone_id = "CT-{0}".format(number)
    return clone_id
    
while True:
    response = input("Name a clone? ")
    if(response == "Y"):
        assign_id()
    if(response == "N"):
        break
