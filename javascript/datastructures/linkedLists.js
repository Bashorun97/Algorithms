class Node {
    constructor(data) {
        this.data = data;
        this.nextNode = undefined;
    }
}

class LinkedList {
    // startNode is none when linkedlist is empty
    constructor() {
        this.startNode = undefined;
    }

    insertNodeAtStart(data) {
        let node = new Node(data);
        node.nextNode = this.startNode;
        this.startNode = node;
        console.log(this.startNode);
    }

    insertNodeAtEnd(data) {
        let node = new Node(data);
        if (this.startNode === undefined) {
            this.startNode = node;
            console.log(this.startNode);
        }
        let n = this.startNode;
        while(n.nextNode !== undefined) {
            n = n.nextNode;
        }
        n.ref = node;
    }

    traverseList() {
        if(this.startNode === undefined) {
            console.log(`LinkedList is empty`);
        }
        else {
            let n = this.startNode;
            while(n !== undefined) {
                console.log(`Item: ${n.data}\n`);
                n = n.nextNode;
            }
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
linkedList.traverseList();
