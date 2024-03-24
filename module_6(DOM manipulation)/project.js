function handleDeposite() {
  var depositeInput = document.getElementById('deposite-input').value;
  var depositeAmount = document.getElementById('deposite-amount').innerText;
  var depositeInputConverted = parseInt(depositeInput);
  var depositeAmountConverted = parseInt(depositeAmount);
  var sum = depositeAmountConverted + depositeInputConverted;
  document.getElementById('deposite-amount').innerText = sum;
  document.getElementById('deposite-input').value = '';

  var totalAmount = document.getElementById('total-amount').innerText;
  var totalAmountConverted = parseInt(totalAmount);
  var totalSum = totalAmountConverted + depositeInputConverted;
  document.getElementById('total-amount').innerText = totalSum;
  //   console.log(depositeAmount);
  //   console.log(depositeInput);
  //   console.log(sum);
}

function handleWithdraw() {
  var withdrawInput = document.getElementById('withdraw-input').value;
  var withdrawAmount = document.getElementById('withdraw-amount').innerText;
  var withdrawInputConverted = parseInt(withdrawInput);
  var withdrawAmountConverted = parseInt(withdrawAmount);
  var sum = withdrawAmountConverted + withdrawInputConverted;
  document.getElementById('withdraw-amount').innerText = sum;
  document.getElementById('withdraw-input').value = '';

  var totalAmount = document.getElementById('total-amount').innerText;
  var totalAmountConverted = parseInt(totalAmount);
  var totalSum = totalAmountConverted - withdrawInputConverted;
  document.getElementById('total-amount').innerText = totalSum;
}
