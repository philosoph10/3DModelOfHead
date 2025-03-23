import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from model import Model
from effects.rotation import update


def animate_model(model):
    """Animates the model rotating around all three axes with different speeds."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Generate random speeds for rotation (small values for smooth motion)
    speeds = np.random.uniform(0.005, 0.02, size=3)

    _ = animation.FuncAnimation(fig, update, frames=200, fargs=(model, ax, speeds), interval=50)

    plt.show()


if __name__ == "__main__":
    model = Model("assets/african_head.obj")
    animate_model(model)
