DROP TABLE IF EXISTS Opening;
DROP TABLE IF EXISTS Shortage;
DROP TABLE IF EXISTS Price;
DROP TABLE IF EXISTS StationService;
DROP TABLE IF EXISTS Closing;
DROP TABLE IF EXISTS Slot;
DROP TABLE IF EXISTS Day;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Service;
DROP TABLE IF EXISTS Station;


CREATE TABLE Station(
    id INT NOT NULL PRIMARY KEY,
    address VARCHAR(250) NOT NULL,
    city VARCHAR(50) NOT NULL,
    postalcode CHAR(5) NOT NULL,
    gps POINT,
    position ENUM('A','R','N') NOT NULL,
    automate BOOLEAN NOT NULL,
);

CREATE TABLE Service(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(250) NOT NULL
);

CREATE TABLE Product(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE Day(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE Slot(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    start TIME NOT NULL,
    end TIME NOT NULL,
    UNIQUE (start , end),
    CHECk ( end > start)
);

CREATE TABLE Closing(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type ENUM('D','T') NOT NULL,
    start DATETIME NOT NULL,
    end DATETIME,
    stationId INT NOT NULL,
    FOREIGN KEY (stationId) REFERENCES Station(id)
);

CREATE TABLE StationService(
    stationId INT NOT NULL,
    serviceId INT NOT NULL,
    FOREIGN KEY (stationId) REFERENCES Station(id),
    FOREIGN KEY (serviceId) REFERENCES Service(id),
    PRIMARY KEY(stationId , serviceId)
    
);

CREATE TABLE Price(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    stationId INT NOT NULL,
    productId INT NOT NULL,
    date DATETIME NOT NULL,
    value FLOAT NOT NULL,
    FOREIGN KEY (stationId) REFERENCES Station(id),
    FOREIGN KEY (productId) REFERENCES Product(id)

);


CREATE TABLE Shortage(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    stationId INT NOT NULL,
    productId INT NOT NULL,
    start DATETIME NOT NULL,
    end DATETIME,
    FOREIGN KEY (stationId) REFERENCES Station(id),
    FOREIGN KEY (productId) REFERENCES Product(id)

);

CREATE TABLE Opening(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    stationId INT NOT NULL,
    dayId INT NOT NULL,
    slotId INT NOT NULL,
    FOREIGN KEY (stationId) REFERENCES Station(id),
    FOREIGN KEY (dayId) REFERENCES Day(id),
    FOREIGN KEY (slotId) REFERENCES Slot(id)
);
