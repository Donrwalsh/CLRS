### Exercise 2.1-1
**Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the array A = {31, 41, 59, 26, 41, 58}.**

| Step | 1 | 2| 3 | 4 | 5 | 6
| - | - | - | - | - | - | - |
|   | 31 | 41 | 59 | 26 | 41 | 58 |
| 1 | | | | | | | 
|   | **31** | ***41*** | 59 | 26 | 41 | 58 |
| 2 | | | | | | |
|   | **31** | **41** | ***59*** | 26 | 41 | 58 |
| 3 | ← | ← | ← | ← | | | 
|   | ***26*** | **31** | **41** | **59**  | 41 | 58 |
| 4 |  |  | ← | ← | ← | | 
|   | **26** | **31** | ***41*** | **41** | **59** | 58|
| 5 | | | | | ← | ← |
|   | **26** | **31** | **41** | **41** | ***58*** | **59**|

The idea here is that the step rows are indicating what action occurs in the row beneath them. Left-pointing arrows demonstrate that a ***number*** has been moved to a new position, and by following these arrows you can map an array element from its original position to its new destination.

### Exercise 2.1-2
**Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.**

The only necessary change is to change the `>` on line 5 to a `<`.

INSERTION-SORT(A)

1 `for  j = 2 to A.length`

2 &nbsp;&nbsp;&nbsp;&nbsp;`key = A[j]`

3 &nbsp;&nbsp;&nbsp;&nbsp;`//Insert A[j] into the sorted sequence A[1..j-1].`

4 &nbsp;&nbsp;&nbsp;&nbsp;`i = j - 1`

5 &nbsp;&nbsp;&nbsp;&nbsp;`while i > 0 and A[i] < key`

6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`A[i+1] = A[i]`

7 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`i = i - 1`

8 &nbsp;&nbsp;&nbsp;&nbsp;`A[i+1] = key`
