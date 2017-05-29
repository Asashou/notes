
# Homework 3: Iteration, the Built-In Functions, and File Paths

# Indexing Exercises

Using the example dataset, select only the described elements from each list


```python
scores = [0.2, 0.3, 0.9, 1.1, 2.2, 2.9, 0.0, 0.7, 1.3, 0.3, 0.5, 0.1, 0.0]
```

1) The third score

2) The last score

3) The 2nd through 5th score

4) Every second score (the first, third, fifth, etc)

5) Every score after the 4th score

6) Every second score from the 2nd to the 8th.


# Pure Iteration Exercises

## Exercise 2: A List of Squares

Calculate the square of each integer from 0 to 30, and put those squares in a list (i.e. [1, 4, 9, 16, ...])


## Exercise 3: Calculating the Mean
Without importing any python packages, how could you compute the mean of a list of numbers?


```python
data = [0.3, 0.2, 2.5, 0.6, 1.5, 0.1, 0.7, 0.5, 1.9, 2.1]
```

## Exercise 4: Title-Case Everything!
I listed the names of all my friends, but I left their names lower-case.  Using iteration,
how could I capitalize the first letter of their names?

```python
friends = ['joe', 'gina', 'mehtap', 'michael', 'peter', 'evgeny']
```



## Exercise 5: Summing two Lists

Make a new list that is the sum of the elements in listA and listB.  


```python
lista = [2, 3, 4, 5, 0, 0, 0, 2, 2, 0]
listb = [0, 4, 2, 4, 5, 1, 0, 5, 3, 5]
```



## Exercise 6: Two Lists to One Dictionary

My mood ring changes colors to tell my current emotion, but I always forget which color means which emotion.  Below are the list of colors and list of emotions, with each index matching to each list (i.e. the first color and the firt emotion go together.)  How could you make a 'ring' dictionary, so I could look up the color and get the emotion back?

```python
colors = ['red', 'blue', 'green']
moods = ['angry', 'calm', 'happy']
```


## Exercise 7: More Descriptive Labels

You have a list of single-charachter strings that represent conditions in your experiment: 'L', 'R', and 'C'.  You want to change those labels to full words so they are easier to read and understand, to 'Left', 'Right', and 'Center'.   How could you go about it?

**Hint**: A dictionary may be very useful here.


```python
conds = ['C', 'L', 'C', 'R', 'C', 'C', 'C', 'R', 'R', 'R']

```

## Exercise 8: Mean of Each Condition

Now you have two lists: a list of what group each patient was in, and a list of their performance scores.  Calculate the mean of each group's scores and put the means into a dictionary, so I can easily look up their values by just indexing the group's name.

**Sample**: means = {'A': 2.1, 'B': 4.2}


```python
groups = ['A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A']
scores = [0.2, 0.3, 0.9, 1.1, 2.2, 2.9, 0.0, 0.7, 1.3, 0.3]    
```



## Exercise 9: Get the Public Functions

The dir() function returns a list of strings!  Use list comprehension to make a new list that contains only the names that don't begin with an underscore.


