from flask import Flask
from operators import Calculation
from exception import *

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome"

@app.route('/<operator>/<int:a>/<int:b>')

def index(operator, a, b):
    obj = Calculation(a,b)
    if operator == 'add':
        try:
            if a>=11 or b>=11:
                raise ValueToLarge ("Number should be less than 11")
            else:
                return str(obj.add())
        except ValueToLarge as e:
            return str(e)
        
    if operator == 'sub':
        try:
            if a<b:
                raise ValueToSmall ("The value of a should be greater than b")
            else:
                return str(obj.sub())
        except ValueToSmall as s:
            return str(s)
    
    if operator == 'mul':
        return str(obj.mul())
    
    if operator == 'div':
        try:
            if  b == 0:
                raise ZeroDivisionError ('divided by zero not possible')
            else:
                 return str(obj.div())
        except ZeroDivisionError as z:
            return str(z)

if __name__ == '__main__':
    app.run (debug = True, port = 5612)