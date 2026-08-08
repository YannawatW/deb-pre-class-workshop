CREATE TABLE weather (
    city    VARCHAR,
    temp_lo INTEGER, -- minimum temperature on a day
    temp_hi INTEGER, -- maximum temperature on a day
    prcp    FLOAT, -- precipitation (น้ำในบรรยากาศที่ควบแน่นและตกลงมาสู่พื้นโลก)
    date    DATE
);

CREATE TABLE cities (
    name VARCHAR,
    lat  DECIMAL,
    lon  DECIMAL
);

COPY weather FROM 'weather.csv';
COPY cities FROM 'cities.csv';
