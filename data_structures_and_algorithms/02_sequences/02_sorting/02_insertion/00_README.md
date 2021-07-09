# Insertion sort


## Algorithm description

The algorithm works by taking a value (key) and comparing it to all the values
to the left of it in the sequence.

Algorithm starts by taking a key value and position beginning from the second
position of the array (notice this works only if the array has at least
two elements - no need to sort an array of one element).

Now, given any key position and value from the second to the last element of
the array, the value immediately to the left of the key overrides the value
in the key position, and the value at that position is overridden by the value
to its left until either the start of the array is reached or a value that
is lower than the key is found.

Notice that at this point we have a reference of the position where the low
value was noticed or -1 if the array start was reached.

After this iteration of shifting values and comparing, the value from either
the first position in the array, or from the right side of the value that was
lower than the key, is overridden by the key. In this manner, we now have
values in order from the start to the key's position.

This process continues until the last element of the array is reached, and
respectively the whole array is sorted.

An alternative to this would be to just swap values from the key position
until either the start of the array is reached or a lower value than the key.
This alternative eliminates the step that does the override with the key
after each swap sweep.
