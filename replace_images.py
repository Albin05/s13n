import os

base = '/Users/ranjan/masai/masai/s13n/09: Python for Programming/9.3: Applied Python'

# Define mappings: LO number -> (new_image_url, new_alt_text, new_caption)
mappings = {
    '9.3.1': (
        'https://upload.wikimedia.org/wikipedia/commons/c/c5/If-Then-Else-diagram.svg',
        'If-Then-Else flowchart diagram illustrating conditional branching in exception handling',
        'Try-except follows an if-then-else pattern: if an error occurs, branch to the except handler'
    ),
    '9.3.2': (
        'https://upload.wikimedia.org/wikipedia/commons/c/c5/If-Then-Else-diagram.svg',
        'If-Then-Else flowchart diagram showing the finally block as a guaranteed exit path',
        'The finally block guarantees cleanup runs regardless of which branch executes, like a guaranteed exit path in a flowchart'
    ),
    '9.3.3': (
        'https://upload.wikimedia.org/wikipedia/commons/c/c5/If-Then-Else-diagram.svg',
        'If-Then-Else flowchart diagram showing how raised exceptions alter program flow',
        'Raising exceptions redirects program flow to the error-handling branch, similar to an if-then-else decision'
    ),
    '9.3.4': (
        'https://upload.wikimedia.org/wikipedia/commons/c/c5/If-Then-Else-diagram.svg',
        'If-Then-Else flowchart diagram representing custom exception class branching',
        'Custom exception classes create specialized branches in your error-handling flowchart'
    ),
    '9.3.5': (
        'https://upload.wikimedia.org/wikipedia/commons/c/c5/If-Then-Else-diagram.svg',
        'If-Then-Else flowchart diagram showing multiple exception type handling paths',
        'Handling multiple exception types creates multiple conditional branches, each catching a specific error'
    ),
    '9.3.6': (
        'https://upload.wikimedia.org/wikipedia/commons/d/d7/Flowgorithm_Functions_Main.svg',
        'Flowgorithm functions diagram showing program flow through function calls for debugging',
        'Debugging traces program execution through function calls and control flow to identify errors'
    ),
    '9.3.7': (
        'https://upload.wikimedia.org/wikipedia/commons/6/67/Flowgorithm_Input_Process_Output.svg',
        'Flowgorithm Input-Process-Output diagram illustrating file reading operations',
        'Reading files follows the Input-Process-Output pattern: open the file, read the data, then process it'
    ),
    '9.3.8': (
        'https://upload.wikimedia.org/wikipedia/commons/6/67/Flowgorithm_Input_Process_Output.svg',
        'Flowgorithm Input-Process-Output diagram illustrating file writing operations',
        'Writing files follows the Input-Process-Output pattern: prepare data, then write it to a file'
    ),
    '9.3.9': (
        'https://upload.wikimedia.org/wikipedia/commons/6/67/Flowgorithm_Input_Process_Output.svg',
        'Flowgorithm Input-Process-Output diagram illustrating file append operations',
        'Appending to files follows the Input-Process-Output pattern: read existing content, then add new data'
    ),
    '9.3.10': (
        'https://upload.wikimedia.org/wikipedia/commons/5/5a/DOM-model.svg',
        'DOM tree model diagram representing hierarchical file path structure',
        'File paths form a tree hierarchy similar to the DOM model, navigating from root to nested directories'
    ),
    '9.3.11': (
        'https://upload.wikimedia.org/wikipedia/commons/d/df/Flowgorithm_Arrays_BuildF.svg',
        'Flowgorithm arrays diagram representing structured CSV data organization',
        'CSV files organize data in structured rows and columns, similar to arrays in a flowchart'
    ),
    '9.3.12': (
        'https://upload.wikimedia.org/wikipedia/commons/5/5a/DOM-model.svg',
        'DOM tree model diagram representing nested JSON data structure',
        'JSON data forms a nested tree structure similar to the DOM, with objects containing other objects'
    ),
    '9.3.13': (
        'https://upload.wikimedia.org/wikipedia/commons/5/5a/DOM-model.svg',
        'DOM tree model diagram representing hierarchical JSON output structure',
        'Writing JSON serializes a nested tree structure of data into a formatted text file'
    ),
    '9.3.14': (
        'https://upload.wikimedia.org/wikipedia/commons/d/d7/Flowgorithm_Functions_Main.svg',
        'Flowgorithm functions diagram showing modular program organization with built-in modules',
        'Built-in modules provide pre-written functions that you can import and call in your program flow'
    ),
    '9.3.15': (
        'https://upload.wikimedia.org/wikipedia/commons/d/d7/Flowgorithm_Functions_Main.svg',
        'Flowgorithm functions diagram showing external package integration via pip',
        'External packages installed via pip extend your program with additional functions and capabilities'
    ),
    '9.3.16': (
        'https://upload.wikimedia.org/wikipedia/commons/d/d7/Flowgorithm_Functions_Main.svg',
        'Flowgorithm functions diagram showing isolated virtual environment module organization',
        'Virtual environments isolate project dependencies, keeping each project\'s modules separate'
    ),
    '9.3.17': (
        'https://upload.wikimedia.org/wikipedia/commons/d/d7/Flowgorithm_Functions_Main.svg',
        'Flowgorithm functions diagram showing custom module imports in program flow',
        'Custom modules organize your own functions into reusable files that can be imported across projects'
    ),
    '9.3.18': (
        'https://upload.wikimedia.org/wikipedia/commons/6/67/Flowgorithm_Input_Process_Output.svg',
        'Flowgorithm Input-Process-Output diagram illustrating HTTP request and response cycle',
        'HTTP operations follow the Input-Process-Output pattern: send a request, server processes it, receive a response'
    ),
    '9.3.19': (
        'https://upload.wikimedia.org/wikipedia/commons/1/10/Python_3._The_standard_type_hierarchy.png',
        'Python standard type hierarchy diagram showing class and object relationships',
        'Classes serve as blueprints in Python\'s type hierarchy, defining the structure for creating objects'
    ),
    '9.3.20': (
        'https://upload.wikimedia.org/wikipedia/commons/2/21/Function_machine5.svg',
        'Function machine diagram showing how a class produces objects from input parameters',
        'Creating objects from classes works like a function machine: input parameters, output a new object'
    ),
    '9.3.21': (
        'https://upload.wikimedia.org/wikipedia/commons/2/21/Function_machine5.svg',
        'Function machine diagram showing the __init__ constructor transforming parameters into object state',
        'The __init__ constructor acts as a function machine, transforming input parameters into initialized object state'
    ),
    '9.3.22': (
        'https://upload.wikimedia.org/wikipedia/commons/1/10/Python_3._The_standard_type_hierarchy.png',
        'Python type hierarchy diagram showing how instance attributes store data within objects',
        'Instance attributes store unique data within each object, positioned within Python\'s type hierarchy'
    ),
    '9.3.23': (
        'https://upload.wikimedia.org/wikipedia/commons/2/21/Function_machine5.svg',
        'Function machine diagram showing instance methods as operations that transform object state',
        'Instance methods act as function machines that operate on and transform an object\'s internal state'
    ),
    '9.3.24': (
        'https://upload.wikimedia.org/wikipedia/commons/5/5a/DOM-model.svg',
        'DOM tree model diagram representing class inheritance hierarchy',
        'Inheritance creates a tree hierarchy of classes, where child classes extend parent class functionality'
    ),
    '9.3.25': (
        'https://upload.wikimedia.org/wikipedia/commons/5/5a/DOM-model.svg',
        'DOM tree model diagram showing method override relationships between parent and child classes',
        'Method overriding replaces parent behavior at specific nodes in the class hierarchy tree'
    ),
    '9.3.26': (
        'https://upload.wikimedia.org/wikipedia/commons/5/5a/DOM-model.svg',
        'DOM tree model diagram showing super() traversal up the class hierarchy',
        'super() navigates up the class hierarchy tree to call parent class methods from child classes'
    ),
    '9.3.27': (
        'https://upload.wikimedia.org/wikipedia/commons/5/5a/DOM-model.svg',
        'DOM tree model diagram representing object composition relationships',
        'Composition builds complex objects by combining simpler objects, forming a tree of contained parts'
    ),
    '9.3.28': (
        'https://upload.wikimedia.org/wikipedia/commons/1/10/Python_3._The_standard_type_hierarchy.png',
        'Python type hierarchy diagram illustrating encapsulation and data protection in classes',
        'Encapsulation protects internal data within Python\'s type system, controlling access through defined interfaces'
    ),
    '9.3.29': (
        'https://upload.wikimedia.org/wikipedia/commons/1/1c/Flowgorithm_For_Loop.svg',
        'Flowgorithm for loop diagram showing iterative list comprehension process',
        'List comprehensions condense a for-loop pattern into a single expression for concise list creation'
    ),
    '9.3.30': (
        'https://upload.wikimedia.org/wikipedia/commons/1/1c/Flowgorithm_For_Loop.svg',
        'Flowgorithm for loop diagram showing iterative dictionary comprehension process',
        'Dictionary comprehensions use a for-loop pattern to create key-value pairs in a single expression'
    ),
    '9.3.31': (
        'https://upload.wikimedia.org/wikipedia/commons/e/ea/Flowgorithm_While_Loop.svg',
        'Flowgorithm while loop diagram showing lazy evaluation in generator functions',
        'Generators use a while-loop pattern to yield values one at a time for memory-efficient iteration'
    ),
    '9.3.32': (
        'https://upload.wikimedia.org/wikipedia/commons/e/ea/Flowgorithm_While_Loop.svg',
        'Flowgorithm while loop diagram showing sequential iterator advancement',
        'Iterators advance through elements one at a time using a while-loop pattern until exhausted'
    ),
    '9.3.33': (
        'https://upload.wikimedia.org/wikipedia/commons/2/21/Function_machine5.svg',
        'Function machine diagram showing how decorators wrap and transform function behavior',
        'Decorators wrap functions like a machine that adds processing before and after the original function'
    ),
    '9.3.34': (
        'https://upload.wikimedia.org/wikipedia/commons/9/9d/Flowgorithm_Strings_Main.svg',
        'Flowgorithm strings diagram showing pattern matching operations on text',
        'Regular expressions process strings through pattern-matching operations to find and manipulate text'
    ),
    '9.3.35': (
        'https://upload.wikimedia.org/wikipedia/commons/c/c5/If-Then-Else-diagram.svg',
        'If-Then-Else flowchart diagram showing context manager enter and exit paths',
        'Context managers follow an enter-then-exit pattern, ensuring resources are properly acquired and released'
    ),
    '9.3.36': (
        'https://upload.wikimedia.org/wikipedia/commons/1/10/Python_3._The_standard_type_hierarchy.png',
        'Python standard type hierarchy diagram showing type annotations and classifications',
        'Type hints reference Python\'s type hierarchy to annotate expected types for code clarity'
    ),
    '9.3.37': (
        'https://upload.wikimedia.org/wikipedia/commons/c/c5/If-Then-Else-diagram.svg',
        'If-Then-Else flowchart diagram showing test pass and fail decision paths',
        'Unit tests follow an if-then-else pattern: if the assertion passes, the test succeeds; otherwise it fails'
    ),
    '9.3.38': (
        'https://upload.wikimedia.org/wikipedia/commons/4/45/Arithmetic_operations.svg',
        'Arithmetic operations diagram representing datetime calculations and time arithmetic',
        'Datetime operations use arithmetic to calculate durations, differences, and time-based computations'
    ),
}

