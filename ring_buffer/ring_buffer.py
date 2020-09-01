from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        if self.capacity > self.storage.length:
            
            self.storage.add_to_head(item)
            
            self.current = self.storage.tail
        else:
            
            self.current.value = item

            
            if self.current is self.storage.head:
                
                self.current = self.storage.tail
            else:
                
                self.current = self.current.prev

    def get(self):
        
        list_buffer_contents = []

        
        last_node_item = self.storage.tail

        
        while last_node_item is not None:

            
            list_buffer_contents.append(last_node_item.value)
            last_node_item = last_node_item.prev

        return list_buffer_contents