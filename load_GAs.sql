LOAD DATA LOCAL INFILE '/Users/ryanletto/Desktop/WT2/Django Experimentation/indicatorVC/GA.csv'
INTO TABLE indicators_graduateattribute
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(GA_id, title);
