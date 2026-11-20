# Airline Flight Delay & On-Time Performance Analysis

A Python project that studies flight delays to find bottleneck airports, worst routes and delay patterns.

**Tools:** Python 3, pandas, NumPy
**Dataset:** 14_flight_delays.csv (900 flights after removing duplicates)

## What the project does
- Cleans the data (missing values, duplicates, dates)
- Calculates total flights, average departure delay and on-time percentage
- Ranks airports and finds the 10 worst routes
- Compares delays by time of day and by delay cause
- Finds cancellation and diversion percentage by airline
- Calculates correlation, median, standard deviation, 90th percentile and outliers
- Groups delays by severity (On-Time, Minor, Moderate, Severe)
- Gives five recommendations to improve schedule reliability

## Key results
- Average departure delay: 28.73 minutes, on-time flights: 40.56%
- Most delayed origin airport: BOM (31.6 minutes)
- Worst valid route: DEL to CCU (44.3 minutes)
- Correlation between departure and arrival delay is weak (0.07)

## Files
- Smriti-Shakya_airline-flight-analysis_SRS: Software Requirements Specification
- Smriti-Shakya_SourceCode: Source code of the project

## Author
Smriti Shakya | Admission No.:2026B15410168  | Email: smriti.26b15410168@abes.ac.in
