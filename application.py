import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///anime_list.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show anime list"""
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        user_id = session["user_id"]
        images = request.form.get("Imgs")
        links = request.form.get("Hrefs")
        name = request.form.get("Names")
        
        # Image imput Error checking
        if not images:
            return apology("Empty IMAGE field")
        
        # Link input Error checking
        elif not links:
            return apology("Empty LINK field.")
        
        # Name input Error checking
        elif not name:
            return apology("Empty Name field.")
        
        
        # Save image, link , user_id and name in database
        try:
            db.execute("INSERT INTO animes (imageL, siteL, user_id, name) VALUES(?, ?, ?, ?)", images, links, user_id, name)
            
            # Redirect user to home page
            return redirect("/")
            
        except:
            return apology("Error entering")
            
        
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        
        # Collecting data from the database to insert into the html
        user_id = session["user_id"]
        anime_images = db.execute("SELECT * FROM animes WHERE user_id = ?", user_id)
        
        # launch Index page
        return render_template("index.html", anime_images=anime_images)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Stores username, password and all usernames already registered in the database
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        # User name Error checking
        if not username:
            return apology("Empty USERNAME field")
        
        # Password Error checking
        elif not password:
            return apology("Empty password field.")
        
        elif not confirmation:
            return apology("Empty confirmation field.")
        
        if password != confirmation:
            return apology("Passwords do not match")
        
        # Save username and hash of password in database
        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))
            
            # Redirect user to home page
            return redirect("/")
        except:
            return apology("USERNAME already exists")
    
    # User reached route via GET (as by clicking a link or via redirect)   
    else:
        # launch register page
        return render_template("register.html")


@app.route("/removes", methods=["GET", "POST"])
@login_required
def removes():
    """Remove an Anime"""
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        user_id = session["user_id"]
        options = request.form.get("comp_select")
        
        # Options in select Error checking
        if not options:
            return apology("ERROR")
        
        try:
            #Updata anime list
            db.execute("DELETE FROM animes WHERE name = ?", options)
            
            # Redirect user to home page
            return redirect("/")
            
        except:
            return apology("Error entering")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
