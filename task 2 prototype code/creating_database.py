from easy import SQL

db = SQL("database.db")

    
# query1 = """
#         CREATE TABLE users (
#         UserId INT PRIMARY KEY,
#         FirstName TEXT(255) NOT NULL,
#         LastName TEXT(255) NOT NULL,
#         Username VARCHAR(255) NOT NULL UNIQUE,
#         Password VARCHAR(255) NOT NULL,
#         Address VARCHAR(255) NOT NULL,
#         City VARCHAR(255) NOT NULL
#         )
#         """
        
    
# query2 = """
#         CREATE TABLE Products(
#         ProdcutID INT PRIMARY KEY ,
#         ProductName VARCHAR(255) NOT NULL,
#         ProductQuantity INT NOT NULL,
#         ProductSupplier VARCHAR(255) NOT NULL,
#         ProductImages BLOB 
#             )
#     """


# query3 = """

#         CREATE  TABLE Employees(
#         EmployeeID INT PRIMARY KEY ,
#         FirstName VARCHAR(255) NOT NULL ,
#         LastName VARCHAR(255) NOT NULL ,
#         Position VARCHAR(255) NOT NULL ,
#         Since VARCHAR(255) NOT NULL
#         )
#     """

# query5 = """

#         CREATE TABLE Orders (
#         OrderID INT PRIMARY KEY ,
#         OrderedProduct VARCHAR(255) NOT NULL ,
#         OrderReceipt VARCHAR(255) NOT NULL,
#         OrderDate DATE NOT NULL,
#         DeliveryDate DATE NOT NULL
#         )
#         """


# query6= """
#         CREATE TABLE  User_Order_History(
#         user_order_ID INT PRIMARY KEY,
#         OrderDate DATE NOT NULL,
#         OrderSummary VARCHAR(255),
#         OrderDelivery DATE NOT NULL ,
#         OrderTotalAmount FLOAT DEFAULT "0.00"

#         )

#         """
        
# LIST= [query1,query2,query3,query5,query6]


# def create_datbase():
#         query = """
#             CREATE DATABASE IF NOT EXIST database
#             """
#         db.run(query)


# #TO BE USED WHEN CREATING THE TABLES AND DATABASE
# # for query in LIST:   
# #          db.run(query)

# #drop tables
# QUERY_NUKE = """
#     DROP TABLE users
# """


# #add foreign keys 
# class foreignKeys():
#         def __init__(self):
#                 self.orderHistory
#                 self.productOrders

#         def productOrders(self):
#                 query = """
#                 ALTER TABLE  Order
#                 ADD COLUMN ProductID INTEGER NOT NULL
#                 FOREIGN KEY(ProductID) REFERENCES Product(ProductID)
#                 """
#                 db.run(query)


#         def orderHistory(self):
#                 query ="""
#                         ALTER TABLE  User_Order_History
#                         ADD COLUMN userID INTEGER NOT NULL,
#                         FOREIGN KEY(userID) REFERENCES users(userID) 
#                         """
#                 db.run(query)

        

# foreignKeys()
# query= """
# INSERT INTO TABLE users(UserId,FirstName,LastName,Username,Password,Address,City)
# VALUES(1,Ash,Chi, janeDoe, theoretical,12,City)
# """
# db.run(query)

# # db.run("""
# # ALTER TABLE  User_Order_History
# # ADD COLUMN userID INTEGER NOT NULL,
# #        FOREIGN KEY(userID) REFERENCES users(userID)  
# # """)


# class addingData():
#         def __init__(self):
#                 addingUsers = self.addUsers
#                 addingOrders = self.addOrders
#                 addingEmployees = self.addEmployees
#                 addingProduct = self.addProducts


#         def addEmployees(self):
#               add_employees_query = """
#                 INSERT INTO Employees (EmployeeID,Firstname, Lastname ,Position, Since)
#                 VALUES(?,?,?,?,?,?)

#                 """  
#               db.run(add_employees_query)

