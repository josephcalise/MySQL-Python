create
    definer = root@`%` procedure NewOrderDetails(IN sp_orderID int, IN sp_productID int, IN sp_quantity int,
                                                 IN sp_unitPrice decimal(10, 2))
BEGIN
    INSERT INTO OrderDetails(OrderID, ProductID, Quantity, UnitPrice)
        VALUES(sp_orderID,sp_productID,sp_quantity,sp_unitPrice);
    call updateStock(sp_productID,sp_quantity);
end;

