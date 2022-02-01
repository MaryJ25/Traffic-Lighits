# Testing Traffic Lights
This is a repo for a coding task I was given for an interview.

The purpose of the code here is to test a data set and determine if the Traffic Light is working correctly.
## Contents
 - _Main.py_ contains all the relevant code
 - _tests/test_main.py_ contains tests making sure that the main elements of code work the way they should.
 - _data.txt_ contains a sample data set
 - _requirements.txt_ list of all packages used. Majority are for formatting therefore it's more optional than required

## Task Guidelines
The task is to create a python script, that reads data from the file, and analyses it to check if the traffic light is
working correctly. 

#### There are following constraints:
- In the data each light is represented as a number:
  - 1,0,0,0 - Red
  - 0,1,0,0 - Yellow
  - 0,0,1,0 - Green
  - 0,0,0,1 - Left Green
  - 0,0,0,0 - Blink

- Colour change must follow a specific order eg:
  - Red -> Yellow -> Green -> Yellow -> Red (and repeat)
  - Red -> Yellow -> Left Green -> Green -> Yellow -> Red (and repeat)

#### Additional assumptions made on information provided:
- Green and Left Green always Blink before switching to a different colour.
- Other lights can't blink.
- A data set can contain any number of records, but can't be empty.
- If a light can't be read (unrecognised input) it will be treated as bad entry rather than Traffic Light malfunction.

## How to
To run te code it is enough to run the main.py file. If a data.txt file is not in the same repository as main.py an error will occur. 

## Alternative Solutions
A possible alternative solution would be to use bitwise operations -  this could be less resource intensive.
