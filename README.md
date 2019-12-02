# Advent of Code

## 2019
I am using #adventofcode to practice Pandas in Python 3.8.  That means I will likely be using Pandas where the library is overkill, but I need to become more fluent in the Pandas API so I can apply it more easily when it is indicated.

### Day 1
* The first part was pretty easy.   I looked up the best ways to round down and remembered that the `//` operator does integer division and decided to use that instead of pulling in the math library.
* The second part made me think a little more because any good solution should involve recursion.  I resisted my urge to iterate through the rows and apply the recursive function.  Instead, I used `map` to apply the function to a list and save that list in a new column. 
* While both parts could be outputted simply by wrapping the result list in `sum()` (and not even add it to the df itself), I decided to use `df.aggregate()` to bring that method into my focus.
