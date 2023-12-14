import mysql.connector
import re
import datetime
import time

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host= HOST,
            port='3306',
            user=USER,
            password=PASSWORD,
            database='FSEEngStore' #This is the name of the DB you connecting to.
        )
        print(f'Connected to DB.')
        return conn

    except mysql.connector.Error as e:
        print(f'Error connecting to MySQL: {e}')
        return None

def validate_date(date_string):
    pattern = "^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, date_string):
        return True
    else:
        return False



###Customer Population
# customers = [['Purple Shopper', 'Tim Allen', '541 Purple St.', 'VilleEco','EV5421', 'EcoCounty'], ['Bary\'s', 'Barry Allen', '751 Speed St.', 'Star City','EV9999', 'DCUniverse'],
#              ['THE Customer', 'Timmy Turner', '641 Violet St.', 'Nikelodean City','EV5421', 'EcoCenter'], ['Sparrow\'s', 'Johnny Depp', '901 Pirate Ln.', 'Whiskey','EV7765', 'Carribean'],
#              ['Greenish Buyer', 'Bruce Banner', '521 Brown St.', 'Angryville','EV5621', 'USEco'], ['Uncle Ben\'s', 'Peter Parker', '871 Spidy St.', 'Tingleville','EV9103', 'Marvel'],
#              ['TVA', 'Loki Elderson', '311 Time St.', 'Chicago','EV5691', 'EdgeOfTime'], ['Green\'s', 'Oliver Queen', '562 Bow Ln.', 'Star City','EV5522', 'DCUniverse'],
#              ['Stark Industries', 'Tony Stark', '541 31st St.', 'New York','EV8832', 'USA'], ['Doc Oct\'s', 'Otto Octavius', '541 Arms St.', 'New York','EV5521', 'EcoCounty']]
#
#

##Supplier Population
# suppliers = [['Greenie Supplies', 'Johnny Green', '913 Blue St.', 'VilleEco','EV5421', 'EcoCounty', '411-555-2351'], ['Purple Stains', 'Jimmy John', '612 Dark Ln.', 'EcoVille','EV5421', 'EcoCountry', '552-612-0098'],
#              ['FriendsToEco LLC.', 'Tree Hugger', '613 Tree St.', 'TreeVille','TR6612', 'TreeEco', '621-980-7771'], ['Brownie Evo.', 'Long John', '201 Brown St.', 'VilleEco','EV5421', 'EcoCounty', '445-966-0192'],
#              ['TB12', 'Tom Brady', '913 Boston St.', 'Tampa','EV1212', 'Traitor', '642-676-0980'], ['No Bleach Here', 'Tim Howard', '712 Germ St.', 'GermVille','EV5113', 'GermanCounty', '556-124-6642'],
#              ['Enviorment Lovers', 'Taylor Swift', '913 Billionaire St.', 'MoneyVille','EV0000', 'EcoCounty', '421-554-2221'], ['Blueie Supplies', 'Bluie John', '951 Purple St.', 'PurpVille','EV5511', 'EcoCounty', '955-521-6122'],
#              ['Clean Ocean Peeps', 'Biggie Blue', '913 Orange St.', 'OceanVille','EV5332', 'OceanCounty', '911-653-2234'], ['No Waste Company', 'Jeffery Bozo', '511 Lane Ln.', 'EwVille','EV1234', 'EcoCounty', '611-512-6112']]
#
#


# ###Product Population
# products = [['Organic Underwear', 'Clothing'], ['Reusable Toilet Paper', 'Personal Care'], ['Reclaimed Cutting Boards', 'Cooking'], ['Oranic Wool Socks', 'Clothing'],
#             ['Organic Backpack', 'Outdoor'], ['Paper Straws', 'Commercial'], ['No Chemical Soap', 'Personal Care'], ['Organic Sweatshirt', 'Clothing'],
#             ['Organic Utensils', 'Cooking'], ['Reuseable Staw', 'Cooking']]
#
# import random
# conn = connect_to_database()
# for product in products:
#     randomSupplier = random.randint(1, 12)
#     randomPrice = round(random.uniform(5.00, 75.00), 2)
#     randomUnits = random.randint(0, 3000)
#     cursor = conn.cursor()
#     query = ("INSERT INTO Products (ProductName, SupplierID, Category, UnitPrice, UnitsInStock) VALUES (%s, %s, %s, %s, %s)")
#     cursor.execute(query, (product[0],randomSupplier, product[1], randomPrice, randomUnits))
#     conn.commit()




