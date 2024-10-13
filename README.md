# Selection Sort Optimization

In this practice exercise, you will add a modification to selection sort to try to improve its performance. In traditional selection sort, the smallest element in the unsorted portion of the list is swapped into its final sorted position on each pass of the algorithm.

However, we can additionally swap the *largest* remaining element into its final sorted position on each pass. In other words, each pass over the list keeps track of both the smallest and largest elements, and swaps them both into their final positions. Since each pass puts *two* elements into place, we only need half the number of passes! In order to get a time savings, though, we need to be careful about we make comparisons. The algorithms is explained in more detail below.

## Starter Code

You are given the file `selection_sort.py`, which includes the implementation of selection sort that was covered in this week's lessons. It has a few modifications:

- It is in a class called `Sort`, which has two fields: `comps` and `moves`. These variables track the number of comparisons and moves made by the sorting algorithm, respectively. On creating an instance of the `Sort` class, `comps` and `moves` are initialized to zero.
- The `selection_sort()` uses the `compare()` method to compare two elements of a list while incrementing the `comps` field. For example, instead of:
    ```python
    if lst[j] < lst[index_min]:
    ```

    The method instead uses:
    ```python
    if self.compare(lst[j] < lst[index_min]):
    ```
This method returns the result of the comparison (`True` or `False`), and it will increment the count of comparisons that the class maintains.
- The `swap()` method has also been modified to increment the `moves` field by three, since each swap consists of three moves of data in memory.
- You are given a `random_list()` function that generates a random integer list of length `n`.
- You are given an `is_sorted()` function that checks whether a list is in sorted order.

## Steps to Complete

As mentioned above, we now wish to modify selection sort to additionally swap into place the next largest element with each pass. However, in order to actually get some savings in terms of comparisons, we need to be careful about how we implement the change.

During each pass of selection sort, we initialize the index of the minimum element seen so far (`index_min`) as the first element of the list. We then keep track of the index of the minimum value seen so far as we traverse the list, as pictured below:

<center>
<img
  src="/images/list-0.svg"
  alt="Comparing each element of the list to the element at index_min to track the minimum."
  style="width:400px;"
/>
</center>

One way of implementing our improvement to the algorithm would be to modify the inner loop so that we also track the index of the maximum value seen so far. This would require us additionally comparing each element to the element as `index_max`:

<center>
<img
  src="/images/list-1.svg"
  alt="Comparing each element of the list to the element at both index_min and index_max to track the min and max."
  style="width:400px;"
/>
</center>

Once the `index_min` and `index_max` are found, we could swap them into place:

<center>
<img
  src="/images/list-2.svg"
  alt="The contents of the list after the first pass of modified selection sort."
  style="width:400px;"
/>
</center>

However, you should *not* take this approach to implementing the modification. This is because we are doubling the number of comparisons we are making for each element in the inner loop in order to find `index_max`. Even though we are doing half as many passes over the list, that savings is canceled out by the fact that we are doubling the number of comparisons!

Instead of considering one element at a time in the inner loop, you should consider *two* elements at a time. You can again initialize `index_min` and `index_max` as the first element of the list, but now we consider both the elements at the second and third indexes. We do a comparison between these two elements to see which one is `lesser` and which one is `greater` compared to each other. We can then compare the `lesser` with the element at `index_min`, and compare the greater with the element at `index_max`:

<center>
<img
  src="/images/list-3.svg"
  alt="Considering two elements at a time in modified selection sort."
  style="width:400px;"
/>
</center>

The net effect is that we have processed two elements with only **three** comparisons. Before, we would have needed **four** comparisons to process two elements. This is a 25% savings in comparisons!

The next iteration of the inner loop would consider the next two elements:

<center>
<img
  src="/images/list-4.svg"
  alt="Considering the next two elements in modified selection sort."
  style="width:400px;"
/>
</center>

In this case, the lesser of the two elements became the new `index_min`, while `index_max` stayed the same because the greater of the two elements was not larger than it.

The final iteration of the inner loop considers the last two elements of the list:

<center>
<img
  src="/images/list-5.svg"
  alt="Considering the final two elements in modified selection sort."
  style="width:400px;"
/>
</center>

This time, `index_max` is updated but `index_min` stays the same. We now can swap the minimum and maximum values into their final sorted position:

<center>
<img
  src="/images/list-2.svg"
  alt="The contents of the list after the first pass of modified selection sort."
  style="width:400px;"
/>
</center>

1. Add code to `selection_sort_mod()` to swap the largest element in each pass into place (in addition
to swapping the smallest element into place) to achieve the 25% savings in the number of comparisons.

    Carefully study the algorithm as described above. Additionally, here are some hints:

      - Since you're now swapping *two* elements into place during each pass, you can perform half as many passes! The outer loop controls how many passes the algorithm makes.
      - Because the list is now being filled with the largest sorted elements from the end, the *inner* loop can stop one position earlier with each pass.
      - In order to get the savings in comparisons as described above, you will need to check two elements at a time for whether they should be the min or max of the current pass. You will probably find it helpful for the inner loop to advance two positions at a time by passing `2` as an optional third argument to the `range()` function.
      - It is possible that when swapping the element at `index_min` into position, you happen swap it with the element at `index_max`. In this case, you need to be careful about how you then make sure the maximum element gets swapped to the end of the list.

    Some other notes:

      - You can know you've implemented the modification successfully if there is a 25% reduction in comparisons as compared to the original `selection_sort()`.
      - Make sure your code works for both even-length and odd-length lists. It is recommended that you get the function working for even-length lists first, and then see what small modifications are necessary to make sure it works for odd-length lists.
      - If you get stuck trying to achieve three comparisons for every two elements, for partial credit you may implement the version that just considers one element for each iteration of the inner loop, and therefore has the same number of comparisons as the original algorithm (but puts the next largest element into place with each pass).

2. Run `selection_sort()` and `selection_sort_mod()` and compare the number of comparisons they make. `selection_sort_mod()` should make approximately 25% fewer comparisons! 
