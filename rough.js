class Node{
    constructor(val,next){
        this.val = null
        this.next = null
    }
}

class SinglyLL {
    constructor(){
        this.head = null
    }

    insert(val){
        const new_node = val
        if(this.head === null){
            this.head = new_node
        }else{
            let current = this.head
            while (current.next != null){
                current = current.next
            }
            current.next = new_node
        }
    }

    traversal()
}