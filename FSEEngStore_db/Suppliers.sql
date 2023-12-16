create table Suppliers
(
    SupplierID   int auto_increment
        primary key,
    SupplierName varchar(255) not null,
    ContactName  varchar(255) null,
    Address      varchar(255) null,
    City         varchar(100) null,
    PostalCode   varchar(20)  null,
    Country      varchar(100) null,
    Phone        varchar(20)  null
);

