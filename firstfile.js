function bubbleSort (arr) {
  let i
  let j
  let temp
  for (i = 0; i < arr.length - 1; i++) {
    for (j = 0; j < arr.length - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
      }
    }
  }
  return arr
}

let arr = [5, 2, 9, 1, 5, 6]
let result = bubbleSort(arr)
console.log('排序结果：', result)