# import datetime
# ###Populate Orders
# orders = [[datetime.date(2023, 11, 1), datetime.date(2023, 11, 14)], [datetime.date(2023, 7, 11), datetime.date(2023, 7, 17)],
#           [datetime.date(2023, 9, 5), datetime.date(2023, 9, 9)], [datetime.date(2023, 3, 12), datetime.date(2023, 3, 17)],
#           [datetime.date(2023, 6, 11), datetime.date(2023, 6, 19)], [datetime.date(2023, 4, 10), datetime.date(2023, 4, 12)],
#           [datetime.date(2023, 2, 9), datetime.date(2023, 2, 15)], [datetime.date(2023, 2, 9), datetime.date(2023, 2, 11)],
#           [datetime.date(2023, 4, 5), datetime.date(2023, 4, 12)], [datetime.date(2023, 6, 13), datetime.date(2023, 6, 17)],
#           [datetime.date(2023, 7, 3), datetime.date(2023, 7, 10)], [datetime.date(2023, 3, 6), datetime.date(2023, 6, 12)]]
#
# import random
# conn = connect_to_database()
# for order in orders:
#     randCustomer = random.randint(1, 13)
#     cursor = conn.cursor()
#     customerQuery = f"Select * FROM Customers WHERE CustomerID = {randCustomer}"
#     cursor.execute(customerQuery)
#     data = cursor.fetchone()
#     query = ("INSERT INTO Orders (CustomerID, OrderDate, ShipDate, ShipAddress, ShipCity, ShipPostalCode, ShipCountry) VALUES (%s, %s, %s, %s, %s,%s,%s)")
#     cursor.execute(query,(randCustomer,order[0], order[1], data[3], data[4], data[5], data[6]))
#     conn.commit()


#####Populate OrderDetails
# import random
# numOrders = 16
# conn = connect_to_database()
# randNumProd = random.randint(1, 5)
# for i in range(1, numOrders+1):
#     for j in range(0,randNumProd+1):
#         randProd = random.randint(1, 15)
#         randQuant = random.randint(1, 10)
#         cursor = conn.cursor()
#         productQuery = f"Select UnitPrice FROM Products WHERE ProductID = {randProd}"
#         cursor.execute(productQuery)
#         data = cursor.fetchone()
#         query = ("INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice) VALUES (%s, %s, %s, %s)")
#         cursor.execute(query, (i, randProd, randQuant, data[0]))
#         conn.commit()




def queryCustomers(conn):
    try:
        cursor = conn.cursor()
        query = "SELECT * From Customers"
        cursor.execute(query)
        for ID,CustName, contactName, address, city, postalCode, Country in cursor:
            print(f"Customer ID: {ID} | Contact Name: {contactName} | Address: {address} | City: {city} | Postal Code: {postalCode} | Contry: {Country}")
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')

def outOfStock(conn):
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
            print("The following products are out of stock:")
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
        #Checking if the data is empty meaning no customers have ordered anything
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
        # sub query to find customers and be able to relay product information
        query = ("SELECT DISTINCT OD.OrderID, P.ProductID, P.ProductName, P.UnitPrice "
                 "FROM OrderDetails OD join Products P on OD.ProductID = P.ProductID "
                 "WHERE (OD.OrderID, OD.UnitPrice) IN ("
                 "SELECT OrderID, MAX(UnitPrice) FROM OrderDetails GROUP BY OrderID);")
        cursor.execute(query)
        data = cursor.fetchall()
        #Checking for an empty return
        if len(data) == 0:
            print("There are no items that match this criteria.")
        else:
            print("Most Expensive Items Per Order:")
            for orderID, prodID, prodName, price in data:
                print(f'Order #{orderID}: Product ID {prodID} | Product Name: {prodName} | Product Price: ${price}')
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')

def itemsNeverOrdered(conn):
    cursor = conn.cursor()
    #Using the same sub query, but checking for things not in.
    query = ("SELECT P.ProductID, P.ProductName, P.UnitPrice FROM Products P "
             "left join OrderDetails OD on P.ProductID = OD.ProductID "
             "WHERE P.ProductID NOT IN ("
             "SELECT DISTINCT ProductID FROM OrderDetails);")
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        if len(data) == 0:
            print("Every Item has been Ordered!!")
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
            print("All items have been ordered at least once!")
        else:
            print("Supplier's Revenue:")
            for supplierID, supplierName, revenue in data:
                print(f'Supplier ID: {supplierID} | Supplier Name: {supplierName} | Total Sales Revenue: ${revenue}')
    except mysql.connector.Error as e:
        print(f'Error creating a record {e}')


