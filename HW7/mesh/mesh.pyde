# Sample code for starting the mesh processing project

class Mesh(object):
    def __init__(self, geometry, vertices):
        self.vertices = vertices
        self.geometry = geometry
        self.face_normals = self._getFaceNormals()
        self.vertex_normal_mapping = self._getVertexNormals()
        self.opposites = self._getOpposites()
        self.vertex_shading = False
        self.white = True
        
    def set_random_colors(self):
        self.colors = [(random(255), random(255), random(255)) for _ in range(len(self.vertices) / 3)]
                  
    def _getFaceNormals(self):
        output = []
        for i in range(len(self.vertices) / 3):
            v1 = self.geometry[self.vertices[i * 3]]
            v2 = self.geometry[self.vertices[i * 3 + 1]]
            v3 = self.geometry[self.vertices[i * 3 + 2]]
            
            u = PVector.sub(v2, v1)
            v = PVector.sub(v3, v1)
            n = u.cross(v).normalize()
            n.mult(-1)
            output.append(n)
        return output
    
    def _getOpposites(self):
        output = [-1 for _ in range(len(self.vertices))]
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if i != j:
                    nextI = self.geometry[self.vertices[self._next(i)]]
                    prevI = self.geometry[self.vertices[self._prev(i)]]
                    nextJ = self.geometry[self.vertices[self._next(j)]]
                    prevJ = self.geometry[self.vertices[self._prev(j)]]
                    if nextI == prevJ and prevI == nextJ:
                        output[i] = j
                        output[j] = i
        return output
    
    def _getVertexNormals(self):
        vertex_normal_mapping = {}
        for i in range(len(self.geometry)):
            curr_vertex = self.geometry[i]
            adj_face_normals = []
            for j in range(len(self.vertices)):
                if self.vertices[j] == i:
                    adj_face_normals.append(self.face_normals[j / 3])
            v = PVector(0,0,0)
            for norm in adj_face_normals:
                v.add(norm)
            v.normalize()
            vertex_normal_mapping[curr_vertex] = v
        print(vertex_normal_mapping)
        return vertex_normal_mapping
    
    def get_vertex_normal(self, v):
        return self.vertex_normal_mapping[v]
        for i in range(len(self.geometry)):
            if self.geometry[i] == v:
                return self.vertex_normals[i]
        raise Exception()
    
    def create_dual(self):
        dual_geometry = []
        dual_vertices = []
        for i in range(0, len(self.vertices), 3):
             v1 = self.geometry[self.vertices[i]]
             v2 = self.geometry[self.vertices[i+1]]
             v3 = self.geometry[self.vertices[i+2]]
             centroid = self._get_triangle_centroid(v1, v2, v3)
             dual_geometry.append(centroid)
        for i in range(len(self.geometry)):
            if i % 100 == 0:
                print("ITERATING {}/{}".format(i, len(self.geometry)))
            for j in range(len(self.vertices)):
                if self.vertices[j] == i:
                    # found a corner of the triangle @ index j
                    corners = [j]
                    next = self._swing(j)
                    while next != j:
                        corners.append(next)
                        next = self._swing(next)
                    cornerAverage = PVector(0,0,0)
                    for cornerIndex in range(len(corners)):
                        corner = corners[cornerIndex]
                        vCentroid = dual_geometry[corner / 3]
                        cornerAverage.add(vCentroid)
                    cornerAverage.mult(1 / float(len(corners)))
                    dual_geometry.append(cornerAverage)
                    for cornerIndex in range(len(corners)):
                        corner = corners[cornerIndex]
                        v1 = corner / 3
                        
                        corner2 = corners[(cornerIndex+1) % len(corners)]
                        v2 = corner2/3

                        v3 = len(dual_geometry) - 1
                        dual_vertices += [v1, v2, v3]
                    break
        self.geometry = dual_geometry
        self.vertices = dual_vertices
        print("CREATING NORMALS")
        self.face_normals = self._getFaceNormals()
        self.vertex_normal_mapping = self._getVertexNormals()
        print("CREATING OPPOSITES")
        self.opposites = self._getOpposites()
        self.set_random_colors()
        print("FINISHED")
    def _next(self, cornerId):
        return cornerId - (cornerId % 3) + ((cornerId+1) % 3)
    def _prev(self, cornerId):
        return self._next(self._next(cornerId))
    def _swing(self, cornerId):
        return self._next(self.opposites[self._next(cornerId)])
    def _get_triangle_centroid(self, v1, v2, v3):
        x = (v1.x + v2.x + v3.x)/float(3)
        y = (v1.y + v2.y + v3.y)/float(3)
        z = (v1.z + v2.z + v3.z)/float(3)
        return PVector(x,y,z)

