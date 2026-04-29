from flask import Flask, render_template, session , url_for ,request , redirect, flash, Response
from easy import SQL, test
from werkzeug.security  import generate_password_hash , check_password_hash
import secrets 

#establishing app instance
app = Flask(__name__)
#creating database connection 
db = SQL("database.db")

#creating secret key for sessison
app.secret_key = secrets.token_hex(16)



# # #creating the tables/database
# class creating_database:
#     # <UnComment when runniung for the first time>
#     # this is to create the database and tables 


#     # db.run("""
#     #      CREATE DATABASE database
#     #    """) 


#     db.run("""

#                     CREATE TABLE users (
#                     UserId INT PRIMARY KEY,
#                     FirstName TEXT(255) NOT NULL,
#                     LastName TEXT(255) NOT NULL,
#                     Password VARCHAR(255) NOT NULL,
#                     Address VARCHAR(255) NOT NULL,
#                     City VARCHAR(255) NOT NULL
#                     )
#                     """) 
            
#     db.run( """
#             CREATE TABLE Products(
#             ProdcutID INT PRIMARY KEY ,
#             ProductName VARCHAR(255) NOT NULL,
#             ProductQuantity INT NOT NULL,
#             ProductSupplier VARCHAR(255) NOT NULL,
#             ProductImages BLOB 
#                 )
#         """
#     )

#     db.run("""
#                 CREATE  TABLE Employees(
#                 EmployeeID INT PRIMARY KEY ,
#                 FirstName VARCHAR(255) NOT NULL ,
#                 LastName VARCHAR(255) NOT NULL ,
#                 Position VARCHAR(255) NOT NULL ,
#                 Since(YEAR) VARCHAR(255) NOT NULL
#                 )
#             """
#            )
        

#     db.run("""
#                 CREATE TABLE Orders (
#                 OrderID INT PRIMARY KEY ,
#                 OrderedProduct VARCHAR("255) NOT NULL ,
#                 OrderReceipt VARCHAR(255) NOT NULL,
#                 OrderDate DATE NOT NULL DEFAULT date("now","localtime") ,
#                 DeliveryDate DATE NOT NULL DEFAULT date("now","localtime")
#                 ) 
#             """
#     )
    


#     db.run("""
#                 CREATE TABLE  User_Order_History(
#                 user_order_ID INT PRIMARY KEY,
#                 OrderDate DATE NOT NULL DEFAULT date("now","localtime"),
#                 OrderSummary VARCHAR(255) DEFAULT "Nothing Here Yet",
#                 OrderDelivery VARCHAR(255) DEFAULT "Nothing Here Yet",
#                 OrderTotalAmount FLOAT DEFAULT 0.00)
#             """
#                     )
        
#     # add foreign keys

#     db.run("""
#                     ALTER TABLE  Order
#                     ADD COLUMN ProductID INTEGER NOT NULL
#                     FOREIGN KEY(ProductID) REFERENCES Product(ProductID)
#                     """)



#     db.run("""
#             ALTER TABLE  User_Order_History
#             ADD COLUMN userID INTEGER NOT NULL,
#             FOREIGN KEY(userID) REFERENCES users(userID) 
#             """)
    

        

# #creating_database()


# adding the data to the databases with placeholder values  ¦ admin function
class addingData():
        def __init__(self):
                addingUsers = self.addUsers
                addingOrders = self.addOrders
                addingEmployees = self.addEmployees
                addingProduct = self.addProducts


        def addEmployees(self):
              add_employees_query = """
                INSERT INTO Employees (EmployeeID,Firstname, Lastname ,Position, Since)
                VALUES(?,?,?,?,?,?)

                """  
              db.run(add_employees_query)

        def addUsers(self):
                add__users_query = """
                        INSERT INTO users (FirstName, LastName, Username ,Password, Address , City)
                        VALUES(?,?,?,?,?,?)
                        """
                
                db.run(add__users_query)
        
        def addProducts(self):
                add_products_query= """
                        INSERT INTO Products(ProductName,ProductQuantity,ProductSupplier,ProductImage)
                        VALUES(?,?,?,?)
                        """
                
                db.run(add_products_query)
        
        def addOrders(self):
                add_orders_query="""
                        INSERT INTO Orders(OrderProduct , OrderReceipt  , OrderDate , DeliveryDate)
                        VALUES (?,?,?,?)
                        """
                
                db.run(add_orders_query)

#deleting data from the tables ¦ admin function
class removingData():
        def __init__(self):
                delEmployees = self.removeEmployees
                delProducts = self.removeProduct
                delUsers = self.removeUSers
                delOrders = self.removeOrders

        def removeEmployees():
                query= """
                        DELETE * FROM Employees WHERE FirstName = firstname AND LastName= lastname
                        """

                db.run(query)
        
        def removeProduct():
                query= """
                        DELETE * FROM  WHERE ProductName= PName  
                        """
                db.run(query)

        
        def removeUSers():
                query= """
                        DELETE * FROM users WHERE Username = username AND Password = password
                        """

                db.run(query)

        def removeOrders():
                query= """
                        DELETE * FROM OrderHistory WHERE OrderID = orderID
                        """

                db.run(query)


