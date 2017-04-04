# caughtSpeeding
Let's say you got pulled over for speeding. This Python unit test challenge is designed for you to write a function (caughtSpeeding()) that will tell you what your fine will be depending on the speed and whether it's your birthday or not (the cops are kind if it's your birthday).


**requirements:**
----------
* If the speed is 60 or less, there is no ticket.
* If the speed is between 61 and 80, the fine is $500.
* If the speed is between 61 and 80, the fine is $500,
* However, if it is your birthday on that day, your speed can be 5 mph greater (in all cases)

**Inputs:**
----------
* **caughtSpeeding()** receives two values (integer & boolean): *speed* and *isBirthday*
  * **speed** = mph your car is travelling when the cop tracked your speed
  * **isBirthday** is a Boolean
    * True = if it's your birthday
    * False = if it's not your birthday

**Output:**
------------
Output will be a fine in the form of an integer (0, 500, or 1000)

**Examples:**
inputs => output/s
--------------------------------
* 60 False => 0
* 61 False => 500
* 65 False => 500
* 65 True => 0
* 80 False => 500
* 81 False => 1000
* 85 False => 1000
* 65 True => 500
* 91 False => 1000
* 55 True => 0
