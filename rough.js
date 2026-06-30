var mapWordWeights = function(words, weights) {
    let weightMap = {}
    let alphabetMap = {}
    let  i = 0;
    let res = ''
    for(let ch = 'a'.charCodeAt(0); ch <= 'z'.charCodeAt(0); ch++){
        weightMap[String.fromCharCode(ch)] = weights[i]
        alphabetMap[25-i] = String.fromCharCode(ch)
        i++
    }
    for(let word of words){
        let total = 0
        for(let ch = 0; ch < word.length; ch++){
            total += weightMap[word[ch]]
        }
        let modulo = total % 26
        res += alphabetMap[String(modulo)]
    }
    return res
};

console.log(mapWordWeights(["a","b","c"],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))