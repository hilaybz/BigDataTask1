# BigDataTask1
Hadoop Training questions
Please answer the questions below


Exercise 1
Q1. How many files are there?
6 Data files and 1 Success file

Q2. Did number of mapper change?
No - we got 9 launched map tasks in both runs

Q3. Did number of reducer changed?
Yes - it has changed from 3 launched reduce tasks in the first run to 6 in the second run

Q4. Did number of output files change? Why?
Yes - Because hadoop creates one output file for each reducer, since the number of reducers changed, the number of output files changed as well. 

Q5. What does the value of 'Merged Map outputs' represents and how is it calculated?



Exercise 2
Q1. Is your change in the mapper or in the reducer?
The change is in the mapper because the reducer needs to get the words stripped from dots commas and make it case sensitive before it sums them up.

Q2. Please submit your code in GitHub
Added as Q2.py

Exercise 3
Q1. Is your change in the mapper or in the reducer?
Q2. Please submit your code in GitHub
______________________________
Q3. Print the output of the MapReduce and add to the project.
Note: you should not use external pipes, sort, or filters. All should be done inside the mapReduce Python code
I want to see in the screenshot that includes the command you typed:
$ > hadoop fs -ls /user/hduser/gutenberg-output
______________________________
