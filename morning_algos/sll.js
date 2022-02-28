// Nodes and Singly Linked Lists

// Node
class ListNode {
    constructor(value) {
        this.next = null;
        this.value = value;
    }
}

// Singly Linked List
class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    display() {
        if(this.head == null) {
            console.log("List is empty");
            return;
        }

        let output = "";

        let runner = this.head;

        while(runner != null) {
            output += runner.value;

            if(runner.next != null) {
                output += " - "
            }

            runner = runner.next;
        }

        console.log(output);
        return;
    }

    contains(target) {
        let runner = this.head;

        while(runner != null) {
            if(runner.value == target) {
                return true;
            }

            runner = runner.next;
        }

        return false;
    }

    addToHead(value) {
        let new_node = new ListNode(value);

        if(this.head == null && this.tail == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            new_node.next = this.head;
            this.head = new_node;
        }
    }

    addToTail(value) {
        let new_node = new ListNode(value);

        if(this.head == null && this.tail == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }
    }

    removeFront() {
        // if there are no items in the list
        if(this.head == null && this.tail == null) {
            console.log("List is empty")
            return;
        }

        // if there's only one item in the list
        else if (this.head.next == null) {
            this.head = null;
            this.tail = null;
            return;
        }

        // if there are 2 or more items in the list
        else {
            let temp = this.head;
            this.head = this.head.next;
            temp.next = null;
        }

        return;
    }

    removeBack() {
        // if there are no items in the list
        if(this.head == null && this.tail == null) {
            console.log("List is empty")
            return;
        }

        // if there's only one item in the list
        else if (this.head.next == null) {
            this.head = null;
            this.tail = null;
            return;
        }

        // if there are 2 or more items in the list
        else {
            // start at the head of the list
            let runner = this.head;

            // finds the second to last node, the node immediately preceding the tail
            while(runner.next != this.tail) {
                runner = runner.next;
            }

            // assigns second to last node as the new tail, then disconnects the previous tail from the new tail's .next attribute
            this.tail = runner;
            this.tail.next = null;

            return;
        }
    }
}

let sll = new SinglyLinkedList();
sll.display();
sll.addToTail(1);
sll.addToTail(2);
sll.addToTail(3);
sll.display();
sll.addToHead(1);
sll.addToHead(0);
sll.display();
sll.removeFront();
sll.display();
sll.removeBack();
sll.display();
console.log(sll.contains(2));
console.log(sll.contains(100));