#         def addUsers(self):
#                 add__users_query = """
#                         INSERT INTO users (FirstName, LastName, Username ,Password, Address , City)
#                         VALUES(?,?,?,?,?,?)
#                         """
                
#                 db.run(add__users_query)
        
#         def addProducts(self):
#                 add_products_query= """
#                         INSERT INTO Products(ProductName,ProductQuantity,ProductSupplier,ProductImage)
#                         VALUES(?,?,?,?)
#                         """
                
#                 db.run(add_products_query)
        
#         def addOrders(self):
#                 add_orders_query="""
#                         INSERT INTO Orders(OrderProduct , OrderReceipt  , OrderDate , DeliveryDate)
#                         VALUES (?,?,?,?)
#                         """
                
#                 db.run(add_orders_query)

# class removingData():
#         def __init__(self):
#                 delEmployees = self.removeEmployees
#                 delProducts = self.removeProduct
#                 delUsers = self.removeUSers
#                 delOrders = self.removeOrders

#         def removeEmployees():
#                 query= """
#                         DELETE * FROM Employees WHERE FirstName = firstname AND LastName= lastname
#                         """

#                 db.run(query)
        
#         def removeProduct():
#                 query= """
#                         DELETE * FROM  WHERE ProductName= PName  
#                         """
#                 db.run(query)

        
#         def removeUSers():
#                 query= """
#                         DELETE * FROM users WHERE Username = username AND Password = password
#                         """

#                 db.run(query)

#         def removeOrders():
#                 query= """
#                         DELETE * FROM OrderHistory WHERE OrderID = orderID
#                         """

#                 db.run(query)




# # adding the data to the databases with placeholder values



# # #creating the tables/database
# # class creating_database:
# #     def __init__(self):
# #         self.__init__
# #         #self.create_database
# #         self.employee_list 
# #         self.orders 
# #         self.User_Order_History 
# #         self.product_tables 
# #         self.user_tables 

# #     # def create_database():
# #     #     query = """
# #     #         CREATE DATABASE database
# #     #         """
# #     #     db.run(query)


# #     def user_tables():
# #         query = """
# #                 CREATE TABLE users (
# #                 UserId INT PRIMARY KEY,
# #                 FirstName TEXT(255) NOT NULL,
# #                 LastName TEXT(255) NOT NULL,
# #                 Password VARCHAR(255) NOT NULL,
# #                 Address VARCHAR(255) NOT NULL,
# #                 City VARCHAR(255) NOT NULL
# #                 )
# #                 """
        
# #         db.run(query)

# #     def product_tables():
# #         query = """
# #                 CREATE TABLE Products(
# #                 ProdcutID INT PRIMARY KEY ,
# #                 ProductName VARCHAR(255) NOT NULL,
# #                 ProductQuantity INT NOT NULL,
# #                 ProductSupplier VARCHAR(255) NOT NULL,
# #                 ProductImages BLOB ,
# #                     )
# #             """
# #         db.run(query)

# #     def employee_list():

# #         query = """

# #                 CREATE  TABLE Employees(
# #                 EmployeeID INT PRIMARY KEY ,
# #                 FirstName VARCHAR(255) NOT NULL ,
# #                 LastName VARCHAR(255) NOT NULL ,
# #                 Position VARCHAR(255) NOT NULL ,
# #                 Since(YEAR) VARCHAR(255) NOT NULL
# #                 )
# #             """
# #         db.run(query)

# #     def orders():
# #         query = """

# #                 CREATE TABLE Orders (
# #                 OrderID INT PRIMARY KEY ,
# #                 OrderedProduct VARCHAR("255) NOT NULL ,
# #                 OrderReceipt VARCHAR(255) NOT NULL,
# #                 OrderDate DATE NOT NULL DEFAULT date("now","localtime") ,
# #                 DeliveryDate DATE NOT NULL DEFAULT date("now","localtime")
# #                 ) 
# #                 """
        
# #         db.run(query)

