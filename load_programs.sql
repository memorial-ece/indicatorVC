LOAD DATA LOCAL INFILE '/Users/ryanletto/Desktop/WT2/Django Experimentation/indicatorVC/Program.csv'
INTO TABLE indicators_program
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(program_id, name);
