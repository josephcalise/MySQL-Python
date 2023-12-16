create table Products
(
    ProductID    int auto_increment
        primary key,
    ProductName  varchar(255)   not null,
    SupplierID   int            null,
    Category     varchar(100)   null,
    UnitPrice    decimal(10, 2) null,
    UnitsInStock int            null,
    constraint Products_ibfk_1
        foreign key (SupplierID) references Suppliers (SupplierID)
);

create index SupplierID
    on Products (SupplierID);

