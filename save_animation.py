import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from model import Model
from effects.rotation import update


def save_animation(model, filename="demo.gif", fps=20, duration=10):
    """Saves the rotating model animation as a GIF."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    speeds = np.random.uniform(0.005, 0.02, size=3)  # Random rotation speeds
    ani = animation.FuncAnimation(fig, update, frames=fps * duration, fargs=(model, ax, speeds), interval=1000 / fps)

    ani.save(filename, fps=fps, dpi=100, writer="pillow")  # Save as GIF
    print(f"Animation saved as {filename}")

# Run and save animation
model = Model("assets/african_head.obj")
save_animation(model, filename="assets/demo.gif")