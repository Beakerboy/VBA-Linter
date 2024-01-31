[![Coverage Status](https://coveralls.io/repos/github/Beakerboy/VBA-Linter/badge.svg?branch=main)](https://coveralls.io/github/Beakerboy/VBA-Linter?branch=main) [![Python package](https://github.com/Beakerboy/VBA-Linter/actions/workflows/python-package.yml/badge.svg)](https://github.com/Beakerboy/VBA-Linter/actions/workflows/python-package.yml)
# VBA-Linter
Lint VBA code

Check that code parses correctly. If so, check that the formatting meets a specified standard.

## Formatting Checks

### 100 Character errors
* 114 Excess whitespace after keywords
* 115 Tabs after keywords
* 120 Missing whitespace before '('
* 121 Excess whitespace before '('
* 122 Tabs before '('
* 123 Missing whitespace after '('
* 124 Excess whitespace after '('
* 125 Tabs after '('
* 130 Missing whitespace before ')'
* 131 Excess whitespace before ')'
* 132 Tabs before ')'
* 133 Missing whitespace after ')'
* 134 Excess whitespace after ')'
* 135 Tabs after ')'
* 140 Missing whitespace before ','
* 141 Excess whitespace before ','
* 142 Tabs before ','
* 143 Missing whitespace after ','
* 144 Excess whitespace after ','
* 145 Tabs after ','
* 150 Whitespace characters before '='
* 151 Tabs before '='
* 152 Whitespace characters after '='
* 153 Tabs after ':='
* 160 Whitespace characters before ':='
* 161 Tabs before ':='
* 162 Whitespace characters after ':='
* 163 Tabs after ':='
* 170 Whitespace characters before arithmetic operator
* 171 Tabs before arithmetic operator
* 172 Whitespace characters after arithmetic operator
* 173 Tabs after arithmetic operator
* 180 Whitespace characters before comparison operator
* 181 Tabs before comparison operatoe
* 182 Whitespace characters after comparison operator
* 183 Tabs after comparison operator
### 200 Parameter errors
* 110 Missing Let
* 111 Optional Let
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
* 310 Incorrect line ending
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
* missing final eol
* 601 missing module attributes
* 602 Missing module declarations
### 800 Documentation
* Missing function documentation
* Missing module documentation
### 900 Syntax Errors
* 910 Line longer than 1023
* 999 Syntax Error
