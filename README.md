
# Advent of Code

## 2020
I'm going to try not to poop out on Day 6 this year.

### Day 1
* Some easy list searching stuff.
* I figured that Part 2 would probably involve a deeper search, so I used numpy to find the sum and product instead of performing it manually.  This seems silly when I'm already double- and triple-looping through the list, but I was also interested in some reading on what is out there for list work.  I already know that I do not use numpy enough.

### Day 2
* Easy regex problem with some looping.
* I started writing the logic line as `match.group(4).count(match.group(3)` and quickly realized how cumbersome this is.  I had never used the `re.search().groups()` method before, but it was super handy to assign that to a custom list of variables with shorter, meaningful names.
* Part 2 required looking up the XOR operator, as I'm pretty sure I'd never used it before.
* The competitive solvers are FAST.  I had solutions entered for both parts by 14 minutes past the hour and received zero points.

### Day 3
* Pretty straightforward looping and logic.
* For part 2, I first tried `np.prod()` to get the product of the tree counts but quickly got an integer overflow.  I was really surprised that numpy would overflow at such a low number by default.  Instead of messing around with different data types, I decided to switch to `math.prod()`.
* I remembered that GitHub can display Jupyter notebooks natively, so I left today's code in a notebook.  There's really no need to clean these up into .py files when notebooks already display so nicely online.

### [Day 4 - Passport Processing](https://adventofcode.com/2020/day/4)
* Today was a fun couple of challenges.
* I tried to be as Pythonic as possible using list comprehensions for parsing the strings into passports.
* It splits the whole file into a list of passport strings by double-newline (`\n\n`).
* Next, it splits each passport string into a list of strings, then splits *that* string into a key, value dictionary on `:`.
* A lot happens in that one line, but it takes really great advantage of Python's list comprehension.
* I can never remember the pattern for checking if all elements of a list belong in another list,but I think today may have made it stick.  I think I realized what `all()` and `any()` do, finally.  That will probably help with Pandas work too.
* Part 2 required a lot more logic to decide whether a passport passes the test, so I abstracted that out into a function that could be mapped.
* All of the individual tests were pretty easy to implement.  I have been doing a lot of regex lately and am finally getting comfortable with the various methods.
* I messed up on the two that required a simple pattern, as I forgot to include a `$` at the end of the pattern.  There were presumably some passports with extra characters in this positions, which would pass the test but be invalid.
* The short-circuiting of having a function exit and return a value is really handy here.  The assumption (at the end) is that all of the tests were passed.  If any test fails, we can exit at that point and return a False to the list we are summing at the end.

### [Day 5 - Binary Boarding](https://adventofcode.com/2020/day/5)
* This seemed a lot harder at first than it ended up being. This is because 128 and 8 are nice round numbers, and the exact number of letters needed to filter the list was provided in each input.
* Only one row and column were left after looping through all of the instructions.
* In Part 1, I first solved it by holding a max seatid and increasing it with each check.
* When starting Part 2, I realized that building a list of seatids would be slicker.  This allowed me to compute a max and a filtered list starting from the same list.

### [Day 6 - Custom Customs](https://adventofcode.com/2020/day/6)
* I tried really hard not to abstract this out into a function, but it just didn't seem possible.
* Because the question list was unique within a group, I did not see a way to do this in a single line without some old-school looping.
* I found a place to use `set()`, which is always fun.
* Part 2 was a little more challenging.  I am not sure if there is a good way to use the boolean list filtering here, so I chose a more human-friendly approach.
* Start with person 0's endorsed questions and treat these as common.
* Move through the rest of the people in the group and remove any questions from the list if not seen in the current person.

## 2019
I am using #adventofcode to practice Pandas in Python 3.8.  That means I will likely be using Pandas where the library is overkill, but I need to become more fluent in the Pandas API so I can apply it more easily when it is indicated.

### Day 1
* The first part was pretty easy.   I looked up the best ways to round down and remembered that the `//` operator does integer division and decided to use that instead of pulling in the math library.
* The second part made me think a little more because any good solution should involve recursion.  I resisted my urge to iterate through the rows and apply the recursive function.  Instead, I used `map` to apply the function to a list and save that list in a new column.
* While both parts could be outputted simply by wrapping the result list in `sum()` (and not even add it to the df itself), I decided to use `df.aggregate()` to bring that method into my focus.

### Day 2
* No real opportunities to use Pandas today.  Just some list stuff.
* I was almost able to read the file of inputs without looking up the syntax.  Couldn't remember file.read() after the handle was created.
* In the loop, I goofed and didn't use `elif`.  Since the value of position 0 changed as a result of the first instruction, it actually ran the addition op and the multiplication one.  My first unit test failed, so I caught it right away and changed the `if`s to `elif`s.
* In part 2, the operation failed when trying to compute the second noun-verb pair.  That tipped me off that there was probably something wrong with resetting the memory of the computer back to the initial state.  Some variable tracing and a good Google search reminded me that Python lists are always assigned by reference, not by value.  That is, in the case of lists, issuing `memory = input` means these two variables point to the same address.  Thus, modifying one modifies the other.  My first solution involved using `copy.copy()` to produce a copy of the list, but I remembered that there was a more Pythonic idiom for this.  A couple of searches finally brought me to `[:]`.  This can be taken to mean slicing a list from the first element to the last element (which makes sense, given the syntax for list slicing), but it's not necessarily obvious that what is returned is a copy of that list.

