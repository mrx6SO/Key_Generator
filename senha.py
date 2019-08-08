#!/usr/bin/env python
# -* coding: utf-8 -*-

## function to generate key 

import sys, time, string, random
def generated_key(size):
        caracters = '~{}^=+()@#$%*¨\/[]&ABCDEFGHIJKLMNOPQRSTUVXZY0123456789abcdefghijlmnopqrstuwvxz'
        password = ''
        for char in xrange(size):
                password += random.choice(caracters)
        return password

if __name__ == "__main__": 
        
    password = generated_key(12) 
    print(password)
    
    with open(password, "w+") as file:
        file.write(password)
    pass
