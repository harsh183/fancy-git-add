# Git Fancy Add

Fancy Command Line Interface with ASCII art and interactive menus for `git add` and `git commit`. 

This uses 

* `pyfiglet` to create ASCII art
* `questioner` to have interactive menus
* `plumbum` to wrap around the command line app
* `plumbum.cmd` to provide `ls` and `git` shell commands via a python interface

as well as `pytest` to test and `pylint` for style checking for the development process.

Made for the [workshop](https://125summer.tech/cli) in Summer 21 [125 Summer of Side Projects](https://125summer.tech/cli)

## Demo

Just adding 

```
$ python fgit.py
   _______ __     ______                                    __    __
  / ____(_) /_   / ____/___ _____  _______  __   ____ _____/ /___/ /
 / / __/ / __/  / /_  / __ `/ __ \/ ___/ / / /  / __ `/ __  / __  /
/ /_/ / / /_   / __/ / /_/ / / / / /__/ /_/ /  / /_/ / /_/ / /_/ /
\____/_/\__/  /_/    \__,_/_/ /_/\___/\__, /   \__,_/\__,_/\__,_/
                                     /____/

? What would you like to add? (Use arrow keys to move, <space> to select, <a> to toggle, <i> to invert)
   ○ __pycache__
   ● fgit.py
   ○ file3.txt
 » ● requirements.txt
   ○ test_folder
```

Add and commit as well using the flag `--commit`/`-c`

```
$ python fgit.py -c
   _______ __     ______                                    __    __
  / ____(_) /_   / ____/___ _____  _______  __   ____ _____/ /___/ /
 / / __/ / __/  / /_  / __ `/ __ \/ ___/ / / /  / __ `/ __  / __  /
/ /_/ / / /_   / __/ / /_/ / / / / /__/ /_/ /  / /_/ / /_/ / /_/ /
\____/_/\__/  /_/    \__,_/_/ /_/\___/\__, /   \__,_/\__,_/\__,_/
                                     /____/

? What would you like to add? [file3.txt]
```

Get help

```
$ fgit.py --help
fgit.py 1.3

Usage:
    fgit.py [SWITCHES]

Meta-switches:
    -h, --help         Prints this help message and quits
    --help-all         Prints help messages of all sub-commands and quits
    -v, --version      Prints the program's version and quits

Switches:
    -c, --commit       Commits the added files as well
```



