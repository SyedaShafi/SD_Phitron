var arr1 = [1, 2, 3, 34, 6, 8];
var arr2 = [1, 34, 8, 99];

var ans = [];

for (var i = 0; i < arr1.length; i++) {
  for (var j = 0; j < arr2.length; j++) {
    if (arr1[i] == arr2[j]) ans.push(arr1[i]);
  }
}

console.log(ans);
