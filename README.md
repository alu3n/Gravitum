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
Q - Zoom camera out
E - Zoom camera in
W - Move camera up
A - Move camera left
S - Move camera down
D - Move camera right
ARROW KEYS - Move solvers arround (editor only)

### How does it work?
Gravitum does not create real-time simulations, you have to create solvers, setup your simulation and after that you can hit simulate button. It will run simulation and save cache into your drive. Than you can playback the cache to see if you like it and you can export it eventually

### User interface
...

### Aviable solvers
Parameters:
- Framerate
- Frames
- Export resolution
- Background color
Source:
- Position
- Frequency
- Direction
- Spread
- Range
- Color min start
- Color max start
- Color min end
- Color max end
- Velocity
- Lifespan
- Size start
- Size end
- Active
Drag:
- Multiplier
Gravity:
- Force
Noise:
- Separation
- Multiplier
- Range
Vortex:
- Position
- Speed
- Range
Attract:
- Position
- Multiplier
- Range


# Programmer manual


## Spusteni programu

Program je rozdeleny na 3 hlavni uzivatelske casti (editor, playback a export)

#Editor

#Playback

#Export




Programatorska cast

#Fungovani simulace
Simulace v programu neprobiha realtime, kazdy snimek simulace se pocita podle parametru u solveru a frameratu, podle toho probihaji zmeny (framerate=30 => 2x vetsi zmeny za frame nez u framerate=60) Hotova simulace se uklada do souboru "/export/cache.json".

#Pridani noveho solveru
Vsechny solvery se ukladaji do slozky "simulation/forces/"

Pro pridani noveho solveru je treba vytvorit tridu, ktera bude mit self.type = "Nazev_Solveru". Aby se spravne zobrazovaly parametry v uzivatelskem rozhrani, tak je treba vytvorit self.attributes, to musi byt slovnik, jehoz klice jsou nazvy parametru a jeho hodnoty jsou objekty typu matrix.

Trida solveru musi mit metodu apply, ta slouzi na aplikovani solveru, jako vstup dostane objekt particles, v jehoz hodnote particles jsou ulozene jednotlive particly. Metoda apply tedy muze delat neco s temito particly.

Pro vizualizaci solveru v editoru je treba vytvorit soubor ve slozce "simulation/editor_visualisation/". U vytvareni vizualizace nejsou zadne pozadavky na vstupni a vystupni promenne, funkce bude bezet v souboru "simulation/editor_visualisation/visualise.py", z tohoto souboru si muzete brat hodnoty.

Taky je treba pridat solver do souboru "simulation/simulation/run/sim_runner". Aplikuje se stejnym zpusobem jak vsechny ostatni solvery, ktere uz se tam nachazi.

Dale je treba pro korektni zobrazeni solveru v editoru pridani nazvu solveru do souboru "/utility/gui/editor/solver_menu_add_popup.py". Toto prida moznou return hodnotu do menu updatu, nyni je treba jeste pridat cely soubor do "utility/gui/editor/solver_menu.py". A pridat podminky "if self.adding:" append podle toho, jmena pridaneho solveru.

#Uprava solveru
Prubeh simulace solveru se upravuje primo v jeho hlavnim souboru v metode apply, jeho vizualizace se da upravit ve slozce "simulation/editor_visualisation/..."

Pokud chcete upravit globalni parametry, pro ktere neni treba vzdy pridat solver, a nejak budou ovlivnovat simulaci, tak takove parametry se ukladaji do slozku "simulation/forces/parameters"

#Uprava uzivatelskeho rozhrani
Kazda scena ma svoje vlastni gui, jedine co je spolecne je obsah cast sceny composition, pokud chcete neco pridat ke vsem scenam, tak to delejte pres tohle.
Jinak ke kazde scene jsou vlastni menu etc., pokud neco z toho chcete najit, tak je nejspise najdete ve slozce /utility/gui/...
