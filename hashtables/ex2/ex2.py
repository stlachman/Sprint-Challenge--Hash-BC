#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
  hashtable = HashTable(length)
  route = [None] * length

  for ticket in tickets:
    hash_table_insert(hashtable, key = ticket.source, value = ticket.destination)
  
  # The first ticket, Value of ticket == "NONE"
  stack = [hash_table_retrieve(hashtable, "NONE")]
  # used to update index in array
  current_index = 0

  while len(stack) > 0:
    current_ticket = stack.pop()
    route[current_index] = current_ticket
    current_index += 1
    next_destination = hash_table_retrieve(hashtable, current_ticket)
    if next_destination is not "NONE":      
      stack.append(next_destination)

  # follow trail
  return route[:-1]
