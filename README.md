Beginner Projects
=================
Project list copied from [here](https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/edit?usp=sharing)

## Table of Contents 
- [99 Bottles](https://github.com/alfredmuffin/Beginner-Projects#99-bottles)
- [Magic 8 Ball](https://github.com/alfredmuffin/Beginner-Projects#magic-8-ball)
- [Pythagorean Triples Checker](https://github.com/alfredmuffin/Beginner-Projects#pythagorean-triples-checker)
- [Coin Estimator By Weight](https://github.com/alfredmuffin/Beginner-Projects#coin-estimator-by-weight)
- [Mad Libs Story Makes](https://github.com/alfredmuffin/Beginner-Projects#mad-libs-story-maker)
- [Change Calculator](https://github.com/alfredmuffin/Beginner-Projects#change-calculator)
- [Mean, Median, and Mode](https://github.com/alfredmuffin/Beginner-Projects#mean-median-and-mode)
- [Higher Lower Guessing Game](https://github.com/alfredmuffin/Beginner-Projects#higher-lower-guessing-game)
- [Multiplication Table](https://github.com/alfredmuffin/Beginner-Projects#multiplication-table)
- [Fibonacci Sequence](https://github.com/alfredmuffin/Beginner-Projects#fibonacci-sequence)
- [Hangman Game](https://github.com/alfredmuffin/Beginner-Projects#hangman-game)
- [Menu Calculator](https://github.com/alfredmuffin/Beginner-Projects#menu-calculator)
- [Dice Rolling Simulator](https://github.com/alfredmuffin/Beginner-Projects#dice-rolling-simulator)
- [Creating a Dice Simulator](https://github.com/alfredmuffin/Beginner-Projects#creating-a-dice-simulator)
- [Count and Fix Green Eggs and Ham](https://github.com/alfredmuffin/Beginner-Projects#count-and-fix-green-eggs-and-ham)
- [What's My Number?](https://github.com/alfredmuffin/Beginner-Projects#whats-my-number)
- [Factors of a Number](https://github.com/alfredmuffin/Beginner-Projects#mfactors-of-a-number)
- [Countdown Clock](https://github.com/alfredmuffin/Beginner-Projects#countdown-clock)
- [Turn Based Pokemon Style Game](https://github.com/alfredmuffin/Beginner-Projects#turn-based-pokemon-style-game)
- [A Variation of 21](https://github.com/alfredmuffin/Beginner-Projects#magic-8-ball)
- [Compare Recent reddit Karma](https://github.com/alfredmuffin/Beginner-Projects#compare-recent-reddit-karma)
- [Watch for New /r/TIL Facts](https://github.com/alfredmuffin/Beginner-Projects#watch-for-new-/r/til-facts)
- [Random Wikipedia Article](https://github.com/alfredmuffin/Beginner-Projects#random-wikipedia-article)
- [What's the Weather?](https://github.com/alfredmuffin/Beginner-Projects#whats-the-weather)


Beginner Projects
-----------------
(projects are ordered from easiest to hardest)

##### 99 Bottles
- Create a program that prints out every line to the song "99 bottles of beer on the wall."
- Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
- Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
- Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
- Put a blank line between each verse of the song.

##### Magic 8 Ball
- Simulate a magic 8-ball.
- Allow the user to enter their question.
- Display an in progress message(i.e. "thinking").
- Create 20 responses, and show a random response.
- Allow the user to ask another question or quit.
- Bonus:
  - Add a gui.
  - It must have box for users to enter the question.
  - It must have at least 4 buttons: 
    - ask
    - clear (the text box)
    - play again
    - quit (this must close the window)

##### Pythagorean Triples Checker
- If you do not know how basic right triangles work, read this article on wikipedia[1] .
- Allows the user to input the sides of any triangle in any order.
- Return whether the triangle is a Pythagorean Triple or not.
- Loop the program so the user can use it more than once without having to restart the program.

##### Coin Estimator By Weight
- Allows the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
- Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all of their money.
- Weight of each coin[2] and how many fit inside each type of wrapper[3].
- Subgoals:
  - Round all numbers printed out to the nearest whole number.
  - Allow the user to select whether they want to submit the weight in either grams or pounds.

##### Mad Libs Story Maker
- Create a Mad Libs style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user inputted. 
- The story doesn't have to be too long, but it should have some sort of story line.
- Tip: it's easiest to write out a quick story on a piece of paper or a word document, and then go back through and see which words the user should be able to change.
- Subgoals:
  - If the user has to put in a name, change the first letter to a capital letter.
  - Change the word "a" to "an" when the next word in the sentence begins with a vowel.

##### Change Calculator
- Imagine that your friend is a cashier, but has a hard time counting back change to customers. 
- Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.
Example: if he inputs 1.47, the program will say that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.
- Subgoals:
- So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him and the price of the item. The program should then tell him the amount of each coin he needs like usual.
- To make the program even easier to use, loop the program back to the top so your friend can continue to use the program without having to close and open it every time he needs to count change.

##### Mean, Median, and Mode
Background
In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all the numbers numerically, the median is the number in the middle.
Goal
Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions that already complete these tasks, do not use them.
Subgoals
In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
If there is an even number of numbers in the list, return both numbers that could be considered the median.
If there are multiple modes, return all of them.

##### Higher Lower Guessing Game
BASIC GOAL Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is. After every guess, the computer should tell the user if the guess is higher or lower than the answer. When the user guesses the correct number, print out a congratulatory message.
SUB GOALS
Add an introduction message that explains to the user how to play your game.
In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.
At the end of the game, allow the user to decide if they want to play again (without having to restart the program).

##### Multiplication Table
Goal
Create a program that prints out a multiplication table for the numbers 1 through 9. It should include the numbers 1 through 9 on the top and left axises, and it should be relatively easy to find the product of two numbers. Do not simply write out every line manually (ie print('7 14 21 28 35 49 56 63') ).
Subgoals
As your products get larger, your columns will start to get crooked from the number of characters on each line. Clean up your table by evenly spacing columns so it is very easy to find the product of two numbers.
Allow the user to choose a number to change the size of the table (so if they type in 12, the table printed out should be a 12x12 multiplication table).

##### Fibonacci Sequence
BACKGROUND INFORMATION If you do not know about the Fibonacci Sequence, read the information on MathIsFun.com[1] .
GOAL
Define a function that allows the user to find the value of the nth term in the sequence. To make sure you've written your function correctly, test the first 10 numbers of the sequence. Remember, the 0th term is 0 and the first and second term are both 1.

##### Hangman Game
Goal
Create a program that selects a random word and then allows the user to guess it in a game of hangman. Like the real game, there should be blank spots for each letter in the word, and a part of the body should be added each time the user guesses a letter than is not in the answer (you may choose how many wrong turns the user can make until the game ends).
Subgoals
If the user loses, print out the word at the end of the game.
Create a "give up" option.

##### Menu Calculator
GOAL
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items, you assign each one to a number, as shown below.
Chicken Strips - $3.50
French Fries - $2.50
Hamburger - $4.00
Hotdog - $3.50
Large Drink - $1.75
Medium Drink - $1.50
Milk Shake - $2.25
Salad - $3.75
Small Drink - $1.25
To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.
SUBGOALS
If you decide to, print out the items and prices every time before the user types in an order.
Once the user has entered an order, print out how many of each item have been ordered, as well as the total price. If an item was not ordered at all, then it should not show up.

##### Dice Rolling Simulator
Goal
By using the random module, python can do things like pseudo-random number generation. So in this program, allow the user to input the amount of sides on a dice and how many times it should be rolled. From there, your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed). After that, print out how many times each number came up.
Subgoal
Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in a real number until they do so.
Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can, round the percentage to 4 digits total OR two decimal places.

##### Creating a Dice Simulator
Goals You are about to play a board game, but you realize you don't have any dice. Fortunately you have this program. 1. Create a program that opens a new window and draws 2 six-sided dice 2. Allow the user to quit, or roll again
Bonus 1. Allow the user to select the number of dice to be drawn on screen(1-4) 2. Add up the total of the dice and display it

##### Count and Fix Green Eggs and Ham
Some of you may remember the Dr. Sues story "Green Eggs and Ham". For those of you that don't remember it or have never heard of it, here is the story[1] . However, there is a problem with the story I gave you - every time the word I is used, it is lowercase.
Because of this problem, your job is to do the following...
Copy the story I gave you into a regular text file.
Create a program that reads through the story and makes the letter i uppercase any time it should be. (Make sure to change it when it's used in sam-I-am's name too.)
Have your program make a new file, and have it write out the story correctly.
Print out how many errors were corrected.
When you're finished, you should have corrected 70 errors [2] .

##### What’s My Number?
Between 1 and 1000, there is only 1 number that meets the following criteria. While it could be manually figured out with pen and paper, it would be much more efficient to write a program that would do this for you. With that being said, your goal is to find out which number meets these criteria. To find out if you have the correct number, click the link at the bottom of this main post.
The number has two or more digits.
The number is prime.
The number does NOT contain a 1 or 7 in it.
The sum of all of the digits is less than or equal to 10.
The first two digits add up to be odd.
The second to last digit is even.
The last digit is equal to how many digits are in the number.

##### Factors of a Number
Define a function that creates a list of all the numbers that are factors of the user's number. For example, if the function is called factor, factor(36) should return [1,2,3,4,6,9,12,18,36]. The numbers in your list should be from least to greatest, and 1 and the original number should be included.

##### Countdown Clock
GOAL
Create a program that allows the user to choose a time and date, and then prints out a message at given intervals (such as every second) that tells the user how much longer there is until the selected time.
SUBGOALS
If the selected time has already passed, have the program tell the user to start over.
If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the month name or its number.
TIP: Making use of built in modules such as time and datetime can change this project from a nightmare into a much simpler task.

##### Turn Based Pokemon Style Game
GOAL
Write a simple game that allows the user and the computer to take turns selecting moves to use against each other. Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves:
The first move should do moderate damage and has a small range (such as 18-25).
The second move should have a large range of damage and can deal high or low damage (such as 10-35).
The third move should heal whoever casts it a moderate amount, similar to the first move.
After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.
SUBGOALS
When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
Give each move a name.

##### A Variation of 21
BACKGROUND INFORMATION
If you do not know how 21 (AKA Blackjack) is played, reading the first couple of paragraphs of this wikipedia article[1] may be beneficial.
MAIN GOAL
In this project, you will make a game similar to 21/blackjack. Since this is not an actual game (as far as I'm aware of), here the the instructions for how to play.
In this version, there is only one player, and there are two types of scores - the round score and the game score. The game score will begin at 100, and the game will last for five rounds.
At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score. From here, the player has two options - draw another card to try to get their round score closer to 21, or they can end the round. The player can draw as many cards as they want until they end the round or their round score exceeds 21.
At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins. After the five rounds, the player is given their total score and the game is over.
---Other Information About The Game---
Aces are only worth 1.
If a player busts, 21 is subtracted from their total score.
All face cards are worth 10.
So the point of your program is to allow the user to play the game described above. Many of the subgoals listed below can be added to shine up the game.
SUBGOALS
At the beginning of each round, print the round number (1 to 5).
Since this is a text base game, tell the user what is happening. For example, tell him/her when he/she draws a card, the name of the card, when they bust, etc.
Create a ranking system at the end of the game and tell the user their rank. For example, if the player finishes with 50-59 points they get an F, 60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
At the end of each round, print out the user's total score.
This may be the hardest part of the project, depending on how you wrote it. Make sure the deck has 4 of each type of card, and then remove cards as they are drawn. At the end of each round, make the deck have all of the cards again.

##### Compare Recent reddit Karma
Background
Since we're all redditors here, let's make something dealing with reddit. If you go to a user's profile and add .json to the end of it, you can get the all sorts of Json data about the user (think of Json as a giant dictionary of smaller dictionaries and lists). For example, if I go to my own profile and view it's Json data, it would look like this[1] . At first it might look intimidating, but if you break it down, you can see it's just one giant dictionary with all sorts of information about my latest posts.
Goal
Create a program that gets information about two different users, and then sees whose most recent post received the most karma. The program should then print out which user received more karma, and what the difference was. This is a pretty open project, so I encourage you to take it further by adding more features if you find it interesting.
Remember - Elements in a list are referenced by their index numbers while entries in a dictionary are referenced by their keys.
Subgoals
Allow the user to put in the name of two different users when the program first begins.
If one of the names of the users does not exist (because of a spelling error), print out a message saying so.
Allow the user to keep comparing other users until the program is closed.
Display the amount of upvotes and downvotes each user received for their posts.
Not sure how to turn json data into usable python data? Check this out[2] .

##### Watch for new /r/TIL facts
Background
If you finished the previous project[1] which compared the karma of two new comments, hopefully you learned a thing or two about receiving data from Reddit's API. Now you're going to take this a step further, and even have the opportunity to make a basic twitter bot.
Goal
Create a program that receives data from the /r/todayilearned[2] subreddit, and looks for new facts that have been posted. Each time the program comes across a new fact, the fact should be printed into the command line. However, phrases like "TIL ", "TIL that", etc should be removed so the only thing that is printed is the fact.
>>New TIL API data here<<[3]
There are a couple things to note about this since you'll more than likely be using a loop to check for new posts. According to Reddit's API Access Rules Page[4] , the API pages are only updated once every thirty seconds, so you'll have to have your code pause for at least thirty seconds before it tries to find more posts. Secondly, if for some reason you decide to try to get data sooner than every thirty seconds, make sure to not send more than thirty requests per minute. That is the maximum you are allowed to do.
Subgoal Ideas
There is actually a lot you can do once your program starts receiving facts. Instead of simply printing the facts, here are some ideas for what you can do with them. If you currently do not feel like you can accomplish these ideas, feel free to come back later when you have more experience.
Print the link to the source of the fact too.
Try to further clean up the fact by adding punctuation to the end if it is missing, capitalize the first word, etc.
Write the facts to a separate text file so you end up with a giant compilation of random facts.
Create a bot that posts the facts to twitter. This may sound hard, but it's actually pretty simple by using the "Python Twitter Tools[5] " module and following the guide posted here[6] . Remember, the maximum amount of characters you can use in a tweet is only 140, so you'll have to filter out facts that are longer than that.
By now you should be pretty familiar with python, so if you get ideas for improving your program, go for it!

##### Random Wikipedia Article
If you've been to Wikipedia, you may have noticed that there is a link to a random article on the left side of the screen. While it can be fun to see what article you get taken to, sometimes it would be nice to see the name of the article so you can skip it if it sounds boring. Luckily, Wikipedia has an API that allows us to do so (Click here[1] ).
However, there is a dilemma. Since Wikipedia has articles about topics from all over the world, some of them have special characters in the title. For example, the article about the spanish painter Erasto Cortés Juárez[2] has é and á in it. If you look at this specific article's API[3] , you will see that the title is "Erasto Cort\u00e9s Ju\u00e1rez" and that the \u00e9 and \u00e1 are replacing the two previously mentioned letters. (For information about what this is, start by checking out the first half of this page[4] in the documentation). To make your program work, you're going to have to handle this problem somehow.
Goal
Create a program that pulls titles from the official Wikipedia API and then asks the user one by one if he or she would like to read about that article. So if the first title is Reddit, then the program should ask something along the lines of "Would you like to read about Reddit?" If the user says yes, then the program should open up the article for the user to read.
HINT: Mouse over the hidden area below to see how the article's ID can be used to access the actual article. http://en.wikipedia.org/wiki?curid=39608394[5]
Subgoals
As mentioned before, do something about the possibility of unicode appearing in the title. Whether you want your program to simply filter out these articles or you want to actually turn the codes into readable characters, that's up to you.
Make the program pause once the user has selected an article to read, and allow him or her to continue browsing different article titles once finished reading.
Allow the user to simply press ENTER to be asked about a new article.

##### What’s the Weather?
- If you would like to know the basics of what an API is, check out [this](http://www.reddit.com/r/explainlikeimfive/comments/qowts/eli5_what_is_api/c3z9kok) post by iamapizza.
- Create a program that pulls data from OpenWeatherMap.org and prints out information about the current weather, such as the high, the low, and the amount of rain for wherever you live. 
- Subgoals:
  - Print out data for the next 5-7 days so you have a 5 day/week long forecast.
  - Print the data to another file that you can open up and view at, instead of viewing the information in the command line.
  - If you know html, write a file that you can print information to so that your project is more interesting. Here is an example of the results from what I threw together.[3]
- Tips:
  - APIs that are in Json are essentially lists and dictionaries. Remember that to reference something in a list, you must refer to it by what number element it is in the list, and to reference a key in a dictionary, you must refer to it by it's name.
  - Don't like Celsius? Add &units=imperial to the end of the URL of the API to receive your data in Fahrenheit.
