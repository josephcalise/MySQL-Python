create table OrderDetails
(
    OrderDetailID int auto_increment
        primary key,
    OrderID       int            null,
    ProductID     int            null,
    Quantity      int            null,
    UnitPrice     decimal(10, 2) null,
    constraint OrderDetails_ibfk_1
        foreign key (OrderID) references Orders (OrderID),
    constraint OrderDetails_ibfk_2
        foreign key (ProductID) references Products (ProductID)
);

create index OrderID
    on OrderDetails (OrderID);

create index ProductID
    on OrderDetails (ProductID);

