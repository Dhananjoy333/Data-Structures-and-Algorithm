var rotate = function(nums, k) {

    let n = nums.length
    let rotate = k%n 

    function swap(arr,l,r){
        while(l < r){
            [arr[l],arr[r]] = [arr[r],arr[l]]
            l++
            r--
        }
    }
    swap(nums,0,n-1)
    console.log(nums)
    swap(nums,0,rotate-1)
    console.log(nums)
    swap(nums,rotate, n-1)
    
    return nums
};
rotate([1,2,3,4,5,6,7],3)