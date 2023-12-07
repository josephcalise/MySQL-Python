import mysql.connector
#Category ID should be its own table for 3NF
#are SPs for datagrip?
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='Input DB Connection',
            port='3306',
            user='Input DB User',
            password='Input DB Passowrd',
            database='FSEEngStore' #This is the name of the DB you connecting to.
        )
        print(f'Connected to DB.')
        return conn

    except mysql.connector.Error as e:
        print(f'Error connecting to MySQL: {e}')
        return None

def queryCustomers(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT * From Customers"
        cursor.execute(query)
        for row in cursor:
            print(row)
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')

def outOfStock(conn): #Menu 1
    try:
        cursor = conn.cursor()
        query = ("SELECT ProductID, ProductName From Products Where UnitsInStock = 0")
        cursor.execute(query)
        #add if none, there are none
        #extra: Maybe low quanitity.
        data = cursor.fetchall()
        if len(data) == 0:
            print("All products are in stock.")
        else:
            for row in data:
                print(f'PID: {row[0]} | Product: {row[1]}.')
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')

def orderCountByCustomer(conn):
    try:
        cursor = conn.cursor()
        query = ("SELECT C.CustomerID, COUNT(OrderID) FROM Customers C "
                 "left outer join Orders O on O.CustomerID = C.CustomerID "
                 "group by C.CustomerID")
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            print("You have no customers!")
        else:
            for row in data:
                print(f'Customer ID: {row[0]} | Number of Orders: {row[1]}')
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')

def maxItemPerOrder(conn):
    try:
        cursor = conn.cursor()
        query = ("SELECT OD.OrderID, P.ProductID, P.ProductName, P.UnitPrice "
                 "FROM OrderDetails OD join Products P on OD.ProductID = P.ProductID "
                 "WHERE (OD.OrderID, OD.UnitPrice) IN ("
                 "SELECT OrderID, MAX(UnitPrice) FROM OrderDetails GROUP BY OrderID);")
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            print("You have no customers!")
        else:
            print("Most Expensive Items Per Order:")
            for orderID, prodID, prodName, price in data:
                print(f'Order #{orderID}: Product ID {prodID} | Product Name: {prodName} | Product Price: ${price}')
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')

def itemsNeverOrdered(conn):
    cursor = conn.cursor()
    query = ("SELECT P.ProductID, P.ProductName, P.UnitPrice FROM Products P "
             "left join OrderDetails OD on P.ProductID = OD.ProductID "
             "WHERE P.ProductID NOT IN ("
             "SELECT DISTINCT ProductID FROM OrderDetails);")
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            print("You have no customers!")
        else:
            print("Current products that have never been ordered:")
            for prodID, prodName, price in data:
                print(f'Product ID: {prodID} | Product Name: {prodName} | Product Price: ${price}')
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')

def revenueBySupplier(conn):
    cursor = conn.cursor()
    query = ("SELECT S.SupplierID , S.SupplierName, SUM(OD.UnitPrice*OD.Quantity) FROM Suppliers S "
             "join Products P on S.SupplierID = P.SupplierID "
             "join OrderDetails OD on P.ProductID = OD.ProductID "
             "group by S.SupplierID;")
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            print("You have no customers!")
        else:
            print("Supplier's Revenue:")
            for supplierID, supplierName, revenue in data:
                print(f'Supplier ID: {supplierID} | Supplier Name: {supplierName} | Total Sales Revenue: ${revenue}')
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')


def main():
    #form the connection:
    conn = connect_to_database()
    print(
    """
    $$$$$$$$\  $$$$$$\  $$$$$$$$\ $$$$$$$$\ $$\   $$\  $$$$$$\   $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  $$$$$$$$\ 
    $$  _____|$$  __$$\ $$  _____|$$  _____|$$$\  $$ |$$  __$$\ $$  __$$\ \__$$  __|$$  __$$\ $$  __$$\ $$  _____|
    $$ |      $$ /  \__|$$ |      $$ |      $$$$\ $$ |$$ /  \__|$$ /  \__|  $$ |   $$ /  $$ |$$ |  $$ |$$ |      
    $$$$$\    \$$$$$$\  $$$$$\    $$$$$\    $$ $$\$$ |$$ |$$$$\ \$$$$$$\    $$ |   $$ |  $$ |$$$$$$$  |$$$$$\    
    $$  __|    \____$$\ $$  __|   $$  __|   $$ \$$$$ |$$ |\_$$ | \____$$\   $$ |   $$ |  $$ |$$  __$$< $$  __|   
    $$ |      $$\   $$ |$$ |      $$ |      $$ |\$$$ |$$ |  $$ |$$\   $$ |  $$ |   $$ |  $$ |$$ |  $$ |$$ |      
    $$ |      \$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ | \$$ |\$$$$$$  |\$$$$$$  |  $$ |    $$$$$$  |$$ |  $$ |$$$$$$$$\ 
    \__|       \______/ \________|\________|\__|  \__| \______/  \______/   \__|    \______/ \__|  \__|\________|                                                                                                
    Welcome to the FseEngStore!
    Please Selection an option below (1-5):
    1. List all products that are out of stock.
    2. Find the total number of orders placed by each customer.
    3. Display the details of the most expensive product ordered in each
       order.
    4. Retrieve a list of products that have never been ordered.
    5. Show the total revenue (price * quantity) generated by each
       supplier                                                                                                      
    """)
    selection = input("Please enter your selection:\n")

conn = connect_to_database()
revenueBySupplier(conn)