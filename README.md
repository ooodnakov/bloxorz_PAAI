# Bloxorz game

https://user-images.githubusercontent.com/40039040/209445919-c5dafdf2-c48e-48f6-9128-ea8818c52eb9.mp4

## Requirements Lib

```
$ pip3 install -r requirement.txt
```

## Run

```
$ python3 run.py path_to_level options view
```

* `path_to_level`: dir path to json file, like `level/1.json`
* `options`: dfs, bfs, hill, astar, dijkstra or handle to play the game yourself
* `view`:
    + 1 for view Step By Step on Consoles and 3D View (All Step of Algorithm)
    + 2 for view only on Consoles (Result of Path)
    + 3 for view only on 3D View (Result of Path)
    + 4 for view with performance metrics printout

Example:
```
$ python3 run.py ./level/1.json astar 2
```
### Value learning

To run Value Learning you need to run another file:
```
$ python3 value_learning.py path_to_level
```
