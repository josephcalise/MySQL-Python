create
    definer = root@`%` procedure NewOrder(IN sp_customerID int, IN sp_orderDate date, IN sp_shipDate date,
                                          IN sp_address varchar(50), IN sp_city varchar(50), IN sp_postal varchar(6),
                                          IN sp_country varchar(50))
BEGIN
    INSERT INTO Orders(CustomerID, OrderDate, ShipDate, ShipAddress, ShipCity, ShipPostalCode, ShipCountry)
        VALUES (sp_customerID, sp_orderDate,sp_shipDate,sp_address,sp_city,sp_postal,sp_country);
end;

