function solve(arr, k) {
    if (arr.length % k !== 0) {
        return false;
    }

    let my_hash = {};

    for (let num of arr) {
        my_hash[num] = (my_hash[num] || 0) + 1;
    }

    let keys = Object.keys(my_hash).map(Number).sort((a, b) => a - b);
    for (let key of keys) {

        while (my_hash[key] > 0) {

            for (let i = 0; i < k; i++) {

                let curr = key + i;

                if (!my_hash[curr] || my_hash[curr] <= 0) {
                    return false;
                }

                my_hash[curr]--;
            }
        }
    }

    return true;
}

console.log(solve([8,1,2,3,6,2,3,4,7],3));