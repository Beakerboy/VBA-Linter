[![Coverage Status](https://coveralls.io/repos/github/Beakerboy/VBA-Linter/badge.svg?branch=main)](https://coveralls.io/github/Beakerboy/VBA-Linter?branch=main) [![Python package](https://github.com/Beakerboy/VBA-Linter/actions/workflows/python-package.yml/badge.svg)](https://github.com/Beakerboy/VBA-Linter/actions/workflows/python-package.yml)
# VBA-Linter
Lint VBA code

Check that code parses correctly. If so, check that the formatting meets a specified standard.

## Formatting Checks

### E1 Indentation
* E101 indentation contains mixed spaces and tabs
### E2 Whitespace errors
* E201 whitespace after '('
* E202 whitespace before ')'
* E203 whitespace before ‘,’
* E211 whitespace before (
### W1 Indentation warning
* W191 indentation contains tabs - should be error.
### W2 Whitespace warning
* W201 no newline at end of file
* W291 trailing whitespace
* W293 blank line contains whitespace

### W3 Blank line warning
* W391 blank line at end of file

### W5 Line break warning
* W500 incorrect line ending
* W501 line too long

## To Do
* E221 multiple spaces before operator
* E222 multiple spaces after operator
* E712 comparison to True should be ‘If cond Then’
* E713 comparison to False should be 'If Not cond Then'
* F841 local variable 'foo' is assigned to but never used
* W101 improper indentation level
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
