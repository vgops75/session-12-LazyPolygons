import math

# Regular Convex Polygon Object

class Polygon:
    '''
    This Polygon takes 2 parameters -- number of edges (N) and circum-radius (R), and the related parameters
    such as vertices, interior angle, edge length, apothem, area and perimeter are obtained using get methods.
    Access to modify by name operator is available only for num_edges and circum_rad, and any such 
    modifications will reflect accordingly in the dependent parameters accessed by get_{attribute} methods.
    '''
    
    def __init__(self, num_edges=3, circum_rad=6):
        if not isinstance(num_edges, int):
            raise TypeError(f'"num_edges" is an integer; TypeError')
        if num_edges < 3:
            raise ValueError(f'Polygon has a minimum of 3 edges; ValueError')
        self.num_edges = num_edges
        self.circum_rad = circum_rad
        self._vertices = None
        self._int_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
        self.__flag = [0, 0] # changes when setter for num_edges and/or circum_radius is called
        self.__repeats = [0, 0, 0, 0, 0, 0] # to track number of times methods get called for 

    @property
    def get_num_edges(self):
        return self.num_edges
    
    @property
    def get_circum_rad(self):
        return self.circum_rad
    
    # Allowing num_edges and circum_radius to be modified without checking if they have existing values...
    # Because num_edges and circum_radius are independent parameters on which rest of other parameters depend
    
    @get_num_edges.setter
    def set_num_edges(self, n):
        print('setter for num_edges called -- you are modifying the original num_edges:')
        self.num_edges = n
        if self.__flag[0] == 1:
            self.__flag[0] = 0
        self.__flag[0] = 1
        self.__repeats = [0, 0, 0, 0, 0, 0]

    @get_circum_rad.setter
    def set_circum_rad(self, r):
        print('setter for circum_radius called -- you are modifying original circum_radius:')
        self.circum_rad = r
        if self.__flag[1] == 1:
            self.__flag[1] = 0
        self.__flag[1] = 1
        self.__repeats = [0, 0, 0, 0, 0, 0]

    # Setters for dependent properties not allowed
    
    @property
    def vertices(self):
        print('getter for vertices')
        cnts = self.__repeats[0]
        if cnts == 0:
            if self._vertices is None or sum(self.__flag) >= 1:
                print(f'first time executing ...')
                # return self.get_num_edges
                self._vertices = self.get_num_edges
                self.__repeats[0] = 1
        return self._vertices
        
    @property
    def int_angle(self):
        print('getter for interior angle')
        cnts = self.__repeats[1]
        if cnts == 0:
            if self._int_angle is None or sum(self.__flag) >= 1:
                print(f'executing first time ...')
                self._int_angle = (self.get_num_edges - 2) * 180 / self.get_num_edges
                self.__repeats[1] = 1
        return self._int_angle

    @property
    def edge_length(self):
        print('getter for edge_length')
        cnts = self.__repeats[2]
        if cnts == 0:
            if self._edge_length is None or sum(self.__flag) >= 1:
                print(f'executing first time ...')
                self._edge_length = 2*self.get_circum_rad * math.sin(math.pi / self.get_num_edges)
                self.__repeats[2] = 1
        return self._edge_length

    @property
    def apothem(self):
        print('getter for apothem')
        cnts = self.__repeats[3]
        if cnts == 0:
            if self._apothem is None or sum(self.__flag) >= 1:
                print(f'executing first time ...')
                self._apothem = self.get_circum_rad * math.cos(math.pi / self.get_num_edges)
                self.__repeats[3] = 1
        return self._apothem

    @property
    def area(self):
        print('getter for area')
        cnts = self.__repeats[4]
        if cnts == 0:
            if self._area is None or sum(self.__flag) >= 1:
                print(f'executing first time ...')
                self._area = self.get_num_edges * self.edge_length * self.apothem / 2
                self.__repeats[4] = 1
        return self._area

    @property
    def perimeter(self):
        print('getter for perimeter')
        cnts = self.__repeats[5]
        if cnts == 0:
            if self._perimeter is None or sum(self.__flag) >= 1:
                print(f'executing first time ...')
                self._perimeter = self.get_num_edges * self.edge_length
                self.__repeats[5] = 1
        return self._perimeter

    def __repr__(self):
        return f'Polygon(edges={self.get_num_edges}, rad={self.get_circum_rad})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.vertices == other.vertices and self.get_circum_rad == other.get_circum_rad:
                return True
            else:
                return False
        else:
            return print(f'Compare instances of same class: Right-side instance not a Polygon')

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            if self.vertices > other.vertices:
                return True
            else:
                return False
        else:
            return print(f'Compare instances of same class: Right-side instance not a Polygon')

#####################################################################################################
            
class PolygonIterator:
    '''
    This class takes in number of vertices for the largest polygon in the sequence. Currently the sequence type is chosen as list,
    but it can be changed later, if required. The SequencePolygon class also takes in a circum_radius and it is assumed to be common
    for all of the polygons in the sequence.
    '''
    
    def __init__(self, num_vertices=3, circum_rad=6):
        if not isinstance(num_vertices, int):
            raise TypeError(f'"num_vertices" is an integer; TypeError')
        if num_vertices < 3:
            raise ValueError(f'Polygon has a minimum of 3 vertices; ValueError')
        
        self.num_vertices = num_vertices
        self.circum_rad = circum_rad
        self._pgon_pairs = ((Polygon, (edges, self.circum_rad)) for edges in range(3, self.num_vertices+1))
        self.__start = 0
        
    def __len__(self):
        return self.num_vertices - 2
    
    def __repr__(self):
        return f'PolygonIterator(iterable: edges={self.num_vertices}, fixed: rad={self.circum_rad})'
    
    def __iter__(self):
        return self._pgon_pairs
               
    def __next__(self):
        try:
            if self.__start < (self.num_vertices - 2):
                current = self.__start
                self.__start += 1
                res = next(self._pgon_pairs)
                return res[0](*res[1])
            else:
                raise StopIteration
        except StopIteration:
            print(f'StopIteration: Iterator reached max_value')
                
    def __getitem__(self, index):
        try:
            if index not in range(self.num_vertices - 2):
                raise IndexError
        except Exception:
            print(f'IndexError: Index out of range')     
        else:
            res = next(itertools.islice(self._pgon_pairs, index, index+1))
            return res[0](*res[1])
            

