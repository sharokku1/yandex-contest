# Problem: Hillswords

Grandmother liked old-fashioned words and used them in an old-fashioned way.  
She never said "Chalk Hills" — she said "Hillswords". Tiffany remembered the phrase:  
"In the Hillswords the winds have plenty of room."

We will now work not with words, but with numbers, and select only “special” lengths.

## Input format

- The first line contains an integer `n` — the number of lines with numbers.  
- Each of the next `n` lines contains several integers separated by single spaces.

## Output format

For every line **except the first one**, output the integers that satisfy all of the following:

- they are divisible by 4;  
- they appear in the current line;  
- they do **not** appear in the previous line;  
- each such integer is printed **at most once** for this line.

Print the selected numbers in any order, separated by the string ` * `  
(a space, an asterisk, and a space).  

If there are no suitable numbers for a line, print an empty line.

## Example 1

Input:

6  
8 5 26 3 3 14 20 16  
20 10 1 28 17 32  
24 36 20 6 23  
6 16 13 10 24 44 52  
12 1 6  
5 28 10 14 92 22 2  

Output:

32 * 28  
24 * 36  
44 * 16 * 52  
12  
28 * 92  

## Example 2

Input:

5  
22 16 21 19 1 20 18 3  
10 12 27 21 12 1 72  
27 21 8 12 17 48  
7 1 19 7 15  
9 28 3 1 10 26 13 3  

Output:

72 * 12  
8 * 48
