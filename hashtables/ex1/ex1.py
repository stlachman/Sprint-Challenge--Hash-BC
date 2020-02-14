#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # key = weight and value = index
    for index in range(length):
      item = weights[index]
      hash_table_insert(ht, key = item, value = index)

    for index in range(length):
      item = weights[index]
      if item < limit:
        # find complemnt of item
        item_complement = limit - item
        # check if index of complement exists
        item_pair_index = hash_table_retrieve(ht, item_complement)

        if item_pair_index is None:
          continue
        elif item_pair_index >= index:
          return (item_pair_index, index)
        else: 
          return (index, item_pair_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
