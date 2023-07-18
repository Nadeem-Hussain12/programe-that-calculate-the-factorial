# programe-that-calculate-the-factorial
in first code using a function here is a some points 
The code defines a recursive function factorial(n) that calculates the factorial of a given number n. The factorial of a number is the product of all positive integers up to and including that number. The base case of the recursion is when n is 0 or 1, in which case the function returns 1.

The code then prints a header for the table that will display the numbers and their corresponding factorials. It uses the print() function to output the string "Number\tFactorial" followed by a line of dashes for visual separation.

The code uses a for loop with the range() function to iterate through the numbers 1 to 9 (inclusive). This loop will generate the numbers for which the factorials will be calculated and displayed.

Within the loop, the code prints the current number and its corresponding factorial. It uses f-strings (formatted strings) to format the output in a tabular format. The factorial(i) function call calculates the factorial of the current number i.

The loop continues until the range is exhausted, and the table of numbers and their factorials is printed to the console.
Now in the second code i used math library
The code imports the math module, which provides various mathematical functions and constants, including the factorial() function.

The code uses a for loop to iterate through the numbers 1 to 9 (inclusive) using the range() function.

Within the loop, the code calculates the factorial of the current number i using the math.factorial() function. It assigns the factorial value to the variable factorial. The print() function is then used to output a formatted string that displays the number and its corresponding factorial.
