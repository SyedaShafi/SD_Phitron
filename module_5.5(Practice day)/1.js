function sumOfArr(arr) {
  var sum = 0;
  for (var i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}
var arr = [1, 2, 3, 4, 5, 6];
var res = sumOfArr(arr);
console.log(res);
