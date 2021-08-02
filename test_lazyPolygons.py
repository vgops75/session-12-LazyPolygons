import math
import random
import pytest
import itertools

from lazyPolygons import Polygon
from lazyPolygons import PolygonIterator

# START OF Polygon class TEST CASES

def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(edges=3, rad=1)', f'actual: {str(p)}'
    assert p.vertices == n, (f'actual: {p.vertices},'
                                   f' expected: {n}')
    assert p.get_num_edges == n, f'actual: {p.get_num_edges}, expected: {n}'
    assert p.get_circum_rad == R, f'actual: {p.get_circum_rad}, expected: {R}'
    assert p.int_angle == 60, (f'actual: {p.int_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.int_angle == 90, (f'actual: {p.int_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.edge_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.apothem},'
                                          ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.int_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = Polygon(12, 3)
    assert math.isclose(p.edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.int_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

test_polygon()
####################################################################################################
########################### END OF Polygon class TEST CASES ########################################
####################################################################################################

# START OF PolygonIterator class TEST CASES

# Test cases for the PolygonIterator

def test_polygon_iterator():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = PolygonIterator(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = PolygonIterator(n, R)
    assert str(p) == 'PolygonIterator(iterable: edges=3, fixed: rad=1)', f'actual: {str(p)}'
    assert len(p) == n-3+1, f'actual: {len(p)}'
    try:
        print(p[1])
        assert False, ('Printing out of range item: '
                       'IndexError exception expected, not received')
    except AssertionError:
        pass
    
    # Now we are going to access individual Polygon using __getitem__() i.e., dictionary key-value of object
    # if p is the PolygonIterator instance, p[0] denotes Polygon(3,R), p[1] = Polygon(4,R), etc. for any R.
    
    n = 4
    R = 1
    p = PolygonIterator(n, R)
    # Below I used the index 1 (p[1]) as p will generate two polygons Polygon(3, 1) and Polygon(4, 1)
    assert p[1].int_angle == 90, (f'actual: {p[1].int_angle}, '
                                    ' expected: 90')
    assert math.isclose(p[1].area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p[1].area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p[1].edge_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p[1].edge_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p[1].perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p[1].perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p[1].apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p[1].apothem},'
                                          ' expected: 0.707')
    
    p = PolygonIterator(6, 2)
    # Here p[3] refers to Polygon(6, 2) as p will create a sequence of Polygons i.e., Polygon(3, 2), Polygon(4, 2), Polygon(5, 2) and Polygon(6, 2)
    assert math.isclose(p[3].edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p[3].apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p[3].area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p[3].perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p[3].int_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = PolygonIterator(12, 3)
    assert math.isclose(p[9].edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p[9].apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p[9].area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p[9].perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p[9].int_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = PolygonIterator(3, 10)
    p2 = PolygonIterator(10, 10)
    p3 = PolygonIterator(15, 10)
    p4 = PolygonIterator(15, 100)
    p5 = PolygonIterator(15, 100)
    
    assert all([p2[i] > p1[0] for i in range(1, 8)])
    assert all([p2[7] < p3[i] for i in range(8, 13)])
    assert all([p3[i] != p4[i] for i in range(13)])
    assert p1[0] != p4[0]
    assert all([p4[i] == p5[i] for i in range(13)])
    
test_polygon_iterator()

