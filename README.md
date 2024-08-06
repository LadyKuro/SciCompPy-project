# SciCompPy-project

## Cel projektu
Obliczanie konduktancji półprzewodnika ze wzbudzonym naprzewodnictwem w zewnętrznym polu magnetycznym. Zapis danych do pliku hdf5 oraz opcja samego odczytu i rysowania wykresów z pliku. 

<img src="https://github.com/user-attachments/assets/9385b1fd-b725-4230-a4d3-c59e726f4dbf" width="400">[^1]

[^1]: Ricco, L.S., Sanches, J.E., Marques, Y. et al. Topological isoconductance signatures in Majorana nanowires. Sci Rep 11, 17310 (2021). https://doi.org/10.1038/s41598-021-96415-3

Celem jest identyfikacja faz topologicznych na wykresie fazowym "phase_diagram.pdf". Faza topologicznie nietrywialna będzie posiadać niezerową konduktancję w zerowym punkcie różnicy potencjału.

<img src="https://github.com/user-attachments/assets/fda7bad9-653f-4369-b97d-5b7751b6641b" width="2700">[^2]

[^2]: M Wimmer et al 2011 New J. Phys. 13 053016

Przestrzeń parametrów w diagramie fazowym rozpinają energia Fermiego, $$E_F$$, oraz parametr porządku nadprzewodnictwa $$\Delta_0$$. Poniżej 
załączony jest przykładowy wynik działania programu `conductance.py`

<img src="https://github.com/user-attachments/assets/0805cf75-602d-4d5c-ba14-83ce5705741e" width="400">[^2]

## Lista plików i jak ich używać
> [!NOTE]
> Wymagane jest posiadanie zainstalowanych bilbiotek `kwant` oraz `h5py`. W tym projekcie znajduje się plik ze środowiskiem conda `topowire_env.yml` posiadającym wszystkie potrzebne pakiety.


`system_init.py` - ten plik tworzy system o zadanym Hamiltonianie do zmiennnej `syst` oraz słownik `default` z parametrami podawanymi do tego systemu 

`conductance.py` - 


