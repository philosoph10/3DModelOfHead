from copy import deepcopy

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from model import Model
from effects.lighting import apply_lighting


def rotation_matrix(rx, ry, rz):
    """Generates a composite 3D rotation matrix."""
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(rx), -np.sin(rx)],
        [0, np.sin(rx), np.cos(rx)]
    ])
    Ry = np.array([
        [np.cos(ry), 0, np.sin(ry)],
        [0, 1, 0],
        [-np.sin(ry), 0, np.cos(ry)]
    ])
    Rz = np.array([
        [np.cos(rz), -np.sin(rz), 0],
        [np.sin(rz), np.cos(rz), 0],
        [0, 0, 1]
    ])
    return Rz @ Ry @ Rx  # Combine rotations


def update(frame, model, ax, speeds):
    """Updates the rotation and redraws the model."""
    ax.clear()
    
    # Compute rotated vertices
    rx, ry, rz = frame * speeds[0], frame * speeds[1], frame * speeds[2]
    R = rotation_matrix(rx, ry, rz)
    rotated_vertices = np.dot(model.get_vertices_array(), R.T)

    # Compute new face normals and lighting
    # new_model = Model("african_head.obj")  # Reload to keep face connectivity
    new_model = deepcopy(model)
    new_model.vertices = rotated_vertices.tolist()
    normals = new_model.compute_normals()
    intensities = apply_lighting(normals)

    # Collect face data
    shaded_faces = []
    face_colors = []
    for face, intensity in zip(model.faces, intensities):
        poly = [rotated_vertices[i] for i in face]
        shaded_faces.append(poly)
        face_colors.append((intensity, intensity, intensity))  # Grayscale shading

    # Draw new rotated model
    poly_collection = Poly3DCollection(shaded_faces, facecolors=face_colors, edgecolor="black", linewidth=0.2)
    ax.add_collection3d(poly_collection)

    # Hide axis
    plt.axis("off")

    # Auto-scaling
    ax.auto_scale_xyz(rotated_vertices[:, 0], rotated_vertices[:, 1], rotated_vertices[:, 2])
