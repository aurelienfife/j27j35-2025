# Reverse a Queue using a Stack

 1. Enqueue all the data into the main queue
 2. Dequeue all the elements of the main queue, push them into a stack
 3. Pop all the elements of the stack, enqueue them back into main queue
 4. Main queue should be reverse order of origin

Pseudo-code
    
    
    function: reverse queue (receives main qeueue as argument 'q')
        create empty stack 's'
        while q is not empty, do:
            . dequeue q into temp
            . push temp into s
        end while
        while s is not empty, do:
            . pop s into temp
            . enqueue temp into q
        end while
        return q
    
    Main:
        create empty queue k
        fill in with sample data
        call reverse queue with k, save back into k
    
