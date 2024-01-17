# python-challenge

PyBank
    For the PyBank challenge, I started by calling the source file directly using the full path as I had issues with the os.path.join and "..". The csvreader methods were the same as what was used in an example from module 3 examples.

    Next, I initialized some variables to hold the desired output values by casting as types I felt were best used for their numeric types. These were to track the number of total months in the document, track the net profit throughout the document, track the greatest profit, and track the greatest loss. These are started at 0 because the values for each row will be compared to some of these variables. Dollar values variables will be cast as float while the month counter will be cast as an integer. At the beginning, these values will need to be 0 for these comparisons to work properly. 

    A for loop is used with csvreader to iterate through each row of the document. The value read from the document will be cast as a float. The loop grabs the current value of the row from the second column and will add that to the net profit. The counter for the number of months evaluated is then incremented. An if statement will be used to determine whether the change for the month is positive or negative. If the current value is positive and above the current greatest value, the value for the greatest profit and the current will be written over the current values. After the for loop is complete, the average change value will be calculated by taking the net profit of the document and divide by the number of months.

    Finally, the output text file will be output with the desired output values. Using "print", we will use the same strings built as writing to the text file to print to the terminal.
    
    The results are
        Financial Analysis
        --------------
        Total Months: 86
        Total: $22564198.0
        Average change: $262374.3953488372
        Greatest increase in profits: Mar-13 $1141840.0
        Total decrease in profits: Dec-10 $-1194133.0

    While these appear different from the screenshot in the module, I checked the sum, min, max, and mean of the profit/loss column and got the following results. Not sure if the pybank file I got was different than what was used for that result but I can confirm at least that the values in the greatest increase and decrease displayed in the module instructions do not appear and those dates in my document have different values.
        sum	22564198
        min	-1194133
        max	1141840
        mean	262374.3953


PyPoll
    For the PyPoll challenge, I started by calling the source file directly using the full path as I had issues with the os.path.join and "..". The csvreader methods were the same as what was used in an example from module 3 examples.

    A vote total counter will be initialized at 0 since we will be incrementing it using "+=" later on. Then a list of canidates and a dictionary for canidate votes will be created.

    A for loop is used with csvreader to iterate through each row of the document. The total votes count will increment each time the loop runs. Then, the loop checks if the current canidate name in column 3 is in the canidates list or not. If not, it will add the canidate's name into the list and the canidate votes dictionary. Their vote count will be initialized at 0. Then, the vote count for the canidate in the dictionary will be incremented.

    Finally, the output text file will be output with the desired output values. A variable to count the highest vote count will be created for comparison in an if statement while outputting canidate results. While printing the results, we will calculate the percentage of votes for each canidate by dividing their votes by the number of total votes. Then, their count of votes will be compared against the current highest count. If it is higher, their name will be updated to the variable holding the winner name and the highest vote count variable will be updated. Using "print", we will use the same strings built as writing to the text file to print to the terminal.

    The results are:
        Election Results
        --------------
        Total Votes: 369711
        --------------
        Charles Casper Stockham: 23.04854332167558% (85213)
        Diana DeGette: 73.81224794501652% (272892)
        Raymon Anthony Doane: 3.1392087333079077% (11606)
        --------------
        Winner: Diana DeGette
        --------------