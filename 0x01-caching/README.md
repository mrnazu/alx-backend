# Caching
A caching system is a mechanism used in computing to store and manage frequently accessed data or information in a temporary storage area called a cache. The purpose of caching is to improve the efficiency and speed of data retrieval by reducing the need to access the original source or database repeatedly.

## Background Context

In this project, you learn different caching algorithms.

Resources

Read or watch:

    Cache replacement policies - FIFO
    Cache replacement policies - LIFO
    Cache replacement policies - LRU
    Cache replacement policies - MRU
    Cache replacement policies - LFU

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What a caching system is
    What FIFO means
    What LIFO means
    What LRU means
    What MRU means
    What LFU means
    What the purpose of a caching system
    What limits a caching system have

Requirements
Python Scripts

    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/env python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle style (version 2.5)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

More Info
Parent class BaseCaching

All your classes must inherit from BaseCaching defined below:
```
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

# Cache replacement policies

In computing, cache replacement policies are optimizing instructions or algorithms which a computer program or hardware-maintained structure can utilize to manage a cache of information. Caching improves performance by keeping recent or often-used data items in memory locations which are faster, or computationally cheaper to access, than normal memory stores. When the cache is full, the algorithm must choose which items to discard to make room for new data.

The average memory reference time is:

T = m × T m + T h + E {\displaystyle T=m\times T_{m}+T_{h}+E}

where

    m m = miss ratio = 1 - (hit ratio)
    T m T_{m} = time to make main-memory access when there is a miss (or, with a multi-level cache, average memory reference time for the next-lower cache)
    T h T_{h}= latency: time to reference the cache (should be the same for hits and misses)
    E E = secondary effects, such as queuing effects in multiprocessor systems


## let's simplify this:

Imagine you have a `special place (cache)` where you keep your favorite toys. Sometimes, you can quickly find your toys there `(cache hit)`, and sometimes you have to go to your big toy box in the closet `(cache miss)`.

Now, let's talk about how long it takes to get your toys:

- **Miss Ratio (m):** This is like the chance of not finding your toy in the special place. The miss ratio is just the opposite of the hit ratio. So, if you often find your toys in the special place (high hit ratio), the miss ratio is low.

- **Time for a Miss (Tm):** If you can't find your toy in the special place, you have to go to the big toy box. This is how long it takes to get your toy from the big toy box.

- **Latency (Th):** Whether you find your toy in the special place or have to go to the big toy box, it takes a bit of time to grab your toy. This is the latency.

- **Secondary Effects (E):** Sometimes, other things can affect how quickly you get your toy, like waiting in line if you have many friends trying to get toys too.

Now, the total time to get your toy (Average Memory Reference Time, T) is calculated like this:

\[ T = \text{(chance of not finding your toy)} \times \text{(time to get your toy from the big toy box)} + \text{(time it takes to grab your toy)} + \text{(other effects like waiting in line)} \]

So, it's like figuring out how long, on average, it takes for you to get your toys considering the chances of finding them in the special place, going to the big toy box, and any other things that might slow you down.

In short, it's a way to see how fast you can get your toys, taking into account different situations!
