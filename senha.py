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

print generated_key(18) 

