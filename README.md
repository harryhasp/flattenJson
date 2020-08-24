# flattenJson

### General

Python script to flatten a JSON


### Setup

1. Having Python3
2. Clone repo
3. Run `chmod +x main.py` to make the main file executable

note: It's in included a file with the JSON given as an example to the problem description


### Execution

Code can be run either from stdin or by taking input from a file as an argument. In more details:

##### --> stdin

Example execution:  
`cd flattenJson/`  
`cat example.json | ./main.py`


##### --> input file as an argument

Example execution:  
`cd flattenJson/`  
`./main.py example.json`


### Output Example

The result is printed to stdout. Below there is the output where the example.json is given as input:

Original JSON:  
{ "w": 1, "b": true, "c": { "d": 3, "e": "test" } }  
\-------------------------  
Flattened JSON:  
{ "w": 1, "b": true, "c.d": 3, "c.e": "test" }
