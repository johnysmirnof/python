#Variable Names and Keywords.

#Variable names can be arbitrarily long. They can contain both letters and digits, but they have to begin with a letter or an underscore. Although it is legal to use uppercase letters, by convention we don't.If you do, remember that case matters. Bruce and bruce are different variables.

#CAUTION: Variable names can never contain spaces.

#The underscore character ( _ ) can also appear in a name. It is often in names with multiple words, such as my_name or price_of_tea_in_china. There are some situations in which names beginning with an underscore have special meaning, so a safe rule for beginners is to start all names with a letter.

#If you give a variable an illegal name, you get a syntax error. In the example below, each of the variable names is illegal.

#76trombones = "big parade"
#more$ = 1000000
#class = "Computer Science 101"

#76trombones is illegal because it does not begin with a letter. more$ is illegal because it contains an illegal character, the dollar sign. But what's wrong with class?

#It turns out that class is one of the Python keywords. Keywords define the language's syntax rules and structure, and they cannot be used as variable names. Python has thirty-something keywords (and every now and again improvements to Python introduce or eliminate one or two):

#and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield, true, false, none.

#You might want to keep this list handy. If the interpreter complains about one of your variable names and you don't know why, see if it is on this list.

#Programmers generally choose names for their variables that are meaningful to the human readers of the program - they help the programmer document, or remember, what the variable is used for.

#CAUTION: Beginners sometimes confuse "meaningful to the human readers" with meaningful to the computer. So they'll wrongly think that because they've called some variable average or pi, it will somehow automagically calculate an average, or automagically associate the variable pi with the value 3.14159. NO! The computer doesn't attach semantic meaning to your variable names.

#So you'll find some instructors who deliberately don't choose meaningful names when they teach beginners - not because they don't think it is a good habit, but because they're trying to reinforce the message that you, the programmer, have to write some program code to calculate the average, or you must write an assignment statement to give a variable the value you want it to have.

