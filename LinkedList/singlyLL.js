class Node{
    constructor(val){
        this.val = val
        this.next = null
    }
}

class SinglyLL {
    constructor(){
        this.head = null
    }

    append(val){
        const new_node = new Node(val)
        if(this.head === null){
            this.head = new_node
        }else{
            let current = this.head
            while (current.next !== null){
                current = current.next
            }
            current.next = new_node
        }
    }

    traversal(){
        if(this.head === null){
            return 'Linked List is Empty'
        }else{
            let current = this.head
            while(current !== null){
                process.stdout.write(current.val + "->")
                current = current.next
            }
            console.log(null)
        }
    }

    insertAt(val,pos){
        const new_node = new Node(val)
        if(pos === 0){
            new_node.next = this.head
            this.head = new_node
        }else{
            let current = this.head
            count = 0
            prev_node = null
            while (current.next !== null && count < pos){
                prev_node = current
                current = current.next
                count++  
            }
            prev_node.next = new_node
            new_node.next = current
        }
    }
}

sll = new SinglyLL()
sll.append(5)
sll.append(9)
sll.append(14)
sll.append(13)
sll.append(1)
sll.append(10)
sll.append(21)
sll.traversal()