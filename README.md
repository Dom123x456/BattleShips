# Battleship
Battleship is a single-player python version of the classic turn-based guess game.</br >
</br > 

![image]()</br >
</br >


### Deployed Website
A link to the deployed project via the Heroku app can be found [here]().


### Repository
The GitHub repository can be found [here](/).


____



## 1. Design

### 1.1 Structure

![image](https://user-images.githubusercontent.com/108178672/196038038-d90447d7-333e-4a14-b174-f1ccc24dd895.png)
2. The gameboard's grid, enemy ships and the number of attacks the user has left/turns
3. An enemy and user gameboards of grid generated.
4. The ships are generated and placed on the enemy gameboard.
5. When the user enters their row and column guess, the guess gameboard stores these coordinates - this is not visible to the user as it is placed within the hidden board.
6. If the coordinates on the user guess gameboard are the same as the one on the grid for the computer, the gameboard reprints showing an "X" showing a hit.
7. If the coordinates don't match, the gameboard reprints showing a "#" to denote a miss.
8. If the number of ships hit equals the number of ships generated and the number of of attempts has equalled 0 so the user wins.<br>
<br/>

### 1.2 Modules Used
* The __sleep__ function is imported from Python's module in order to stagger displayed text (see section 2.1) and create a delay before the running of selected loops.
* The __randint__ function is imported from Python's module in order to randomly generate the position of the enemy ships on the game board.
The __os__ function is imported which distiguishes the different operating sytem used</br >
</br >

## 2. Features
### 2.1 The Introduction Screen
Page loads an introduction screen explaining the backstory of the game which the leads to the controls on how to play the game.

### 2.4 The Game Board



## 3. Testing

### 3.1 General Testing


### 3.2 PEP8 Testing


### 3.3 Bugs
All identified bugs have been fixed including the example shown in section 3.1 above.</br >
</br >


## 4. Deployment

### 4.1 Deploying the repository via Heroku
* The app was created using Heroku via the following steps:
    * 


### 6. Acknowledgements and Credits
* Credits to Michael Carberry who helped me with getting my controls and introduction to work.
* [stackoverflow](https://stackoverflow.com/questions/60405812/can-you-put-a-operator-into-a-list-comprehension) was referenced for guidance on using operators within list comprehension.
* Finally Ajar Mahars youtube video to help me with the issues I had with indentation link here https://www.youtube.com/c/AjayMaharYT
----
