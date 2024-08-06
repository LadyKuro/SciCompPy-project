# SciCompPy-project

## Cel projektu
Obliczanie konduktancji półprzewodnika ze wzbudzonym naprzewodnictwem w zewnętrznym polu magnetycznym. Zapis danych do pliku hdf5 oraz opcja samego odczytu i rysowania wykresów z pliku. 

<img src="https://github.com/user-attachments/assets/9385b1fd-b725-4230-a4d3-c59e726f4dbf" width="400">[^1]

[^1]: Ricco, L.S., Sanches, J.E., Marques, Y. et al. Topological isoconductance signatures in Majorana nanowires. Sci Rep 11, 17310 (2021). https://doi.org/10.1038/s41598-021-96415-3

Celem jest identyfikacja faz topologicznych na wykresie fazowym "phase_diagram.pdf". Faza topologicznie nietrywialna będzie posiadać niezerową konduktancję w zerowym punkcie różnicy potencjału.

<img src="https://github.com/user-attachments/assets/fda7bad9-653f-4369-b97d-5b7751b6641b" width="270">[^2]

[^2]: M Wimmer et al 2011 New J. Phys. 13 053016

Przestrzeń parametrów w diagramie fazowym rozpinają energia Fermiego, $$E_F$$, oraz parametr porządku nadprzewodnictwa $$\Delta_0$$. Poniżej 
załączony jest przykładowy wynik działania programu `conductance.py` (wykres po lewej).

<img src="https://github.com/user-attachments/assets/7c605683-eb35-4d0c-9689-c5c99cc84d2e" width="500">

## Lista plików i jak ich używać
> [!NOTE]
> Wymagane jest posiadanie zainstalowanych bilbiotek `kwant` oraz `h5py`. W tym projekcie znajduje się plik ze środowiskiem conda `topowire_env.yml` posiadającym wszystkie potrzebne pakiety.


`system_init.py` - ten plik tworzy system o zadanym Hamiltonianie do zmiennnej `syst` oraz słownik `default` z parametrami podawanymi do tego systemu 

`conductance.py` - 

usage: conductance.py [-h] [-p PLOT] [-f FILE]

Calculate conductance and save to hdf5 or just plot from files.

options:
  -h, --help            show this help message and exit
  -p PLOT, --plot PLOT  Just plot the result from hdf5 files. (default: False)
  -f FILE, --file FILE  HDF5 file to read. (default: conductance.h5)

