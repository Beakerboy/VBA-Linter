[![Coverage Status](https://coveralls.io/repos/github/Beakerboy/VBA-Linter/badge.svg?branch=main)](https://coveralls.io/github/Beakerboy/VBA-Linter?branch=main) [![Python package](https://github.com/Beakerboy/VBA-Linter/actions/workflows/python-package.yml/badge.svg)](https://github.com/Beakerboy/VBA-Linter/actions/workflows/python-package.yml)
# VBA-Linter
Lint VBA code

Check that code parses correctly. If so, check that the formatting meets a specified standard.

## Formatting Checks

### 100 Character errors
* 110 Whitespace characters between keywords (x>1)
* 111 Tabs between keywords
* 120 Whitespace characters before '('
* 121 Tabs before '('
* 122 Whitespace characters after '('
* 123 Tabs after '('
* 130 Whitespace characters before ')'
* 131 Tabs before ')'
* 132 Whitespace characters after ')'
* 133 Tabs after ')'
* 140 Whitespace characters before ','
* 141 Tabs before ','
* 142 Whitespace characters after ','
* 143 Tabs after ','
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
* naming
* used before defined (option explicit)
* missing type
### 300 Line errors
* Line Ending
* indent
* miltiple statementz
* line continuation
* line length
* E303 Too many blank lines (3)
### 400 Control Structures
* one line if/then/else
### 500 Function Errors
missing visibility
### 600 Module Errors
* Blank line begining file
* blank line end of file
* missing final eol
* missing module sefinition
* missing module options
### 700 Documentation
* Missing function socumentation
* Missing module documentation
### 900 Syntax Errors

