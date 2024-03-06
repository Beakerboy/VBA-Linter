[![Coverage Status](https://coveralls.io/repos/github/Beakerboy/VBA-Linter/badge.svg?branch=main)](https://coveralls.io/github/Beakerboy/VBA-Linter?branch=main) [![Python package](https://github.com/Beakerboy/VBA-Linter/actions/workflows/python-package.yml/badge.svg)](https://github.com/Beakerboy/VBA-Linter/actions/workflows/python-package.yml)
# VBA-Linter
Lint VBA code

Check that code parses correctly. If so, check that the formatting meets a specified standard.

## Formatting Checks

### 100 Character errors
* 110 Whitespace contains tabs
* 114 Excess whitespace between keywords
* 120 Missing whitespace before '('
* 121 Excess whitespace before '('
* 124 Excess whitespace after '('
* 131 Excess whitespace before ')'
* 133 Missing whitespace after ')'
* 134 Excess whitespace after ')'
* 141 Excess whitespace before ','
* 143 Missing whitespace after ','
* 144 Excess whitespace after ','
* 150 Missing whitespace before '='
* 151 Excess whitespace before '='
* 153 Missing whitespace after '='
* 154 Excess whitespace after '='
* 161 Excess whitespace before ':='
* 164 Excess whitespace after ':='
* 170 Missing whitespace before arithmetic operator
* 171 Excess whitespace before arithmetic operator
* 173 Missing whitespace after arithmetic operator
* 174 Excess whitespace after arithmetic operator
* 180 Missing whitespace before comparison operator
* 181 Excess whitespace before comparison operator
* 183 Missing whitespace after comparison operator
* 184 Excess whitespace after comparison operator
* 191 Excess whitespace before ':'
* 193 Missing whitespace after ':'
### 200 Parameter / Keyword errors
* 201 Missing Let
* 202 Optional Let
* 210 parameter naming
* 220 Keyword not capitalized
* function / sub naming
* property naming
* parameter not defined (option explicit)
* missing parameter type designation
### 300 Expression Errors
* = True
* = False
* Not X = Y
### 400 Line errors
* 400 Incorrect line ending
* 303 Too many blank lines (3)
* 305 Trailing whitespace
* 310 Blank line contains whitespace
* indent
* miltiple statements not allowed
* line continuation
* line length
### 500 Control Structures
* one line if/then/else
### 600 Function Errors
* 510 Missing visibility
* 511 Optional 'Public'
* missing return type designation
### 700 Module Errors
* Blank line begining file
* blank line end of file
* 701 missing final eol
* 601 missing module attributes
* 602 Missing module declarations
### 800 Documentation
* Missing function documentation
* Missing module documentation
### 900 Syntax Errors
* 910 Line longer than 1023
* 999 Syntax Error
