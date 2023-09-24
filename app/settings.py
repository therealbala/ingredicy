from datetime import datetime  
import pytz 
timezone = pytz.timezone('Asia/Kolkata') 

class basic_setting:
    site = 'Blog' 
    site2 = 'Content'  
    name=site+site2 
    version = 1.0 
    dt = datetime.now(timezone)  
    year = dt.year 
    month = dt.month 
    day = dt.day 
    
    #### FOOTER #### 
    class footone: 
        head = 'Contact'
        para = 'Help msg'
    class foottwo: 
        head = 'Some'
        para = 'Text' 
 