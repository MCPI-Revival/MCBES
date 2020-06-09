# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

import decimal

class bcmath:
    @staticmethod
    def bcmul(num1, num2, scale=None):
        if scale != None:
            decimal.getcontext().prec = scale
        result = decimal.Decimal(num1) * decimal.Decimal(num2)
        return int(result)
      
    @staticmethod
    def bcdiv(num1, num2, scale=None):
        if scale != None:
            decimal.getcontext().prec = scale
        result = decimal.Decimal(num1) / decimal.Decimal(num2)
        return int(result)
       
    @staticmethod
    def bcadd(num1, num2, scale=None):
        if scale != None:
            decimal.getcontext().prec = scale
        result = decimal.Decimal(num1) + decimal.Decimal(num2)
        return int(result)
    
    @staticmethod
    def bcsub(num1, num2, scale=None):
        if scale != None:
            decimal.getcontext().prec = scale
        result = decimal.Decimal(num1) - decimal.Decimal(num2)
        return int(result)
    
    @staticmethod
    def bccomp(num1, num2):
        result = (int(num1) > int(num2)) - (int(num1) < int(num2))
        return int(result)
    
    @staticmethod
    def bcmod(num1, num2):
        result = int(num1) % int(num2)
        return int(result)
    
    @staticmethod
    def bcpow(num1, num2):
        result = int(num1) ** int(num2)
        return int(result)
    
    @staticmethod
    def bcpowmod(num1, num2, mod):
        result = pow(num1, num2, mod)
        return int(result)
    
    @staticmethod
    def bcscale(scale):
        result = decimal.getcontext().prec = scale
        return int(result)
    
    @staticmethod
    def bcsqrt(num):
        result = math.sqrt(num)
        return int(result)
