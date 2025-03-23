import numpy as np


class Model:
    """Class for loading and handling an .obj 3D model with shading and rotation."""
    
    def __init__(self, filename):
        self.vertices = []  # List of (x, y, z) tuples
        self.faces = []     # List of faces (each face is a list of vertex indices)
        self.load(filename)

    def load(self, filename):
        """Loads the .obj file and extracts vertices and faces."""
        with open(filename, "r") as file:
            for line in file:
                parts = line.split()
                if not parts:
                    continue
                if parts[0] == "v":  # Vertex
                    x, y, z = map(float, parts[1:4])
                    self.vertices.append((x, y, z))
                elif parts[0] == "f":  # Face
                    face = [int(part.split('/')[0]) - 1 for part in parts[1:]]
                    self.faces.append(face)

    def compute_normals(self):
        """Computes face normals for shading."""
        normals = []
        for face in self.faces:
            v0, v1, v2 = [np.array(self.vertices[i]) for i in face[:3]]
            normal = np.cross(v1 - v0, v2 - v0)
            normal = normal / np.linalg.norm(normal)  # Normalize
            normals.append(normal)
        return normals

    def get_vertices_array(self):
        """Returns vertices as a NumPy array."""
        return np.array(self.vertices)
