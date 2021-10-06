# Anime List  To.Watch

**Author: Thiago Tatico Dall Molin**

 #### Video Demo: https://www.youtube.com/watch?v=qx0cIr2Y-1s

#### Description:

This is my final project for the CS50 course at Harvard. It is a simple site where you can create a list of animes and series to remember to watch later, just insert an image link, a site to redirect the user when clicking on the image, and a title. The list created is saved on your account and it is accessible from anywhere. Any time you need to change it, just log in and it is there.

#### Application details:

The application was made on CS50 IDE using Python, HTML, CSS, Flask,Bootstrap frameworks and SQLite database.

The application's Python code is split into two files: application.py and helpers.py.

#### **application.py:**
 This is the application's heart, where most of the functions and commands to control the website are. First, some libraries are imported to build the application, such as CS50's SQL to be able to control the database through Python, some important Flask libraries, and two other libraries to identify errors and hash user's passwords when creating one account on the website, in addition to importing helpers.py functions to be used in the main code.

 Then the Flask application is configured and the session system is implemented for each user so that they do not need to log in every time they refresh the page. And finally, the CS50 library is configured to use the SQLite database

 After the initial settings of the application, the functions are defined: index(), login(), logout(), register(), removes() and errorhandler()

 **index():**
  The index() function has a "/" route, accepts the GET and POST methods, and requires a login to be executed. Its main function is to display the list of anime or series stored in the user's database. When the user accesses the page via GET, the function accesses its database and sends the list to the index.html template, then it can dynamically generate the user's list. Finally, when the user fills the inputs in index.html to store a new item to the list, he uses the function through the POST method. When the request is made, the function collects the data sent by the user, does an error checking and stores this new data in the database, then redirects the user to the index.html template, reloading the list with the new item included.

 **login():**
   The login() function has as a route "/login" and accepts the GET and POST methods. Its main function is to check if the username and password entered match those stored in the database. After a check to validate this information, a session is started and the user is redirected to the "/" route. When the user accesses the page via GET, the login.html template is loaded, enabling the input of data to log in. Finally, when the user fills the inputs in login.html, he uses the function through the POST method. First, it is checked if the user has entered a username and password to log in, if you leave any of the fields blank an error is returned. Then the function accesses the database to search for that username, if found the function checks the hash stored in the database with the hash of the password entered by the user. If all goes well, the session is started using the user id as the value. Thus, the user is redirected to the "/" route.

  **logout():**
   The logout() function has the route "/logout". Its main function is to log the user out through the session.clear() command, and redirect him to the "/" route.

  **register():**
   The register() function has a "/register" route and accepts the GET and POST methods. Its main function is to register the account created by the user in the database, doing that it is possible to log in later. Making it possible to maintain a different list for each account on the site. When the user accesses the page via GET the register.html template is loaded, enabling the input of data to perform the registration. Finally, when the user fills the inputs in register.html, it uses the function through the POST method. First, it is checked if the user entered with username, password, and password verification to register, if you leave any of the fields blank or the passwords are not the same, an error is returned. Then the function accesses the database to store this new user. Thus, the user is redirected to the "/" route.

  **removes():**
   The removes() function takes the route "/removes" and accepts the POST method. Its main function is to remove an item from the user's list. When the user accesses the page via Post, the function uses the title of the selected item in index.html to remove it from the database. Then the function redirects the user to the "/" route.

  **errorhandler():**
   The errorhandler() function returns error messages when something doesn't work as it should.

#### **helpers.py:**
 helpers.py has two functions: **apology(message, code=400): and login_required(f):.**

**apology(message, code=400):**
  The main function of apology() is to render the apology.html template with the designated error message

#### **layout.html:**
  This is the layout used by other HTML templates. It has 3 tag blocks to insert data in the template using the layout:  block title ,  block main  and  block footer .

#### **index.html:**
  Home page template with the list of anime or series of the logged in user, inputs to add new items and a dropdown menu to select the item to be removed from the list.

#### **login.html:**
  Login page template.

#### **register.html:**
  Registration page template.

#### **apology.html:**
  Returns an image with an error message generated dynamically with the help of the apology(message, code=400) function. 

### **Database:**

![1](https://imgur.com/upViSLf.jpg)

![2](https://imgur.com/PfH67Wh.jpg)

![3](https://imgur.com/S3fQWUy.jpg)
