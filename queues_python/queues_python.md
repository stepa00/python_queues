# Queues python

A queue is an abstract data type that represents a sequence of elements arranged according to a set of rules.

## Queue: First-In, First-Out (FIFO)

At any given time, a new element is only allowed to join the queue on one end called the **tail**.
When an element leaves the queue, then all of its followers shift by exactly one position towards the **head** of the queue.
**Enqueue** operation is adding an element to the FIFO queue.
**Dequeue** operation is retrieving element from the queue.

Enqueueing and dequeueing are two independent operations that nay be taking place at different speeds.
This fact makes FIFO queues the perfect tool for **buffering data** in streaming scenarios and for **scheduling tasks** that need to wait until some shared resource becomes available.

Queue can grow without bounds.
**Bounded queue** is fixed capacity known upfront.
This type of queue used for systems with scarce resources:
  1. By irreversibly rejecting elements that do not fit;
  2. By overwriting the oldest element in the queue.

Bounded queues can be used in camera internal buffers that take rapid photos.

Second option used for eviction of users from the head of the queue.
Users that stayed for too long in cache will be logged out, for example.

## Stack: Last-In, First-Out (LIFO)

Stack has only one entrance/exit called **top**.
New elements are **pushed** to the top of the stack.
Elements are **popped** from the stack when needed.
To get to the bottom of the stack one have to go through all the above elements.

## Deque: Double-Ended Queue

Deque allows to enqueue or dequeue elements from both sides of the queue.
There are two additional operations available for deques:
  1. **rotate left** - last element becomes first in the deque;
  2. **rotate right** - first element becomes last in the deque.

Examples of usage: load balancer or task scheduler working in a round-robin fashion;
in gui applications deques can store recently opened files and undo-redo their actions or navigate back and forth 
in the web browser.

## Priority queue: Sorted from high to low

Priority queue where each element must have an associated priority to compare against other elements.
The queue will maintain sorted order.

Such queue are better used for dynamically arriving elements.
In particular, shortest path in a weighted graph using Dijkstra's algorithm.

Note: Even though the priority queue is conceptually a sequence, its most efficient implementation builds on top of
the heap data structure, which is a kind of binary tree. Therefore, the terms heap and priority queue are sometimes
used interchangeably.

## Implementing queues in python

Here you can read more [Link](https://realpython.com/queue-in-python/#implementing-queues-in-python)
<!--- TODO: Read about this topic. --->

## Using queues in practice

Here is an interesting implementation of queues in the python realm.
<!---TODO: Follow this tutorials.--->














