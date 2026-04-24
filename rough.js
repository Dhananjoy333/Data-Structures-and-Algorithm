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
var reverse = function(x) {
    let rev = 0;

    while (x !== 0) {
        let digit = x % 10;
        x = Math.trunc(x / 10);
        console.log(digit)

        // Check overflow BEFORE multiplying
        if (rev > (2**31 - 1) / 10 || rev < -(2**31) / 10) {
            return 0;
        }

        rev = rev * 10 + digit;
    }

    return rev;
};
console.log(reverse(-123))