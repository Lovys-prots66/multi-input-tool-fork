# multi-input-tool
Simple python module that contains a few functions to run multiple numeric inputs through simple functions and format them in a list[dict] structure.
This is a very tiny module and I will update it, if I find more interesting functions of a similar kind.

## Available functions:
### @add_to_list(list) (wrapper)
The `@add_to_list()` wrapper function can be used on simple functions that take a single numeric input with a single numeric output to allow for multiple values to be passed in and for a target list to be populated effectively.
<br>
The beauty of `@add_to_list()` is that you can run multiple decorated functions on the same list and add different outputs with different keys.
<br>
Decorated functions also return the list that was supplied through the `@add_to_list()`.
<br>
**Warning:** Using the same key multiple times will destroy the previous values associated with the same key and replace them with new ones. It's best to use the same key with the same range of inputs to avoid bad data.
#### Input:
```py
from multi_input import add_to_list

results = []

@add_to_list(results)
def linear_function(x):
  return x * 2

@add_to_list(results)
def quadratic_function(x):
  return x ** 2

linear_function(0, 4, ["x", "y"])
quadratic_function(0, 4, ["x", "z"])

print(results)
```
#### Output:
```py
[{'x': 0, 'y': 0, 'z': 0}, {'x': 1, 'y': 2, 'z': 1}, {'x': 2, 'y': 4, 'z': 4}, {'x': 3, 'y': 6, 'z': 9}]
```
### **json_form(list)**
The lists modified by functions decorated with **add_to_list** can be formatted as strings with JSON-format. Give json_form the modified list and it will give you the JSON-formatted string.
#### Input:
```py
from multi_input import json_form

print(json_form(results))
```
<sub>results is the same list as in previous output</sub>
#### Output:
```json
[
  {
    "x": 0,
    "y": 0,
    "z": 0
  },
  {
    "x": 1,
    "y": 2,
    "z": 1
  },
  {
    "x": 2,
    "y": 4,
    "z": 4
  },
  {
    "x": 3,
    "y": 6,
    "z": 9
  }
]
```
<br>

### **float_range(start, stop, step)**
This generator-function behaves like the built in python `range()` function, except for having support for fractions. This function is also being used inside functions decorated by `@add_to_list()` so you can modify what steps the loop is supposed to take.
### Input:
```py
from multi_input import float_range

print(list(float_range(-2, 2, 0.2)))
```
### Output:
```py
[-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
```
<br>

Using the `step` parameter on a function decorated by `@add_to_list()`:

### Input:
```py
print(linear_function(0, 4, ["x", "y"], 0.5))
```
### Output:
```py
[{'x': 0.0, 'y': 0.0}, {'x': 0.5, 'y': 1.0}, {'x': 1.0, 'y': 2.0}, {'x': 1.5, 'y': 3.0}, {'x': 2.0, 'y': 4.0}, {'x': 2.5, 'y': 5.0}, {'x': 3.0, 'y': 6.0}, {'x': 3.5, 'y': 7.0}]
```
<br>
So far this is it. I might add more functions in the future!