# Find all LO directories
lo_dirs = []
for d in os.listdir(base):
    if d.startswith('LO-'):
        lo_dirs.append(d)

lo_dirs.sort()

updated = 0
errors = []

for lo_dir in lo_dirs:
    filepath = os.path.join(base, lo_dir, 'Lecture Notes.md')
    if not os.path.exists(filepath):
        continue

    # Extract LO number from directory name
    lo_num = lo_dir.split(':')[0].replace('LO-', '').strip()

    if lo_num not in mappings:
        errors.append(f'No mapping for {lo_num}')
        continue

    new_url, new_alt, new_caption = mappings[lo_num]

    with open(filepath, 'r') as f:
        content = f.read()

    if 'images.unsplash.com' not in content:
        errors.append(f'{lo_num}: No Unsplash URL found')
        continue

    lines = content.split('\n')
    new_lines = []
    i = 0
    replaced = False
    while i < len(lines):
        line = lines[i]
        if 'images.unsplash.com' in line and line.strip().startswith('!['):
            new_lines.append(f'![{new_alt}]({new_url})')
            replaced = True
            i += 1
            if i < len(lines) and lines[i].strip() == '':
                new_lines.append('')
                i += 1
                if i < len(lines) and lines[i].strip().startswith('*') and lines[i].strip().endswith('*'):
                    new_lines.append(f'*{new_caption}*')
                    i += 1
                    continue
            elif i < len(lines) and lines[i].strip().startswith('*') and lines[i].strip().endswith('*'):
                new_lines.append(f'*{new_caption}*')
                i += 1
                continue
        else:
            new_lines.append(line)
            i += 1

    if replaced:
        with open(filepath, 'w') as f:
            f.write('\n'.join(new_lines))
        updated += 1
        print(f'Updated {lo_num}: {lo_dir}')
    else:
        errors.append(f'{lo_num}: Could not find image line to replace')

print(f'\nTotal updated: {updated}')
if errors:
    print(f'Errors:')
    for e in errors:
        print(f'  - {e}')
