# pythonEnglishDictionary
Simple console program for creating a interactive dictionary with JSON and remote SQL servers

The source file for List dictionary objects in JSON is data.json

Custom words can be appended in JSON using word as "key" and definition as "value". Note: we're storing the value using Tuples! 

For example if you want to add a new word to the list, maybe do something like this:

[{"example" : ("the definition of example-1")}]

or to add a multiple definition of the word:

[{"example" : ("the definition of example-1", "the definition of example-2)"]

