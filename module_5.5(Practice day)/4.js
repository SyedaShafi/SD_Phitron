function reverse(name) {
  var ans = '';
  for (let i = name.length - 1; i >= 0; i--) {
    ans += name[i];
  }
  return ans;
}
var namee = 'shafi';
console.log(reverse(namee));
