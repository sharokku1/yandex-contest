# Problem: Watching the Little Brother

Winworth is a very sticky child. Whatever he plays with, he somehow ends up sticky again.  
To look after him properly, we need to filter out the activities that are undesirable or dangerous.

## Input format

The input consists of three lines:

1. A separator string.  
2. A connector string.  
3. A single string containing the brother's activities, separated by the given separator.

## Output format

From the list of activities, select only those strings that

- contain the substring `eat`, or  
- contain the substring `sticky`.

Print the selected activities joined by the connector string.

## Example

Input:  

`#`  
`&`  
`eat frogs#play with sticky thistles#build a castle#collect sticky berries#there are lollipops#eating tree bark#sticky key#play game#sticky dandelion`

Output:  

`eat frogs&play with sticky thistles&collect sticky berries&eating tree bark&sticky key&sticky dandelion`
