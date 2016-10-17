import numpy as np

"""
In this module I have defined the necessary classes with the purpose to make 
the program as clean and comprehensible as possible

"""
class Node:
    def __init__(self, x, y, pins = (False, False,), load = (None, None,) , *, abs_pos):
        self.x = x
        self.y = y
        self.pins = pins
        self.abs_pos = abs_pos
        self.deforms = [0, 0]
        self.load = load # forces are given as a tuple of Fx, Fy

    def __repr__(self):
        return "x = {}, y = {}\nload = {}\ndeforms = {} mm\n".format(self.x, self.y,
                self.load,
                self.deforms)

class Elem:
    def __init__(self, node1, node2, **properties):
        self.node1 = node1
        self.node2 = node2
        self.properties = properties # properties shall be: A, E

        # Only 2 properties should be inputted
        if len(self.properties) != 2:
            raise Exception('You should input E, A as the keyword arguements')

        # length of element
        self.properties['L'] = np.sqrt( (self.node1.x - self.node2.x) ** 2 \
                + (self.node1.y - self.node2.y) ** 2)
        # k - element stiffness
        self.properties['k'] = self.properties['E'] * self.properties['A'] / \
                self.properties['L']
        # Theta
        if self.node1.x == self.node2.x:
            if self.node2.y > self.node1.y:
                self.properties['theta'] = np.pi/2.
            else:
                self.properties['theta'] = -np.pi/2.
        else:
            self.properties['theta'] = np.arctan((self.node2.y - self.node1.y)/
                    (self.node2.x - self.node1.x))
        self._arrays = {'C': np.array([]), 'kloc': np.array([]), 'kglob': np.array([])}

    @property
    def length(self):
        return self.properties['L']

    @property
    def C(self):
        """Return the C transformation matirx of the element."""
        if self._arrays['C'].any():
            return self._arrays['C']
        else:
            self._setC()
            return self.C
    def _setC(self):
        """Compute the transformation (loc -> glob) matrix.
        Store it in the _arrays dictionary"""
        th = self.properties['theta']
        s = np.sin(th)
        c = np.cos(th)

        C = np.array([[c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, c, -s],
            [0, 0, s, c]])
        self._arrays['C'] = C

    @property
    def kloc(self):
        """Return the local stiffness matrix of the element."""
        if self._arrays['kloc'].any():
            return self._arrays['kloc']
        else:
            self._setkloc()
            return self.kloc
    def _setkloc(self):
        """Compute the (local) stiffness matrix of the element."""
        k = self.properties['k']

        kloc = np.array([[k, 0, -k, 0],
            [0, 0, 0, 0],
            [-k, 0, k, 0],
            [0, 0, 0, 0]])
        self._arrays['kloc'] = kloc

    @property
    def kglob(self):
        """Return the global stiffness matrix of the element."""
        if self._arrays['kglob'].any():
            return self._arrays['kglob']
        else:
            self._setkglob()
            return self.kglob
    def _setkglob(self):
        self._arrays['kglob'] = np.dot(np.dot(self.C, self.kloc), np.transpose(self.C))


    # Printing the properties
    def __str__(self):
        return "*STR*\n***Node Coordinates***\n" + str(self.node1) + '\n' + str(self.node2)
    def __repr__(self):
        string1 = ("***Node Coordinates***\n" + 
                str(self.node1) + '\n' + 
                str(self.node2) + '\n\n' +
                "*** Element Properties ***\n" +
                "E = {} MPa\nA = {} mm^2\n".format(self.properties['E'], self.properties['A']))
        return string1
