// ------------------------- find a even or odd ----------------
// var num = 47;
// if (num % 2 == 0) console.log('jur');
// else console.log('bijur');

// -----------------------sort an array -------------------

// var arr = [10, 3, 2, 9, 1, 5, 7, 8, 4, 6];

// for (var i = 0; i < arr.length; i++) {
//   for (var j = i + 1; j < arr.length; j++) {
//     if (arr[i] > arr[j]) {
//       var tmp = arr[i];
//       arr[i] = arr[j];
//       arr[j] = tmp;
//     }
//   }
// }

// console.log(arr)

// --------------------------- find the largest name --------------------------

var friends = ['rahim', 'karim', 'abdul', 'saalaamm', 'heroalom'];
var ans = '';
var sz = 0;
for (var i = 0; i < friends.length; i++) {
  if (friends[i].length > sz) {
    ans = friends[i];
    sz = friends[i].length;
  }
}
console.log(ans);
