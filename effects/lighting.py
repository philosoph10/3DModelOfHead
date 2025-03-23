import numpy as np


def apply_lighting(normals, light_dir=np.array([0, 0, 1])):
    """Computes shading intensity for each face based on light direction."""
    light_dir = light_dir / np.linalg.norm(light_dir)  # Normalize
    intensities = np.clip([np.dot(n, light_dir) for n in normals], 0, 1)
    return intensities