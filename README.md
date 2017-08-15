This is a tutorial for the most simple and basic of Python scripting. Assuming that you have some coding experience you should find everything in this to be pretty straight forward and easy to learn. This uses Python 3.6. If you want to follow along and work with me, you can install python 3.6 through the terminal.

Before we begin, let's talk about what python is and what python isn't. Python is a powerful, high-level language that is great for beginnners and experts alike. It is used for almost everything, from this operating system, to APIs (Django), to making robots that fetch butter. I assume. Maybe.

Python allows for awesome ability to import in modules and code without losing integrity, and allowing the developer a greater control of whats going on.

https://xkcd.com/353/

|Installing Python 3.6|

The OS we are running right now already has a version of Python installed. We do NOT want to mess with our installed Python because our OS actually is using it. Go Figure. You can see what your current python version is by running:
```sh
python --version
```
Run that in the terminal and you should see something to the effect of:

```sh
Python 2.7.10
```

This is using 3.6 so we can get that by running:
```sh
brew search python
```
It will display a list of a few options. We want python3.

```sh
brew install python3
```

This installs the latest stable python next to what we have installed.

However we do not need to do this, simly because we can get into python as stands. To do this simply type in python into your terminal, and voila, python 2.7.x is good to go.

If you do follow the instructions above, you can enter into the environment by running python3 in the terminal.

|Printing to console|

So to begin, lets enter into python. Once there, it looks similiar to what we have seen before with node and pry.

To begin,lets start by creating our first hello world program.

run
```sh
touch print.py

atom print.py
```

Inside this, lets write

```py
print(
"Hello World!"
)
```

Now back to termminal, and run
```sh
python print.py
```

Woohoo our first python program.

|Input|

Next up, let's learn about inputs.

Python has a nifty little trick that allows us to work in an input. Start by creating a file, lets call it function.py. In this new file, we're going to put in an input.
```py
name = input("Please add name here: ")
print("Hello,", name)
```

Now run the command
```sh
python function.py
```
Pretty Freaking Cool.

Let's mix it up. Go back into the file and post in:
```py
def doubleInt(num):
    result = num * 2
    return result

def Main():
    num = int(input("Please enter an input: "))
    output = doubleInt(num)
    print output

if __name__ == "__main__":
    Main()
```

Run the file through python, and voila. Inputted, and doubled. Breaking the function apart,

```py
# declares the function
def doubleInt(num):
  # function is passing a num
  # doubles it, saves it into a variable
    result = num * 2
    # returns the result
    return result

def Main():
  # grabs the input from the command
  # int checks the input and converts it to integer
  # saves it to num
    num = int(input("Please enter an input: "))
    # num gets passed to the function
    # returned value gets saved to output
    output = doubleInt(num)
    # and printed
    print output

# this is a catch to prevent code from being ran when it is imported
if __name__ == "__main__":
    Main()
```

|Operators and If|
Operators are essentially the same as JS and Ruby.

Python allows for 7 basic Arithmetic operators
-Addition (+)
-Subtraction (-)
-Multiplication (*)
-Division (/)
-Modulus (%)
-Exponent (**) note this is not carrot.
-Floor Division (//)

We can put those into the following:
+= Plus Equals
-= Minus Equals
*= Times Equals
/= Divide Equals
%= Mod Equals
**= Exponent Equals
//= Float Divide Equals

Let's  put those into test:

```sh
touch if.py
```

Then post in
```py
num = int(input("Please enter a number:"))
if num > 0:
    print("The number is greater zero")
    print(num)
```

Test it out, same way as always.

Next add in
```py
elif num < 0:
    print("The number is less than zero")
    print(num)
```
Run it all together. Nifty.

|Writing a file|

More fun, writing a file. So make a new file, lets call it words.txt. Next lets make another file called createfile.py and copy and paste this code.

```py
def Main():
    words = ["cat", "hay", "goat", "roast"]

    with open("words.txt", 'w') as f:
        for word in words:
            f.write(word + "\n")

if __name__ == "__main__":
    Main()
```
Run it and take a lok at words.txt.

More nifty.

Now make another file, we'll call it printingfunction.py.
Post in:
```py
def Main():
    for step in range(5):
        print(step)

        words = ["cat", "bat", "rat", "tat", "hat"]

        for word in words:
            print(word)

if __name__ == "__main__":
    Main()

```

Woohoo, for loop.

This is just a beginner intro to python.

|LAB|

Now, using what you know about python, let's code our own operating systems!

No, how Super Mario? Just have to run pip and install pygame.

Fine.

I didn't want to play that anyway.

If we are done early, try the following:

Go ahead and create Fibbornacci's in Python. File is located in lib to start.