rotate_flag = True    # automatic rotation of model?
time = 0   # keep track of passing time, for automatic rotation
current_mesh = None

# initalize stuff
def setup():
    size (600, 600, OPENGL)
    noStroke()

# draw the current mesh
def draw():
    global time
    
    background(0)    # clear screen to black

    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    scale (1, -1, 1)    # change to right-handed coordinate system
    
    # create an ambient light source
    ambientLight (102, 102, 102)
  
    # create two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();
    fill (50, 50, 200)            # set polygon color
    ambient (200, 200, 200)
    specular (0, 0, 0)            # no specular highlights
    shininess (1.0)
    rotate (time, 1.0, 0.0, 0.0)

    # THIS IS WHERE YOU SHOULD DRAW THE MESH
    if current_mesh == None:
        beginShape()
        normal (0.0, 0.0, 1.0)
        vertex (-1.0, -1.0, 0.0)
        vertex ( 1.0, -1.0, 0.0)
        vertex ( 1.0,  1.0, 0.0)
        vertex (-1.0,  1.0, 0.0)
        endShape(CLOSE)
    else:
        i = 0
        for face_id in range(len(current_mesh.vertices) / 3):
            i += 1
            if i % 100 == 0:
                print("RENDERING FACE {}/{}".format(i, len(current_mesh.vertices)))
            if current_mesh.white:
                fill(200,200,200)
            else:
                fill(*current_mesh.colors[face_id])
            v1 = current_mesh.geometry[current_mesh.vertices[face_id * 3]]
            v2 = current_mesh.geometry[current_mesh.vertices[face_id * 3 + 1]]
            v3 = current_mesh.geometry[current_mesh.vertices[face_id * 3 + 2]]
            
            if current_mesh.vertex_shading:
                n1 = current_mesh.get_vertex_normal(v1)
                n2 = current_mesh.get_vertex_normal(v2)
                n3 = current_mesh.get_vertex_normal(v3)
                beginShape()
                normal(n1.x, n1.y, n1.z)
                vertex(v1.x, v1.y, v1.z)
                normal(n2.x, n2.y, n2.z)
                vertex(v2.x, v2.y, v2.z)
                normal(n3.x, n3.y, n3.z)
                vertex(v3.x, v3.y, v3.z)
                endShape(CLOSE)
            else:
                n = current_mesh.face_normals[face_id]
                beginShape()
                normal(n.x, n.y, n.z)
                vertex(v1.x, v1.y, v1.z)
                vertex(v2.x, v2.y, v2.z)
                vertex(v3.x, v3.y, v3.z)
                endShape(CLOSE)
    popMatrix()
    
    # maybe step forward in time (for object rotation)
    if rotate_flag:
        time += 0.02

# process key presses
def keyPressed():
    global rotate_flag, current_mesh
    if key == ' ':
        rotate_flag = not rotate_flag
    elif key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
    elif key == '5':
        read_mesh ('torus.ply')
    elif key == 'n':
        if current_mesh != None:
            current_mesh.vertex_shading = not current_mesh.vertex_shading
        pass  # toggle per-vertex shading
    elif key == 'r':
        if current_mesh != None:
            current_mesh.white = False
            current_mesh.set_random_colors()
        pass  # randomly color faces
    elif key == 'w':
        if current_mesh != None:
            current_mesh.white = True
        pass  # color faces white
    elif key == 'd':
        if current_mesh != None:
            current_mesh.create_dual()
        pass  # calculate the dual mesh
    elif key == 'q':
        exit()

# read in a mesh file (THIS NEEDS TO BE MODIFIED !!!)
def read_mesh(filename):
    global current_mesh
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    geometry = []
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex = ", x, y, z
        geometry.append(PVector(x,y,z))
    # read in the faces
    vertices = []
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if nverts != 3:
            print "error: this face is not a triangle"
            exit()
        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        print "face =", index1, index2, index3
        vertices += [index1, index2, index3] # i * 3 + j
    current_mesh = Mesh(geometry, vertices)