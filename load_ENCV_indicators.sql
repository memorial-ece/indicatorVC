LOAD DATA LOCAL INFILE '/Users/ryanletto/Desktop/WT2/Django Experimentation/indicatorVC/ENCV Indicators.csv'
INTO TABLE indicators_indicator
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(program_id, GA_id, tag, description, course_number, course_title, assessment_method, level, bins);
