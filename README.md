[![Coverage Status](https://coveralls.io/repos/github/Beakerboy/VBA-Linter/badge.svg?branch=main)](https://coveralls.io/github/Beakerboy/VBA-Linter?branch=main)
# VBA-Linter
Lint VBA code

Check that code parses correctly. If so, check that the formatting meets a specified standard.

## Formatting Checks

### W2 Whitespace warning
* W201 no newline at end of file
* W291 trailing whitespace

### W3 Blank line warning
* W300 blank line at end of file

### W5 Line break warning
* W500 incorrect line ending
* W501 line too long

## To Do
* E201 Whitespace after (
* E202 Whitespace before )
* E203 whitespace before ‘,’
* E211 Whitespace before (
* E221 multiple spaces before operator
* E222 multiple spaces after operator
* E712 comparison to True should be ‘If cond Then’
* E713 comparison to False should be 'If Not cond Then'
* W100 indentation contains spaces
* W101 improper indentation level
* W202 blank line contains whitespace
* W301 Too few blank lines before function
* W302 Too many blank lines before function
* N800 Keyword formating
* N801 Module name format
* N802 Function name format
* N803 Variable name format
* Missing Strict
* Variable not initialized
* return type not specified
* parameter type not specified
* missing function docbloc
