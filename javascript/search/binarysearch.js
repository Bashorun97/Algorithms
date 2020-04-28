class binarySearch {
    constructor(target, array) {
        this.target = target;
        this.array = array;
    }

    search() {
        let high = this.array.length - 1;
        let low = 0;

        while(low <= high) {
            let mid = (high + low) / 2;
            if (this.array[mid] == this.target) {
                return `Found ${this.target} at position ${mid}`;
            }
            else if (this.array[mid] > this.target) {
                high = mid - 1
            }
            else {
                low = mid + 1;
            }
        }
        return `${this.target} not in array`;
    }
}
let arr = [1,2,3,4,5,6,7];
let target = 4;
console.log(new binarySearch(target, arr).search())

/*
// Recursive implementation

function BinarySearch(array, high, low, target) {
    let mid = low + (high + low) / 2;
    if (low[array] == target) {
        return mid;
    }
    else {
        return () => {
            if (mid[array] > target) {
                BinarySearch(array, mid - 1, low, target);
            }
            else {
                BinarySearch(array, high, mid + 1, target);
            }
        }
    }
    
}

let arr = [1,2,3,4,5,6,7];
let binS = BinarySearch(arr, arr.length - 1, 0, 4)
let binSS = binS(arr, arr.length - 1, 0, 4)
console.log(binSS);
*/