let index1: number = 1;

function turingTest() {
  let index2: number = 2;

  if (index2 > index1) {
    let index3: number = 3;
    index3++; // becomes 4
  }

  while (index1 < index2) {
    let index4: number = 4;
    index1++; // index1 becomes 2
  }

  console.log(index1); // 2
  console.log(index2); // 2
  console.log(index3); // ❌ ERROR
  console.log(index4); // ❌ ERROR
}