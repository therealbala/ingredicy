from flask import Flask,render_template 
import settings as config 
from sample import Recipes_data as d    

app= Flask(__name__)  
site = config.basic_setting 

from views import * 
 
if __name__ == '__main__': 
   app.run(debug = True,host='0.0.0.0', port=80) 


   
