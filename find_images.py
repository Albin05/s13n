import subprocess
import json

API_KEY = "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"

queries = [
    ("LO1_Variables", "python variable assignment memory box diagram site:geeksforgeeks.org OR site:realpython.com"),
    ("LO2_PEP8", "PEP 8 python snake_case naming convention style guide diagram"),
    ("LO3_Integer", "python integer data type whole numbers diagram tutorial"),
    ("LO4_Float", "python float decimal precision floating point number diagram"),
    ("LO5_String", "python string indexing characters sequence diagram geeksforgeeks"),
    ("LO6_Boolean", "python boolean true false values diagram tutorial"),
    ("LO7_Type_func", "python type() function dynamic typing inspect diagram"),
    ("LO8_Conversion", "python type conversion casting int str float diagram geeksforgeeks"),
    ("LO9_Input", "python input() user input function diagram tutorial geeksforgeeks"),
    ("LO10_Fstring", "python f-string formatted string literal diagram tutorial"),
    ("LO11_Arithmetic", "python arithmetic operators + - * / % ** // diagram table tutorial"),
    ("LO12_Precedence", "python operator precedence table order of operations diagram"),
    ("LO13_Comparison", "python comparison operators == != > < >= <= diagram table geeksforgeeks"),
    ("LO14_Logical", "python logical operators and or not boolean diagram geeksforgeeks"),
    ("LO15_If", "python if statement conditional execution flowchart diagram geeksforgeeks"),
    ("LO16_Elif", "python elif else if multiple conditions flowchart diagram tutorial"),
    ("LO17_Else", "python else clause default case flowchart diagram tutorial"),
    ("LO18_Nested_If", "python nested if else conditions inside flowchart diagram tutorial"),
    ("LO19_While", "python while loop flowchart diagram geeksforgeeks OR freecodecamp"),
    ("LO20_Break", "python break statement loop exit flowchart diagram geeksforgeeks"),
    ("LO21_Continue", "python continue statement skip iteration flowchart diagram geeksforgeeks"),
    ("LO22_For", "python for loop iterating sequence list flowchart diagram tutorial geeksforgeeks"),
    ("LO23_Range", "python range function start stop step number sequence diagram"),
    ("LO24_ForControl", "python break continue in for loop comparison diagram geeksforgeeks"),
    ("LO25_NestedLoops", "python nested loops inner outer iteration grid pattern diagram"),
    ("LO26_Functions", "python function def definition syntax structure diagram tutorial"),
    ("LO27_Parameters", "python function parameters arguments pass value diagram tutorial"),
    ("LO28_Return", "python return statement function output value diagram tutorial"),
    ("LO29_Default", "python default parameter argument function optional value diagram"),
]

import urllib.request

for label, query in queries:
    payload = json.dumps({
        "api_key": API_KEY,
        "query": query,
        "search_depth": "basic",
        "include_images": True,
        "max_results": 5
    }).encode()
    req = urllib.request.Request(
        "https://api.tavily.com/search",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            imgs = data.get("images", [])
            top = imgs[0] if imgs else "NOT_FOUND"
            print(f"{label}: {top}")
    except Exception as e:
        print(f"{label}: ERROR - {e}")