#home page route
@app.route('/',methods=['POST','GET'])
def index():
    try:
        if  app.secret_key:
            
            return render_template("index.html")
                
            
    except Exception as  e:
          return redirect(url_for(page_not_found)) ,e
    
    
#about us page
@app.route('/about-us', methods=['POST','GET'])
def about_us():
    try:

        return  render_template('about_us.html')
    
    except Exception as  e: 

        return (flash("an error has occured","info" )),render_template("pageNotFound.html")
         
#products routing 
@app.route('/products', methods=['POST','GET'])
def products_or_services():
    try:
        query= """
        SELECT * FROM Products
        """
        data = db.run(query)

        return render_template('products.html'), data
    
    except Exception as e: 

        return (flash("an error has occured")),render_template("pageNotFound.html")
    

@app.route('/login', methods = ["GET","POST"])
def login():
    try:
        if request.method == "POST":
            session["Username"] = request.form.get("Username")
            Username = session["Username"]
            session["Password"] =request.form.get("Password")
            password = generate_password_hash(session["Password"])

            stored_password_hash = db.run("""
                SELECT Password FROM users WHERE username = Username
                FROM Users
                """)


            User = db.run("""
                SELECT Username FROM users WHERE username = Username 
                FROM Users
                """
            )

            if User and check_password_hash(stored_password_hash, password):

                return redirect(url_for("index")), flash(f"Welcome {Username} !")
            
            else:
                return flash("Username not found! ","warning")
            
            
    except ValueError : 

        return (flash("an error has occured" ),render_template("pageNotFound.html"))
        
    return render_template('/login.html')

@app.route('/logout')
def logout():

    session.clear()

    return  flash(" LOGGED OUT SUCCESSFULLY !!"),render_template("/index.html")

@app.route('/sign-up',methods=['POST','GET'])
def sign_up_page():
    try:
        if request.method == "POST":
            session["firstname"] = request.form.get("firstname")
            Firstname = session["firstname"]
            session["lastname"] = request.form.get("lastname")
            Lastname = session["lastname"]
            session["username"] = request.form.get("username")
            Username =  session["username"]
            session["password"] = request.form.get("password")
            hashed_password = generate_password_hash(session["password"])
            session["Address"]= request.form.get("address")
            address = session["Address"]
            session["City"] = request.form.get("city")
            city = session["City"]

            data =[ Firstname,Lastname,Username,hashed_password,address ,city ]
            
            try:
                 
                query = """
                INSERT INTO users(FirstName,LastName,Username,Password,Address,City)
                VALUES(?,?,?,?,?,?)
                """

                db.run(query,data )
                print(data)
            
                flash("Successful, got to Login","success")
                return redirect(url_for(login)) 
                    
 
            except Exception as e:
                flash(" sign up unsuccessful, enter username or password again !","warning"), redirect(url_for(sign_up_page))
                return Response('Error: {}'.format(str(e)), status=500 ), flash(" sign up unsuccessful, enter username or password again !","warning")
                
           
    
    except Exception as  e: 

       return (flash(f"an error has occured" )),render_template("pageNotFound.html")
         # return Response('Error: {}'.format(str(e)), status=500 )
    
    
    return render_template('/signup.html')
    
        
@app.route("/order-history", methods=['POST','GET'])
def order_history():
    try:
         render_template("/order_history.html")

    except:
         return (flash("an error has occured" )),render_template("pageNotFound.html")
    
@app.route('/checkout-page', methods=['POST','GET'])
def checkout():
    try:

        return render_template('/checkout.html')
    
    except Exception as  e: 

        return (flash("an error has occured" )),render_template("pageNotFound.html")


############ admin funtcionality #############
@app.route('/admin-signIn', methods=['POST','GET'])
def admin_signin():
    try:
        if request.method=="POST":

            if app.secret_key and (session["username"] == request.form.get("Administrator")):
                redirect(url_for("admin_choice"))
    
    except Exception as  e: 

        return (flash("an error has occured")),render_template("pageNotFound.html")


@app.route('/admin-choice',methods=['POST','GET'])
def admin_choice():
    try:
        session["adminChoice"] = request.form.get("adminChoice")
        adminChoice = session["adminChoice"]

        if adminChoice == "Add":

            session("adminAction") == request.form.get("adminAction")
            admin_action  = session["adminAction"] 

            if admin_action == "product":
                query ="""      
                    INSERT INTO Products
                    VALUE (?,?,?,?,?)
                        """
                try:
                    productName = input("Enter product name : ") 
                    productQuantity = int(input("Enter product quantity : "))
                    productPrice = float(input())
                except:
                    return "an error has occured "
            
                data =[]

            return render_template("/admin.html")
        
    except Exception as  e: 

        return (flash("an error has occured")),render_template("pageNotFound.html")

@app.route('/error')
@app.errorhandler(404)
def page_not_found( error ):
    render_template("pageNotFound.html")

# starting the function
if __name__ == "__main__" :
    
    app.run(debug=True )


