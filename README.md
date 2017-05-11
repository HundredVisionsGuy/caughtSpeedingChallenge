# caughtSpeeding()
Let's say you got pulled over for speeding. This Python unit test challenge is designed for you to write a function (caughtSpeeding()) that will tell you what your fine will be depending on how much over the speed limit you were driving and whether it's your birthday or not (the cops are kind if it's your birthday).


**requirements:**
----------
* If your speed is 5 miles per hour over the speed limit or less, there is no ticket.
* If your speed is 6-15 miles per hour over the speed limit, the fine is $500.
* If your speed is 16-25 miles per hour over the speed limit, the fine is $1000.
* If your speed is more than 25 miles per hour over the speed limit, the fine is $1500.
* If your speed is more than 100 miles per hour, the fine is $2000 (and you might have to serve jail time, but that will be up to the judge, not this program)
* However, if it is your birthday on that day, the officer will take 5 off of your speed and calculate the fine based on that adjusted speed.

**Inputs:**
----------
* **caughtSpeeding()** receives three values (integer, integer & boolean): *speed*, *speed_limit*, and *isBirthday*
  * **speed** = mph your car is travelling when the cop tracked your speed
  * **speed_limit** = the posted speed limit where you were driving
  * **isBirthday** is a Boolean
    * True = if it's your birthday
    * False = if it's not your birthday

**Output:**
------------
Output will be a fine in the form of an integer (0, 500, 1000, 1500, 2000)

**Examples:**
inputs => output/s
--------------------------------
* 45 45 False => 0
* 51 45 False => 500
* 55 45 False => 500
* 61 40 False => 1000
* 100 55 False => 1500
* 81 55 False => 1500
* 105 55 False => 2000
* 65 55 True => 0
* 60 40 True => 500
* 65 40 True => 1000
* 103 55 True => 1500
