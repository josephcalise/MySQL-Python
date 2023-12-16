create table Customers
(
    CustomerID   int auto_increment
        primary key,
    CustomerName varchar(255) not null,
    ContactName  varchar(255) null,
    Address      varchar(255) null,
    City         varchar(100) null,
    PostalCode   varchar(20)  null,
    Country      varchar(100) null
);

