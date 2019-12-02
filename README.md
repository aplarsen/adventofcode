# Advent of Code

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