# #     def User_Order_History():
# #         query= """
# #                 CREATE TABLE  User_Order_History(
# #                 user_order_ID INT PRIMARY KEY,
# #                 OrderDate DATE NOT NULL DEFAULT date("now","localtime"),
# #                 OrderSummary VARCHAR(255) DEFAULT "Nothing Here Yet",
# #                 OrderDelivery VARCHAR(255) DEFAULT "Nothing Here Yet",
# #                 OrderTotalAmount FLOAT DEFAULT 0.00

# #                 )

# # #                 """
# #         db.run(query)

# # #creating_database()
# # creating_database = creating_database()
# # creating_database.user_tables
# # creating_database.employee_list
# # creating_database.orders
# # creating_database.User_Order_History
# # creating_database.product_tables

# # #add foreign keys 
# # class foreignKeys():
# #         def __init__(self):
# #                 self.orderHistory
# #                 self.productOrders

# #         def productOrders(self):
# #                 query = """
# #                 ALTER TABLE  Order
# #                 ADD COLUMN ProductID INTEGER NOT NULL
# #                 FOREIGN KEY(ProductID) REFERENCES Product(ProductID)
# #                 """
# #                 db.run(query)


# #         def orderHistory(self):
# #                 query ="""
# #                         ALTER TABLE  User_Order_History
# #                         ADD COLUMN userID INTEGER NOT NULL,
# #                         FOREIGN KEY(userID) REFERENCES users(userID) 
# #                         """
# #                 db.run(query)

        

# # foreignKeys()

# # # adding the data to the databases with placeholder values
# # class addingData():
# #         def __init__(self):
# #                 addingUsers = self.addUsers
# #                 addingOrders = self.addOrders
# #                 addingEmployees = self.addEmployees
# #                 addingProduct = self.addProducts


# #         def addEmployees(self):
# #               add_employees_query = """
# #                 INSERT INTO Employees (EmployeeID,Firstname, Lastname ,Position, Since)
# #                 VALUES(?,?,?,?,?,?)

# #                 """  
# #               db.run(add_employees_query)

# #         def addUsers(self):
# #                 add__users_query = """
# #                         INSERT INTO users (FirstName, LastName, Username ,Password, Address , City)
# #                         VALUES(?,?,?,?,?,?)
# #                         """
                
# #                 db.run(add__users_query)
        
# #         def addProducts(self):
# #                 add_products_query= """
# #                         INSERT INTO Products(ProductName,ProductQuantity,ProductSupplier,ProductImage)
# #                         VALUES(?,?,?,?)
# #                         """
                
# #                 db.run(add_products_query)
        
# #         def addOrders(self):
# #                 add_orders_query="""
# #                         INSERT INTO Orders(OrderProduct , OrderReceipt  , OrderDate , DeliveryDate)
# #                         VALUES (?,?,?,?)
# #                         """
                
# #                 db.run(add_orders_query)

# # #deleting data from the tables 
# # class removingData():
# #         def __init__(self):
# #                 delEmployees = self.removeEmployees
# #                 delProducts = self.removeProduct
# #                 delUsers = self.removeUSers
# #                 delOrders = self.removeOrders

# #         def removeEmployees():
# #                 query= """
# #                         DELETE * FROM Employees WHERE FirstName = firstname AND LastName= lastname
# #                         """

# #                 db.run(query)
        
# #         def removeProduct():
# #                 query= """
# #                         DELETE * FROM  WHERE ProductName= PName  
# #                         """
# #                 db.run(query)

        
# #         def removeUSers():
# #                 query= """
# #                         DELETE * FROM users WHERE Username = username AND Password = password
# #                         """

# #                 db.run(query)

# #         def removeOrders():
# #                 query= """
# #                         DELETE * FROM OrderHistory WHERE OrderID = orderID
# #                         """

# #                 db.run(query)



# # @app.route('/run-python', method=['GET'])



 
query= """
INSERT INTO users(FirstName,LastName,Username,Password,Address,City)
        VALUES(Ash,Chi,janeDoe,theoretical,12,City)
"""
db.run(query)