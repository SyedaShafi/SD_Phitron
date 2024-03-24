function isPalindrome(str) {
  var tmp = str;
  var j = str.length - 1;
  for (var i = 0; i < str.length; i++) {
    if (str[i] != tmp[j]) {
      return false;
    }
    j--;
  }
  return true;
}
var str = 'mumu';
if (isPalindrome(str)) console.log('Palindrome');
else console.log('Not palindrome');