def newOrderDetails(conn, orderID):
    cursor = conn.cursor()
    #creating a dict to be able to store item and number of items they are ordering.
    orderedItems = {}
    more = True
    #This allows for multiple order entries instead of reprompting
    while more == True:
        #checking if the product entered exsists
        productOrdered = int(input('Enter the product ID of the ordered Item:\n'))
        quantity = int(input('Enter the quantity ordered:\n'))
        query = f"SELECT UnitsInStock FROM Products WHERE ProductID = {productOrdered}"
        cursor.execute(query)
        prodcutDetails = cursor.fetchone()
        #Conditional to tell that we do not have the item
        if prodcutDetails == None:
            print('We do not have a product with that ID.')
            continue
        #Checking stock of item they are trying to order.
        elif prodcutDetails[0] == 0:
            print("We are out of stock on that product.")
            continue
        #Allows for the person to order only what we have in stock.
        while quantity > prodcutDetails[0]:
            quantity = int(input(f'We only have {prodcutDetails[0]} in stock. Please enter a new quantity:\n'))
        #if all conditions are met, store the item in the dictionary
        orderedItems[productOrdered] = quantity
        moreProd = input('Did they order more items? (Y/N):')
        if moreProd.lower() == 'y':
            more = True
        elif moreProd.lower() == 'n':
            more = False
    #loop through and create each record for all items, and store in Order Details
    for item in orderedItems:
        query = f"SELECT UnitPrice FROM Products WHERE ProductID = {item}"
        cursor.execute(query)
        price = cursor.fetchone()
        #Calls Stored Prodcedure
        cursor.callproc('NewOrderDetails', (orderID, item, orderedItems[item], price[0]))
        conn.commit()
        print("Your records have been added to OrderDetails")

def newOrder(conn):
    cursor = conn.cursor()
    import datetime
    custID = input("Please enter the Customer ID:\n")
    validID = False
    #Checks for a valid CustomerID
    while validID == False:
        try:
            int(custID)
            validID = True
        except:
            custID = (input("Please enter a valid Customer ID:\n"))
    query = f"SELECT * FROM Customers WHERE CustomerID = {custID}"
    cursor.execute(query)
    data = cursor.fetchone()
    #Keeps asking for a valid customerID
    while data == None:
        custID = (input("We do not have a customer with that ID try again:\n"))
        validID = False
        while validID == False:
            try:
                int(custID)
                validID = True
            except:
                custID = (input("Please enter a valid Customer ID:\n"))
        query = f"SELECT * FROM Customers WHERE CustomerID = {custID}"
        cursor.execute(query)
        data = cursor.fetchone()
    #Getting and checking Dates for ordering and shipping
    orderDate = (input("Please enter the order date (YYYY-MM-DD):\n"))
    orderDateValid = False
    while orderDateValid == False:
        try:
            orderDate = datetime.date(*map(int, orderDate.split('-')))
            orderDateValid = True
        except:
            orderDate = (input("Please enter a valid order date (YYYY-MM-DD):\n"))
    shipDate = input("Please enter the ship date (YYYY-MM-DD):\n")
    shipDateValid = False
    while shipDateValid == False:
        try:
            shipDate = datetime.date(*map(int, shipDate.split('-')))
            shipDateValid = True
        except:
            shipDate = (input("Please enter a valid order date (YYYY-MM-DD):\n"))
    #Query customer so address information can be populated without prompting
    query = f"SELECT Address, City, PostalCode, Country FROM Customers WHERE CustomerID = {custID}"
    cursor.execute(query)
    data = cursor.fetchone()
    #Calls stored procedure for a new order
    cursor.callproc('NewOrder', (custID, orderDate, shipDate, data[0], data[1], data[2], data[3]))
    conn.commit()
    print('Your record has been created in Orders.')
    time.sleep(.5)
    #queries the most recent order from the customer to put into orderdetail function
    query = f"SELECT OrderID FROM Orders WHERE CustomerID = {custID} ORDER BY OrderID DESC LIMIT 1"
    cursor.execute(query)
    data = cursor.fetchone()
    #call and run for orderdetail population
    newOrderDetails(conn, data[0])

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
    """
    )
    stay = True
    while stay == True:
        selection = input(
    """
    Please Selection an option below (1-7):
    1. List all products that are out of stock.
    2. Find the total number of orders placed by each customer.
    3. Display the details of the most expensive product ordered in each
        order.
    4. Retrieve a list of products that have never been ordered.
    5. Show the total revenue (price * quantity) generated by each
        supplier  
    6. Create a new order
    7. Exit                                                                                                    
    """)
        validInput = False
        while validInput == False:
            try:
                selection = int(selection)
                if selection < 1 or selection > 7:
                    selection = input('Please input a valid selection:\n')
                else:
                    validInput = True
            except ValueError:
                selection = input('Please input a valid selection:\n')
        if selection == 1:
            outOfStock(conn)
        elif selection == 2:
            orderCountByCustomer(conn)
        elif selection == 3:
            maxItemPerOrder(conn)
        elif selection == 4:
            itemsNeverOrdered(conn)
        elif selection == 5:
            revenueBySupplier(conn)
        elif selection == 6:
            newOrder(conn)
        elif selection == 7:
            stay = False
    print("Thank you for visiting the FSEEngineering Store.")


main()



