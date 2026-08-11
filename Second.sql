use EmergencySOS;

--TOTAL NUMBER OF INCIDENTS

SELECT COUNT(*) AS Total_Incidents FROM Emergency_Incidents;

--COUNT OF INCIDENTS BY PRIORITY

SELECT Priority, COUNT(*) Incident_Count FROM Emergency_Incidents 
GROUP BY Priority
ORDER BY Incident_Count
DESC;

-- MOST COMMON EMERGENCY DESCRIPTION 

SELECT TOP 10 Description, COUNT(*) AS Incident_Count FROM Emergency_Incidents
GROUP BY Description
ORDER BY Incident_Count
DESC;

--INCIDENTS BY DISTRICT 

SELECT District, COUNT(*) AS Incident_Count
FROM Emergency_Incidents
GROUP BY District 
ORDER BY Incident_Count
DESC;

--INCIDENTS BY NEIGHBOURHOOD 

SELECT TOP 10 Neighborhood, COUNT(*) AS Incident_Count
FROM Emergency_Incidents
WHERE Neighborhood IS NOT NULL
GROUP BY Neighborhood
ORDER BY Incident_Count
DESC;

-- CHECKS INCIDENT DATES 
SELECT MIN(Call_Date_Time) AS Earliest_Incident,
       MAX(Call_Date_Time) AS Latest_Incident
       FROM Emergency_Incidents


-- INCIDENTS BY HOUR - emergency incidents occured during each hour of the day 

SELECT 
    DATEPART(HOUR, Call_Date_Time) AS Incident_Hour,
    COUNT(*) AS Incident_Count
FROM Emergency_Incidents
WHERE Call_Date_Time IS NOT NULL
GROUP BY DATEPART(HOUR, Call_Date_Time)
ORDER BY Incident_Hour;


-- INCIDENTS BY MONTH - emergency incident recorded each month 

SELECT 
    MONTH(Call_Date_Time) AS Incident_Month,
    COUNT(*) AS Incident_Count
FROM Emergency_Incidents
WHERE Call_Date_Time IS NOT NULL
GROUP BY MONTH(Call_Date_Time)
ORDER BY Incident_Month;

-- INCIDENTS BY DAY OF WEEK
--days with number of emergency incidents.
SELECT 
DATENAME(WEEKDAY,Call_Date_Time) AS DAY_Name,
COUNT(*) AS
Incident_Count
FROM Emergency_Incidents
WHERE Call_Date_Time IS NOT NULL
GROUP BY DATENAME(WEEKDAY,Call_Date_Time)
ORDER BY Incident_Count
DESC;


-- INCIDENTS BY POLICE DISTRICT - police districts with highes

SELECT 
    PoliceDistrict,
    COUNT(*) AS Incident_Count
FROM Emergency_Incidents
WHERE PoliceDistrict IS NOT NULL
GROUP BY PoliceDistrict
ORDER BY Incident_Count 
DESC;


-- TOP 10 INCIDENT LOCATIONS -- 10 locations where the highest number of emergency incidents were reported.

SELECT TOP 10
    Incident_Location,
    COUNT(*) AS Incident_Count
FROM Emergency_Incidents
WHERE Incident_Location IS NOT NULL
GROUP BY Incident_Location
ORDER BY Incident_Count DESC;



--SUMMARY VIEW 

USE EmergencySOS;
GO

CREATE VIEW vw_Incident_Summary AS
SELECT
    Priority,
    District,
    PoliceDistrict,
    Description,
    Neighborhood,
    Call_Date_Time,
    Incident_Location
FROM Emergency_Incidents;


SELECT TOP 10 *
FROM vw_Incident_Summary;

