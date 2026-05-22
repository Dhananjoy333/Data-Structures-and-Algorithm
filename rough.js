function maxFruits(fruits) {
    let left = 0
    let right = 0
    let maxi = 0
    const freq = {}
    let types = 0
    while (right < fruits.length) {
        if (freq[fruits[right]] == null) {
            freq[fruits[right]] = 1
            types++
        } else {
            freq[fruits[right]]++
        }
        if (types > 2) {
            freq[fruits[left]]--
            if (freq[fruits[left]] === 0) {
                delete freq[fruits[left]]
                types--
            }
            left++
        }   
        maxi = Math.max(maxi, right - left + 1)
        right++
    }
    return maxi
}
const num = [3,3,3,1,2,1,1,2,3,3,4];
console.log(maxFruits(num));
    let last = -1
    let secondLast = -1
    let lastCount = 0
    let curr = 0
    let max = 0
    for (let f of fruits) {
        if (f === last || f === secondLast) {
            curr++
        } else {
            curr = lastCount + 1
        }
        if (f === last) {
            lastCount++
        } else {
            lastCount = 1
            secondLast = last
            last = f
        }
        max = Math.max(max, curr)
    }
    return max
