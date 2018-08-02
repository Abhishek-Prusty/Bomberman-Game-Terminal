# Bomberman-Terminal-Game

## Running the game

1. Make sure you are in the directory `Bomberman-Terminal-Game`

2. To run the game, enter the following command:

        sudo ./run.sh

*   If the above command results in an error saying `command not found`, enter the following command first:

    `chmod +x run.sh`

*   Sudo permissions are required for setting all the cpu governors to `performance` temporarily.
    After the game is over the original values will be reset.

*   If you don not wish to give sudo permission you may run this command:

    `python bomberman.py` or `python3 bomberman.py`

## Controls:

|    Moves   | Keyboard input |
|:----------:|:--------------:|
| Move left  |        a       |
| Move right |        d       |
| Move up    |        w       |
| Move down  |        s       |
| Drop bomb  |   x or b or o  |
| Quit       |        q       |
