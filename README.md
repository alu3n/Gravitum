Uzivatelska cast
#Spusteni programu
Program byl tvoren, pomoci:
- Python 3.9.0
- pygame 2.0.0
Mit nainstalovany pygame 2.0.0 je pro spusteni programu nutnost, python verze 3.9.0 je optimalni.

Program se spousti pres soubor main.py

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
