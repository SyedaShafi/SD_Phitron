function maxNum(arr) {
  var mx = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > mx) {
      mx = arr[i];
    }
  }
  return mx;
}
var arr = [12, 23, 2, 1, 91, 16, 0];

console.log(maxNum(arr));
