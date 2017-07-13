Othello README

This was my first game I have written from scratch with a graphic user interface. This game is a two player game and requires two human players to play.

To start the program, run the game_setup module.

I separated my program into three parts:
Game Setup
- This module is where the game initializes the board. It starts off with a graphical interface that prompts the user to choose how they want to setup their board. 
Logic
- This module holds all the rules of the games. It determines when and where the player can place their piece and when the game is finished.
GUI
- All of the graphics needed for this game is setup here. It graphically sets up the board based on the properties from the game_setup module. It also interacts with the logic module to determine where to graphically place the piece and with the correct piece color.

