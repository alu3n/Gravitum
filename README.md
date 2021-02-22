# User manual
## Running Gravitum
U have to have:
- pygame 2.0.0 (necessarily)
- Python 3.9.0 (optimal)

To start gravitum run main.py

## Using gravitum
Gravitum has 3 main parts
You can use top menu to navigate between them
### Editor
There you can setup your simulation and edit export properties.

### Playback
There you can check the simulatiot (you have to simulate it first for it to be aviable there).

### Export
There you can move export camera to desired position and export the simulation in .jpg format.


### User controls
- Q - Zoom camera out
- E - Zoom camera in
- W - Move camera up
- A - Move camera left
- S - Move camera down
- D - Move camera right
- ARROW KEYS - Move solvers arround (editor only)

### How does it work?
Gravitum does not create real-time simulations, you have to create solvers, setup your simulation and after that you can hit simulate button. It will run simulation and save cache into your drive. Than you can playback the cache to see if you like it and you can export it eventually

### User interface
![Gravitum GUI EDITOR](https://i.ibb.co/sqsmX0S/gravitum-gui.jpg)

### Aviable solvers
Parameters:
- Framerate
- Frames
- Export resolution
- Background color

Source:
- Position - Center of the source (x,y)
- Frequency - How often should particle be spawned, how much particles should be spawned at once (how often, how much)
- Direction - Direction of source in degrees
- Spread - Spread of the source in degrees
- Range - Range of the source
- Color min start and color max start - particle will have color in this range at the start (it is randomized in that range)
- Color min end and color max end - particle will have color in this range in the end (it is randomized in that range)
- Velocity - minimal and maximal velocity (min, max)
- Lifespan - minimal and maximal lifespan (min, max)
- Size start - minimal and maximal size at the start (min, max)
- Size end - minimal and maximal size in the end (min, max)
- Active - range when is the solver active

Drag:
- Multiplier - amplify the force

Gravity:
- Force - force vector direction

Noise:
- Separation - spacing between 
- Multiplier - amplify noise vectors
- Range - how many noise vectors should be in the vector field (there will be that ammount ^2)

Vortex:
- Position - center of the vortex force
- Speed - vortex force amplifier
- Range - range of the vortex force

Attract:
- Position - center of the attract force
- Multiplier - attract force amplifier
- Range - range of the attract force

## Exporting simulation as jpg
Go to the export tab (you need to have simulation cached before you can go there)
In parameters you can specify export properties:
- Export resolution in pixels
- Export background color (R,G,B) 1-255
- Ammount of simulated frames

Export is sequence of jpg files

# Programmer manual
## How does the simulation work?
User specifies solvers and their properties those solvers each frame affects all of the particles separately. The simulation does not run real time, it is simulated and then saved to /cache/cache.json. When you want to play it back the software loads the file into memory and plays it frame by frame.

## Add new solver
### Create new solver in /simulation/forces/
You always have to include those:
- self.type = "name"
- self.attributes = {...}
-   In there you put attribute names as keys and Matrices from /utility/mathematics/matrix/ as parameters
- Method called apply which takes particles and framerate as input

Check some of the forces before creating one.

Next step is to add your solver into /simulation/editor_visualisation/visualise.py:
- Check how is it done with other solvers and do it like that
- In this file your force will be applied

Make the solver accesible from add menu:
- You have to add it there /utility/gui/editor/solver_menu_add_popup.py
- You have to add it there /utility/gui/editor/solver_menu.py

### Visualising solver
If you want to visualise solver you have to:
- Create file with visualisation in /simulation/editor_visualisation/
- Add support for it in /simulation/editor_visualisation/visualise.py

## Editing existing solvers
If you want to edit simulation behaviour of existing solver go to the method apply
If you want to edit its parameters add them to the self.attributes
If you want to edit its visualisation do it in its visualisation vile

## Edit global simulation parameters
There is solver called "Parameters"
- In there you can add or remove some of the global parameters
- You can use them when you're editing the software

## Edit gui
Each scene has its own gui, the have file called "composion.py" in common, they're its child it is used for the global navigation bar.
Most of the gui elements are located inside /utility/gui/
