function filterEvenNum(arr) {
  even = [];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) even.push(arr[i]);
  }
  return even;
}

var arr = [12, 23, 2, 1, 91, 16, 0];
console.log(filterEvenNum(arr));
