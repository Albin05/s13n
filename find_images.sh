#!/bin/bash

API_KEY="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"

search_images() {
  local query="$1"
  local label="$2"
  result=$(curl -s -X POST "https://api.tavily.com/search" \
    -H "Content-Type: application/json" \
    -d "{\"api_key\": \"$API_KEY\", \"query\": \"$query\", \"search_depth\": \"basic\", \"include_images\": true, \"max_results\": 5}" \
    | python3 -c "import json,sys; data=json.load(sys.stdin); imgs=data.get('images',[]); print(imgs[0] if imgs else 'NOT_FOUND')" 2>/dev/null)
  echo "$label: $result"
}

echo "=== Searching images for all 29 Python LOs ==="

search_images "python variable assignment memory diagram site:geeksforgeeks.org OR site:realpython.com" "LO1_Variables"
search_images "PEP 8 python naming conventions snake_case code style guide diagram" "LO2_PEP8"
search_images "python integer data type number line diagram tutorial" "LO3_Integer"
search_images "python float decimal floating point representation diagram" "LO4_Float"
search_images "python string characters indexing diagram site:geeksforgeeks.org OR site:freecodecamp.org" "LO5_String"
search_images "python boolean true false values diagram site:geeksforgeeks.org" "LO6_Boolean"
search_images "python type() function dynamic typing diagram tutorial" "LO7_Type"
search_images "python type conversion casting int str float diagram site:geeksforgeeks.org" "LO8_Conversion"
search_images "python input() function user input diagram tutorial site:geeksforgeeks.org" "LO9_Input"
search_images "python f-string format string placeholder tutorial diagram" "LO10_Fstrings"
search_images "python arithmetic operators addition subtraction division diagram table" "LO11_Arithmetic"  
search_images "python operator precedence PEMDAS order of operations diagram" "LO12_Precedence"
search_images "python comparison operators == != < > <= >= diagram table" "LO13_Comparison"
search_images "python logical operators AND OR NOT boolean diagram" "LO14_Logical"
search_images "python if statement conditional flowchart diagram site:geeksforgeeks.org" "LO15_If"
search_images "python elif else if multiple conditions flowchart diagram" "LO16_Elif"
search_images "python else statement default branch flowchart diagram" "LO17_Else"
search_images "python nested if else conditions flowchart diagram" "LO18_Nested_If"
search_images "python while loop flowchart diagram site:geeksforgeeks.org OR site:freecodecamp.org" "LO19_While"
search_images "python break statement loop exit flowchart diagram site:geeksforgeeks.org" "LO20_Break"
search_images "python continue statement loop skip flowchart diagram site:geeksforgeeks.org" "LO21_Continue"
search_images "python for loop iterating sequence flowchart diagram tutorial" "LO22_For"
search_images "python range function start stop step diagram tutorial site:geeksforgeeks.org" "LO23_Range"
search_images "python break continue in for loop control diagram site:geeksforgeeks.org" "LO24_ForControl"
search_images "python nested loops inner outer loop grid pattern diagram" "LO25_NestedLoops"
search_images "python function definition syntax def body diagram tutorial" "LO26_Functions"
search_images "python function parameters arguments input diagram tutorial" "LO27_Parameters"
search_images "python return statement function output diagram tutorial" "LO28_Return"
search_images "python default parameter values function definition diagram tutorial" "LO29_Default"

