create table Orders
(
    OrderID        int auto_increment
        primary key,
    CustomerID     int          null,
    OrderDate      date         null,
    ShipDate       date         null,
    ShipAddress    varchar(255) null,
    ShipCity       varchar(100) null,
    ShipPostalCode varchar(20)  null,
    ShipCountry    varchar(100) null,
    constraint Orders_ibfk_1
        foreign key (CustomerID) references Customers (CustomerID)
);

create index CustomerID
    on Orders (CustomerID);

