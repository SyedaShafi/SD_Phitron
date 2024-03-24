function removeDuplicate(nums) {
  var ans = [];
  var f = 0;
  for (var i = 0; i < nums.length; i++) {
    f = 0;
    for (var j = 0; j < ans.length; j++) {
      if (ans[j] == nums[i]) f = 1;
    }
    if (!f) ans.push(nums[i]);
  }
  return ans;
}

var nums = [1, 1, 2, 3, 4, 5, 5, 5, 5, 7];
console.log(removeDuplicate(nums));
