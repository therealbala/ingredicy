# views.py
from wsgi import * 

@app.route('/') 
@app.route('/blog') 
@app.route('/blog/') 
def index():
    return render_template('index.html',site=site) 

@app.route('/blog/<slug>')   
def blogpost(slug): 
    return render_template('blog.html',site=site,recipename='',recipe=d['maggie']) 

@app.route('/find/<item>') 
def etry(item):  
    add_recipe = []  
    item_list = item.split(',')    

    for dvalue in d.keys():  
        add_recipe.append(dvalue) 
        if len(d[dvalue]['need'])<=len(item_list): 
           for i in d[dvalue]['need']: 
               if i not in item_list: 
                  add_recipe.remove(dvalue)
                  break 
        else:
            add_recipe.remove(dvalue) 

    if len(add_recipe)!=0:
        return render_template('recipes.html',recipes=add_recipe,site=site)
    return 'Not found' 

