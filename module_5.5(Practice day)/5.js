function isPrime(num) {
  if (num == 1) return false;
  else {
    for (let i = 2; i < num; i++) {
      if (num % i == 0) return false;
    }
    return true;
  }
}
num = 12;
if (isPrime(num)) console.log(num + ' is a prime number');
else console.log(num + ' is not a prime number');
