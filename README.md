# Project Goal:
* Create a Character Generator that creates personality traits and values and process how they would interact and grow.
## Todo:
* Start creating a mecro_world class capable of creating mecro world simulation (mecro_world.py, L1)
* Start creating a micro_world class capable of creating micro world simulation (micro_world.py, L1)
* Need to allow fill_random_sub_values to accept age as a variable (lib.py, L93)
* Refactor TraitTreeModifier class, possibly move it. (lib.py, L6)
* Start creating a macro_world class capable of creating macro world simulation (macro_world.py, L1)
## Subgoals:
* Create a system that reads in user provided values (0-1) and randomly fills trait and value levels that aren't provided
* Create base core values list that are represented by a numerical percentage (0-1)
* Overall trait value should be a function of time, allowing 
* Input basic statistics for human birth and growth
* Create a system for characters to "work on" their unwanted personality traits if applicable from core values
* Create a processing engine to interprete life events and how they impact a characters development
# Setup:
```
virtualenv venv -p python3
```
```
. hook_scripts/setup.py
```
