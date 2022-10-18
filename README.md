# Battleship
Battleship is a single-player python version of the classic turn-based guess game.</br >
</br > 
The purpose of this game is to allow the user to chose cordinates on a board 1 to 8, A to H and try to hit all the battleship locations before they run out of turns.
![image](https://user-images.githubusercontent.com/108178672/196266802-5c07a0a3-639e-43b3-bcde-6fb71f9dd114.png)</br >
</br >


### Deployed Website
A link to the deployed project via the Heroku app can be found [here](https://battleshippython.herokuapp.com/).


### Repository
The GitHub repository can be found [here](https://github.com/Dom123x456/BattleShips).


____



## 1. Design

### 1.1 Structure

![image](https://user-images.githubusercontent.com/108178672/196038038-d90447d7-333e-4a14-b174-f1ccc24dd895.png)
1. The gameboard's grid, enemy ships and the number of attacks the user has left/turns
2. An enemy and user gameboards of grid generated.
3. The ships are generated and placed on the enemy gameboard.
4. When the user enters their row and column guess, the guess gameboard stores these coordinates - this is not visible to the user as it is placed within the hidden board.
5. If the coordinates on the user guess gameboard are the same as the one on the grid for the computer, the gameboard reprints showing an "X" showing a hit.
6. If the coordinates don't match, the gameboard reprints showing a "#" to denote a miss.
7. If the number of ships hit equals the number of ships generated and the number of of attempts has equalled 0 so the user wins.<br>
<br/>

### 1.2 Modules Used
* The __sleep__ function is imported from Python's module in order to stagger displayed text (see section 2.1) and create a delay before the running of selected loops.
* The __randint__ function is imported from Python's module in order to randomly generate the position of the enemy ships on the game board.
The __os__ function is imported which distiguishes the different operating sytem used</br >
</br >

## 2. Features
### 2.1 The Introduction Screen
Page loads an introduction screen explaining the backstory of the game which the leads to the controls on how to play the game.

### 2.2 The Game Board
My game board brings up a message of two types which is the introduction which contyains the title and the rundown of the games plot. Another message appears explaining the controls and the instructions on how to play.


![image](https://user-images.githubusercontent.com/108178672/196277387-f339ea42-17dd-4f3a-8eeb-1890de08f111.png)



After this the game will run giving you the option to select a row then a column in that order.


![image](https://user-images.githubusercontent.com/108178672/196291338-a288b8c1-0e8e-48b4-8adf-a8a72b0aaa2b.png)

Once the cordinates are correctly inputed they will respond with a MISS or a HIT. There are turns of 10 for the player and when those turns expire before the player hits the all ships, then the player will lose and recive a game over.


![image](https://user-images.githubusercontent.com/108178672/196416115-5b86dd9f-ac17-4072-a6c1-98e7221a89b7.png)


After this game restart and will run through the introduction and controls then loads up the game.


![image](https://user-images.githubusercontent.com/108178672/196416855-0911132d-7496-41d1-8ce0-fe9c8e8f55d2.png) 


## 3. Testing
During the development of the project,I used the "def main" to run my python through my gitpod terminal and to test for errors, like such the python programing not running the cod ein the write order as I intended which was due to the fact that they had been defined but not put into the section of code to be called foward when run.

![image](https://user-images.githubusercontent.com/108178672/196418028-da66f8f0-903a-4507-959f-29157a1cb100.png)

There was a case when the code was run for the first time that it was unable to bring up anything past the controls function. This wa sdue to the fact there was some redundant code that linked to a function that hhad been removed so when it was run the game couldnt find the function, I fixed this by removing the redundant code.

![image](https://user-images.githubusercontent.com/108178672/196273574-d73c485d-04b7-46b8-8f20-02c36f8649a5.png)

After this I put the code into a python syntax checker to check if any major issues were still present within the code and luckily there wrere none that hindered the code and non syntax errors were found.



### 3.1 Bugs
All identified bugs have been fixed including the example shown in section 3 above.</br >
</br >


## 4. Deployment

### 4.1 Deploying the repository via Heroku
* The app was created using Heroku via the following steps:
    * 


### 5. Acknowledgements and Credits
* Credits to Michael Carberry who helped me with getting my controls and introduction to work.
* [stackoverflow](https://stackoverflow.com/questions/60405812/can-you-put-a-operator-into-a-list-comprehension) was referenced for guidance on using operators within list comprehension.
* Finally Ajar Mahars youtube video to help me with the issues I had with indentation link here https://www.youtube.com/c/AjayMaharYT
* Harry Dhillon for helping me realise that I would need to add an introductury to my game and helping me with my indentation errors.
----
