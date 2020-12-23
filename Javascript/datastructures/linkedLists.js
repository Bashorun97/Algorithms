class Node {
    constructor(data) {
        this.data = data;
        this.nextNode = undefined;
    }
}

class LinkedList {
    // startNode is none when linkedlist is empty
    constructor() {
        // startNode is always the node that starts the linkedList
        this.startNode = undefined;
    }

    insertNodeAtStart(data) {
        let node = new Node(data);
        
        node.nextNode = this.startNode;
        this.startNode = node;// startNode can be set here first or...
    }

    insertNodeAtEnd(data) {
        let node = new Node(data);
        if (this.startNode === undefined) {
            this.startNode = node; // ... or can be first set here
            
        }
        let n = this.startNode;
        while(n.nextNode !== undefined) {
            n = n.nextNode;
        }
        n.nextNode = node;
    }

    traverseList() {
        if(this.startNode === undefined) {
            console.log(`LinkedList is empty`);
        }
        else {
            let n = this.startNode;
            while(n !== undefined) {
                console.log(`Item: ${n.data}`)
                n = n.nextNode;
            }
        }
    }

    insertAfterItem (item, data) {
        let n = this.startNode;

        while(n !== undefined) {
            if (n.data == item) {
                break;
            }
            n = n.nextNode;
        }
        if (n === undefined) {
            console.log(`Item is not within the linked list or your are at the end of the Linked List.`);
        }
        else {
            let node = new Node(data);
            node.nextNode = n.nextNode;
            n.nextNode = node;
        }
    }

    insertBeforeItem (item, data) {
        if (this.startNode === undefined) {
            console.log(`Linked list has no element`);
        }
        
        if (item === this.startNode.item) { // this is as good as insertNodeAtStart
            let node = new Node(data);
            node.nextNode = this.startNode;
            this.startNode = node;
        }

        let n = this.startNode;
        while (n.nextNode !== undefined) {
            if (n.nextNode.data === item) {
                break;
            }
            n = n.nextNode;
        }
        if (n.nextNode === undefined) {
            console.log(`Item is not in list`)
        }
        else {
            let node = new Node(data);
            node.nextNode = n.nextNode;
            n.nextNode = node;
        }
    }

    insertAtIndex (index, data) {
        if (index === 1) {
            let node = new Node(data);
            node.nextNode = this.startNode;
            this.startNode = node;
        }
        let i = 1;
        let n = this.startNode;
        while(i < index - 1 && n !== undefined) {
            n = n.nextNode;
            i++;
        }
        if (n === undefined) {
            console.log(`IndexError: Index out of bounds`);
        }
        else {
            let node = new Node(data);
            node.nextNode = n.nextNode;
            n.nextNode = node;
        }
    }

    getListLength () {
        if (this.startNode === undefined) {
            console.log(`Empty linked List`);
        }
        else {
            let acc = 0;
            let n = this.startNode
            while (n !== undefined) {
                acc++;
                n = n.nextNode;
            }
            console.log(`Length of LinkedList is: ${acc}`);
        }
        return;
    }

    searchItem (item) {
        if (this.startNode === undefined) {
            return -1
        }
        var n = this.startNode;
        while (n !== undefined) {
            if (n.data == item) {
                console.log(n)
                console.log(`Item found`);
                return true;
            }
            else if (n.data !== item) {
                n = n.nextNode;
            }
        console.log(`Item not found`);
        return false;
        }
    }

    createList (list_length) { // allows a user create a list
        if (list_length == 0) {
            console.log (`No list of nodes created`);
            return
        }
        else {
            addNodes()
        }
    }

    deleteEnd () {
        if (this.startNode === undefined) {
            console.log(`No node element to delete`);
            return -1
        }
        else {
            let n = this.startNode;
            
            // while not yet at the end of linked list
            while (n.nextNode.nextNode !== undefined) {
                n = n.nextNode;
            }
            n.nextNode = undefined;
        }
    }

    deleteStart () {
        if (this.startNode === undefined) {
            console.log(`No element node to delete`);
            return -1
        }
        else {
            let n = this.startNode;
            this.startNode = this.startNode.nextNode; 
        }
    }

    deleteByValue (item) {
        if (this.startNode === undefined) {
            console.log(`No element node to delete`);
            return -1
        }
        // this is as good as the deletestartNode method above
        if (this.startNode.data === item) {
            this.startNode = this.startNode.item;
            return
        }

        let n = this.startNode;
        while (n.nextNode !== undefined) {
            if (n.nextNode.data === item) {
                break;
            }
            n = n.nextNode;
        }
        if (n.nextNode === undefined) {
            console.log(`Element not found in linked list`);
        }
        else {
            n.nextNode = n.nextNode.nextNode;
        }

    }
}
let linkedList = new LinkedList();

linkedList.insertNodeAtStart(10);
linkedList.insertNodeAtStart(5);
linkedList.insertNodeAtStart(11);
linkedList.insertNodeAtStart(12);
linkedList.insertNodeAtStart(1);

linkedList.insertNodeAtEnd(22);
linkedList.insertNodeAtEnd(-4);
linkedList.insertNodeAtEnd(-2);
linkedList.insertNodeAtEnd(129);

//insert before item
linkedList.insertBeforeItem(11, 100);

//Insert at index
linkedList.insertAtIndex(0, 140);

//Search item
//linkedList.searchItem(140);

// Delete at end
linkedList.deleteEnd();

//Delete at start
linkedList.deleteStart();

//Delete by value
linkedList.deleteByValue(100);

// Get list length
linkedList.getListLength();
console.log('\n');
console.log('Now Traversing...\n');
console.log('===================');

linkedList.traverseList();
console.log('===================\n');
console.log('Finished Traversing...');


