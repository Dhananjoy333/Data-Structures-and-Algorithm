// class Node{
//   constructor(val){
//     this.left = null
//     this.val = val
//     this.right = null
//   }
// }

// let one = new Node(1);
// let two = new Node(2);
// let three = new Node(3);
// let four = new Node(4);
// let five = new Node(5);
// let six = new Node(6);
// let eight = new Node(8);
// let nine = new Node(9);
// let ten = new Node(10);

// // connections
// five.left = three;
// five.right = four;

// three.left = two;
// three.right = nine;

// four.left = eight;
// four.right = ten;

// eight.left = one;
// eight.right = six;

// function inOrder_traversal(node){
//   if(node == null){
//     return
//   }
//   process.stdout.write(node.val + '->')
//   inOrder_traversal(node.left)
//   inOrder_traversal(node.right)
// }
// inOrder_traversal(five)
function permutation(arr){
    let res = []
    function backtrack(ind,subset){
        if(ind === arr.length){
            res.push([...subset])
            return
        }
        for(let i = 0;i<arr.length;i++){
            console.log(i)
        }
    }
    backtrack(0,[])
    return res
}
permutation([1,2,3])