Illustrative example of reference vs. value:

#### Copy by reference

```python
foo = [1,2,3]
bar = foo # Copy by reference
bar[1] = 4

# Same value
print(foo)
print(bar)
```

    [1, 4, 3]
    [1, 4, 3]



```python
# Same address
print(hex(id(foo)))
print(hex(id(bar)))
```

    0x1cddd5541c8
    0x1cddd5541c8

#### Copy by value


```python
foo = [1,2,3]
bar = foo[:] # Copy by value, a slice of all elements
bar[1] = 4

# Different values
print(foo)
print(bar)
```

    [1, 2, 3]
    [1, 4, 3]



```python
# Different addresses
print(hex(id(foo)))
print(hex(id(bar)))
```

    0x1cddd554248
    0x1cddd54acc8

### Day 3
* Yikes
* No issues reading the file and parsing it into a set of wires and instructions.
* I went down a wrong road on turning the instructions into a path because I didn't realize right away that all of the grid locations between the current position and the new location needed to be traversed first.  I just jumped to it instead of walking to it.
* Since the translation from one position to another could move in either axis, I decided to treat the step as a vector and apply some matrix math with ordered pairs.  This really simplified thinking about storing the locations in a list so that list could be processed later.
* I saw Parker Higgins [@xor](https://twitter.com/xor) talking about how searching for lists within lists seemed to be impossibly slow, so I decided to try building my list out of tuples instead of lists.  This worked fine on the test data but failed miserably on the real data.  I decided not to wait until it finished.  Parker also mentioned that searching for hashes would be faster than searching for lists, so I gave that a shot.  Of course the test data was still fast, but I also saw a marked improvement in the real data.  That is, it finished.
*  I probably could have done something with itertools to save the pairs to a new list at the same time as finding a matching hash, but I'm trying to avoid using itertools because it feels so un-Pythonic.  Going back through each list *once* to find pairs that matched a found hash was pretty quick.
* After finding the list of intersection points, computing the Manhattan distances was trivial with a simple `map()`, and then finding the minimum Manhattan was even easier with `min()`.
* Part 2 got me stuck for a little bit because I had a fencepost error while iterating through the lists of pairs to find the first instance of an intersection.  I walked off the end of the list a couple of times before realizing what was happening.  Thank goodness for Jupyter's preservation of state so I didn't have to keep finding the intersections over and over.
* Once the step counts were found, some simple `map()` and `min()` found the smallest sum
* *EDIT:* Whoa, I did not know about `set()`.  Once I replaced my terrible list search with a call to `set().intersection()`, the performance improved an unbelievable degree.  `set()` appears to automatically hash the values under the hood and then do some really quick searching.  I can tell that the hashing is occurring because trying the pairs as lists instead of tuples didn't work with a `unhashable type: 'list'` error.  That seems like a good thing to know about tuples...since they can be hashed, they can be used easily with the built-in `set` functions.

### Day 4
* Part 1 was pretty straighforward.  Iterate through a string representation of the possible integers (nice use of list comprehension and range).  Make some assumptions about what we see so we can break out of the loop early if a rule is violated.  Build a list of possible passwords, then count it.
* Part 2 was trickier because I kept getting tied up in fencepost errors at the edges of the string.  I finally let each loop walk off the ends of the array temporarily but pull the bounds in when calculating the difference.  Another thing that helped was remembering that the `or` operator is short-circuited, so checking for bounds before looking at the postion in the string allowed me to prevent errors in looking at characters.

### Day 5
* The hardest part about today was following the instructions. There are now instructions, opcodes, parameters, modes, and inputs, and it's tough to keep them all straight.
* The most challenging instruction was this: ```Parameters that an instruction writes to will never be in immediate mode.```  I had already looped through the parameters and modes to convert the parameters as indicated by the mode before seeing this, so it wasn't obvious to me that making changes to the program's codes  ignore the mode bit and just use the position mode in all cases.
* Once I made that connection and modified the instructions that set new values, it ran well.
* In Part 2, the only real adjustment (aside from adding handlers for new opcodes) was changing the jumps from always adding to sometimes needing to jump to a particular position.  The program ran on the first try and produced the right diagnostic code.

### Day 6
* I recognized this problem as a binary tree and hoped that my lack of ever really tackling this problem in a class would not hold me back.
* Part 1 went fairly quickly once I recognized it as simple recursion and didn't try to make it more complicated than it is.  I started trying to decide if an object had already been visited before tallying but soon realized that that wouldn't leave enough room for 42 orbits in the test case.  Simple recursion returned the right number on the first try.
* Part 2 was definitely a binary tree problem.  I resisted looking up the "right way" to solve this shortest-path problem and instead focused on solving it visually first.  I imagined that if each object had a list of jumps computed for it, I could work backward in each list to find the first common node between them.  My solution would rely on building these two lists, then finding that first matching node.
* I am pretty sure I had never done recursion with an array before. It was super tricky to write that function correctly to get the result to be not a tree of lists.  My biggest problem was that I tried to use ```append()``` and ```extend()``` first without realizing that they modify the lists directly and do not have a return type.  Instead, returning the combined lists needs to be done with the simple addition operator, except that it's adding lists.  The base case is an empty list, and the recursive call is ```[parent node name] + func(parent node name)```.
* Save the lengths of the jumps into a tuple, and then find the smallest sum of two numbers in the tuple.
