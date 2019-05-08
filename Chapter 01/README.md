### Exercise 1.1-1
**Give a real-world example that requires sorting or a real-world example that requires computing a convex hull.**

Sorting: Alphabitizing the names of employees in order to count how many Johns are employed.

[Convex Hull](https://en.wikipedia.org/wiki/Convex_hull): Crafting dice of various sides (d12, d20, etc.)

### Exercise 1.1-2
**Other than speed, what other measures of efﬁciency might one use in a real-world setting**

Memory; wear-and-tear on physical hardware.

### Exercise 1.1-3
**Select a data structure that you have seen previously, and discuss its strengths and limitations.**

Human memory. Incredible ability to recall specific information on demand, but practically incapable of accurately describing it in its entirety (Have you seen this movie versus tell me every movie you've seen). Subject to unreliable precision as well as deterioration over time.

### Exercise 1.1-4
**How are the shortest-path and traveling-salesman problems given above similar? How are they different?**

They are similar in that they both deal with a map and care about the distance between points (cities and roads for example). Additionally, each problem seeks to produce a route that minimizes distance. They differ in that the shortest-path problem has a defined beginning point and end point with no stipulations on which or how many points must be traversed from beginning to end. The travelling salesman problem instead cares about hitting every destination along the way while ending at the original beginning point - this difference complicates the problem greatly.

### Exercise 1.1-5
**Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is “approximately” the best is good enough.**

Only-the-best: The methods and procedures used by surgeons during life-saving operations must use only the best available approach given the current understanding of medical science. Lives are literally on the line.

"apporximately"-the-best: The algorithm used by a cashier to determine proper change for a purchase need not be efficient, so long as it produces the correct figure.

### Exercise 1.2-1
**Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.**

On my phone, I have a list of contacts. I am able to sort this list by names (first or last), date added, date used, birthday and more. This application must include some sort of sorting algorithm as another user may have an entirely different list of contacts, but would need them to be sorted quickly just the same as me.

### Exercise 1.2-2
**Suppose weare comparing implementations of insertion sort and merge sort on the same machine. For inputs of size *n*, insertion sort runs in 8*n*<sup>2</sup> steps, while merge sort runs in 64*n*lg*n* steps. For which values of n does insertion sort beat merge sort**