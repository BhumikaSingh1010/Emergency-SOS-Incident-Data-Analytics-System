use EmergencySOS;

--  Total COunt 
SELECT COUNT(*) AS Total_Records FROM dbo.Emergency_Incidents;

-- checking records and columns 
SELECT TOP 10 * FROM dbo.Emergency_Incidents;


-- Checking Table structure

SELECT COLUMN_NAME,
       DATA_TYPE, 
       CHARACTER_MAXIMUM_LENGTH 
       FROM 
       INFORMATION_SCHEMA.COLUMNS 
       WHERE TABLE_NAME = 'Emergency_Incidents' 
       ORDER BY ORDINAL_POSITION


-- Creating the sos reports table 

 CREATE TABLE SOS_Reports (
     SOS_ID INT IDENTITY(1,1) PRIMARY KEY,
     Report_Date_Time DATETIME NOT NULL,
     User_Name VARCHAR(100),
     Phone_Number VARCHAR(20),
     Emergency_Type VARCHAR(100),
     Location VARCHAR(255),
     Latitute DECIMAL(10,7),
     Longitude DECIMAL(10,7),
     Description VARCHAR(500),
     Priority VARCHAR(50),
     Status VARCHAR(50) DEFAULT 'Pending');


     SELECT TOP 10 * FROM SOS_Reports;

--- INSERTING RECORD INTO IT
 
 INSERT INTO SOS_Reports
(
    Report_Date_Time,
    User_Name,
    Phone_Number,
    Emergency_Type,
    Location,
    Latitute,
    Longitude,
    Description,
    Priority,
    Status
)
VALUES
(
    GETDATE(),
    'Test User',
    '9999999999',
    'Accident',
    'Main Road',
    21.2514,
    81.6296,
    'Vehicle accident reported',
    'High',
    'Pending'
);

SELECT *
FROM SOS_Reports;


EXEC sp_rename
    'SOS_Reports.Latitute',
    'Latitude',
    'COLUMN';

SELECT *
FROM SOS_Reports;