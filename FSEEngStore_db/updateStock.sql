create
    definer = root@`%` procedure updateStock(IN sp_productID int, IN sp_quantOrdered int)
BEGIN
    UPDATE Products SET UnitsInStock = UnitsInStock - sp_quantOrdered
    Where ProductID = sp_productID;
end;

