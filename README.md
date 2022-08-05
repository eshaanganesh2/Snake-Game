# Snake Game
A game developed in Python that can be played in 2 interactive modes:
* **Standard Mode** (Controlled via keyboard keys)
* **Gesture-Controlled Mode** (Controlled via finger count)

## Usage

**Step 1:**

Install Python from the following link: https://www.python.org/downloads/

**Step 2:**

Clone this repo by using the code below

```
git clone https://github.com/eshaanganesh2/Snake-Game.git
```

**Step 3:**

Execute the following command to install the required dependencies 

```
pip install -r requirements.txt
```

**Step 4:**

Run the python script `snake_game.py` by executing the command below

```
python snake_game.py
```

## Demo

<h3> <ins> Menu Page </ins> </h3>

<img src="https://github.com/eshaanganesh2/Snake-Game/blob/main/Demo/menu.PNG" width="512"/>

<h3> <ins> Normal Mode </ins> </h3>

In this mode, the player would use the **left**, **right**, **up** and **down** keyboard keys to move the snake in the corresponding direction. <br><br>
The game comes to an end in the following scenarios:
* The snake's head makes contact with any part of the body
* The snake's head makes contact with the edges of the game window

<img src="https://github.com/eshaanganesh2/Snake-Game/blob/main/Demo/normal_mode.gif" width="512"/>

<h3> <ins> Gesture-Controlled Mode </ins> </h3>

In this mode, the player's finger count would determine the snake's direction. 
* **1** finger to move **left**
* **2** fingers to move **right**
* **3** fingers to move **up**
* **4** fingers to move **down**<br>

The game comes to an end in the following scenarios:
* The snake's head makes contact with any part of the body
* The snake's head makes contact with the edges of the game window

<img src="https://github.com/eshaanganesh2/Snake-Game/blob/main/Demo/gesture_controlled_mode.gif" width="512"/>
