from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from restaurants_model  import Restaurants

app = Flask(__name__)
restaurants = Restaurants()


# Task 1: Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET','POST'])
def new_menu_item(restaurant_id):
    if request.method == 'POST':
        restaurants.add_menu_item(request.form['item_name'], restaurant_id = restaurant_id)
        flash("New Menu Item Created ({})".format(request.form['item_name']))
        return redirect(url_for('restaurant_menu', restaurant_id = restaurant_id))
    else:
        return render_template('new_menu_item.html', restaurant_id = restaurant_id)
    

# Task 2: Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:item_id>/edit/', methods = ['GET','POST'])
def edit_menu_item(restaurant_id, item_id):
    if request.method == 'POST':
        restaurants.update_menu_item(item_id, request.form['name'])
        flash("{} Changed Successfully".format(request.form['name']))
        return redirect(url_for('restaurant_menu', restaurant_id = restaurant_id))
    else:
        item = restaurants.get_menu_item(item_id)        
        return render_template('edit_menu_item.html', item = item)
        

# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:item_id>/delete/', methods = ['GET','POST'])
def delete_menu_item(restaurant_id, item_id):
    if request.method == 'POST':
        print("in delete_menu_item: {}-{}".format(restaurant_id, item_id))
        item_name = restaurants.get_menu_item(item_id).name
        restaurants.delete_menu_item(item_id)
        flash("{} Deleted".format(item_name))
        return redirect(url_for('restaurant_menu', restaurant_id = restaurant_id))
    else:
        item = restaurants.get_menu_item(item_id)
        return render_template('delete_menu_item.html', item=item)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_menu(restaurant_id = 1):
    restaurant = restaurants.get_restaurant(restaurant_id)
    items = restaurants.get_menu_items_of_restaurant(restaurant_id)
    return render_template('menu.html', restaurant = restaurant, items = items)

# Making an API Endpoing (GET request)
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurant_menu_json(restaurant_id):
    restaurant = restaurants.get_restaurant(restaurant_id)
    items = restaurants.get_menu_items_of_restaurant(restaurant_id)
    return jsonify(menu_items=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/JSON')
def menu_item_json(restaurant_id,item_id):
    item = restaurants.get_menu_item(item_id)
    return jsonify(menu_item=item.serialize)

if __name__ == '__main__':
    
    # The secret_key is used in user-specific information saved in the web server session.
    # This is implemented on top of cookies and signs the cookies cryptographically with the
    # secret_key.
    # The secret_key should be VERY secure. To generate, use os.urandom(24)
    app.secret_key = '\x90\x96\xcex\xe1\xe1\xc0\xd7+T\x81\xdde\x19\x05\x00}\xd7\x90\x14skl\xcf'
    
    # the server will load itself automatically every time it detects a code change.
    # this means that we won't need to keep stopping and restarting the server manually
    # while developing the app 
    app.debug = True        
    
    # Since we run this server on our vagrant machine, we have to make the server accessible
    # on our network by setting host = '0.0.0.0' 
    # If we would have developed and run on the same machine, we wouldn't have needed this. 
    app.run(host = '0.0.0.0' , port = 5000)
