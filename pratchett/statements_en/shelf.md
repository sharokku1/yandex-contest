# Problem: Mother's Shelf

Next to the big black stove there was a shelf. Tiffany's mother still called it  
"Mother Bolen's Library", because she liked to think they had a library at home.  
Everyone else simply said "Mother's shelf".

There were five books on the shelf (not counting the Account Book).  
We will treat each shelf as a string and each book as a block of 5 characters.

You must clean up the shelves according to a specific rule.

## Processing rules

For every input line (except the final stop line):

1. Split the line into consecutive groups of 5 characters ("books").  
2. For every **second** group (i.e. groups with indices 1, 3, 5, ... if counted from 0),  
   reverse the group and convert all its letters to uppercase.  
3. Consider each group as a string. Keep only **unique** groups (remove duplicates,  
   keeping the first occurrence).  
4. Sort the remaining groups in lexicographical order.  
5. Output the concatenation of all groups as a single string.

## Input format

The input consists of several lines.

- Each line represents one shelf.  
- The last line is the string `URGENT MATTER` — it marks the end of input and is **not** processed.

If at any moment you read a line whose length is **not divisible by 5**, you must

- output the line `NOT ENOUGH BOOKS`, and  
- stop processing further input immediately (even if there are more lines after it).

## Output format

For every processed line (except the final `URGENT MATTER`), output the transformed string as described above, each on its own line.

If an invalid line is encountered (length not a multiple of 5), output  
`NOT ENOUGH BOOKS` and terminate.

## Example 1

Input:

MotherBolens Library  
MothersRegiment  
There were fivebooksontheshelf  
Year books  
Diseasesofsheep  
URGENT MATTER  

Output:

ELOBRMotheYRARBns Li  
GERSRMotheiment  
 fiveEREW FLEHSSKOOBThereonthe  
SKOOBYear  
DiseaFOSESsheep  

## Example 2

Input:

Nexttothebook about sheep  
was a thin book  
called  
Flowers of the hills  
URGENT MATTER  

Output:

 TUOBBEHTONexttook asheep  
 bookNIHT was a  
NOT ENOUGH BOOKS
