# Lazy Polygons

To make lazy evaluation work for this polygon, I introduced two trackers, one tracker `object.__flag` for tracking if the independent parameters have been modified using setter methods, and the other tracker `object.__repeats` for tracking if dependent parameters are called multiple times. Both the tracker parameters are defined as mutable list containers because we need to modify per requirements. However as they are defined using `__` so user cannot modify them accidentally or intentionally.

Note: Only independent parameters are defined with setter methods (These are num_edges and circum_radius). Hence these independent parameters are defined as a regular variable without any `_`. Rest of the parameters have no setters associated with them, and are defined using `_`.

Exception: I could have made all the dependent parameters with `__` to stop any accidental or intentional editing of parameters but I go with the python standard notation of single `_`. As a result, changes to dependent parameters is possible and could give 'incorrect' results with no warnings or error messages which is dangerous. One example is shown to illustrate this result in notebook.

Test cases for class Polygon is working.

Test cases for class PolygonIterator is to be resolved for issues related to `__getitem__` not getting the proper item pointing to the index specified due to advancing of item pointer to the next value in the generator i.e., need to include some resetting of generator to get the correct item of specified index value. First time, the index specified value is correct but if we operate the same index on the object, I am getting a different value (or the value corresponding to the next item in the generator).


