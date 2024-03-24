function factorial(num) {
  var res = 1;
  for (var i = 2; i <= num; i++) {
    res *= i;
  }
  return res;
}
var num = 5;
console.log(factorial(num));
