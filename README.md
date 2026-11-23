# BCDE321 Advanced Programming: Zombies In My Pocket

This repository contains the Zombie In My Pocket (ZIMP) game created by "Just a couple of cool guys" for Assessment 2.

## Requirements

- Python 3.12 or later
- Tkinter
- pytest & coverage

## Git Clone
```powershell
git clone https://github.com/Tyelk/Zombie_In_My_Pocket_Game_Refactor.git
cd Zombie_In_My_Pocket_Game_Refactor
```

## Setup

Create and activate a virtual environment, then install the project and pytest/coverage:

```powershell
python -m pip install -e .
python -m pip install pytest
python -m pip install pytest-cov
```

## Run Objective Smoke Checker

```powershell
python scripts/smoke_check.py
```

The smoke checker verifies required paths, non-GUI imports, pytest collection, and the baseline tests. It does not calculate marks.

## Run Tests

```powershell
python -m pytest
```

## Run Coverage

```powershell
pytest --cov=zimp
```

## Create Branch Coverage Report
### Full Report
```powershell
pytest --cov=src/zimp --cov-branch --cov-report=html
```
### Focused Refactor Report (only tests that focus on the implemented design pattern)
```powershell
pytest --cov=src/zimp tests/test_map/test_tile.py tests/test_map/test_tile_manager.py tests/test_map/test_inside_tile.py tests/test_map/test_inside_tile_factory.py tests/test_map/test_outside_tile.py tests/test_map/test_outside_tile_factory.py --cov-branch --cov-report=html
```
### Tile/Tile Manager Report (only tile/tile manager classes and tests)
```powershell
pytest --cov=zimp.domain.map.tile --cov=zimp.domain.map.tile_manager tests/test_map/test_tile.py tests/test_map/test_tile_manager.py --cov-branch --cov-report=html
```

## Run App

```powershell
python -m zimp.main
```

## How to Play

- The goal of the game is to disperse the corruption causing the zombies to appear
- To accomplish this the totem must be found in the house and buried in the garden
- The player must explore the house and fight zombies
- Use found items to help you survive encounters!

## Troubleshooting

- If `_tkinter` cannot be imported, use the supported campus Python installation and report the exact Python command and error.
- If tests cannot find `zimp`, run `python -m pip install -e .` from the repository root.
- Do not create Tk windows at module import time.
