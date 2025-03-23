# 3D Head Model Renderer  

This project renders a **3D model of a head** from a Wavefront `.obj` file. The model is **rotated around all three axes at different speeds** and is **shaded using Lambertian lighting**, giving it a realistic light-dark effect based on surface orientation.

## Demo  
![Rotating Head Model](assets/demo.mp4)

## Features  
- **OBJ File Parsing**: Reads and processes the 3D head model.  
- **Rotation Animation**: Rotates the model **at different speeds** for each axis.  
- **Lambertian Shading**: Computes lighting based on the **dot product** between surface normals and a directional light source.  
- **Matplotlib Visualization**: Uses `matplotlib`'s 3D rendering capabilities to display the model.  

## Installation  
Ensure you have **Python 3.11** installed, then install the dependencies:  
```sh
pip install -r requirements.txt
```

## Running the Project

To run the renderer, use:
```sh
python render.py
```

## Dependencies
This project requires the following libraries:

```
numpy==2.2.x
matplotlib==3.10.x
```

## Tested Environment  
- **Python 3.11**  
- **Matplotlib 3.10.x**  
- **NumPy 2.2.x**  

## How It Works  
1. **Load the Model**: Reads vertex (`v`) and face (`f`) data from an `.obj` file.  
2. **Apply Rotation**: Uses **rotation matrices** to animate the model.  
3. **Compute Lighting**: Implements **Lambertian shading** using face normals.  
4. **Render the Model**: Displays the wireframe and shaded faces using `matplotlib`.  

## Example  
After running `python render.py`, a 3D rotating and shaded head model will be displayed.

---

### Author  
This project was created for a **university graphics assignment** by Yur-Liubomysl Dekhtiar.