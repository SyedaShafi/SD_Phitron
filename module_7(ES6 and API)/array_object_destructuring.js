// array destructuring
const arr = [1, 2, 3, 4, 5];
const [a, b] = arr;
console.log(a, b);


// object destructuring
const obj = {
  name: 'shafi',
  age: 24,
  add: 'S Nagar',
};
const { name, age } = obj;
console.log(age);


// nested structure
const nested = [{ name: 'eka', age: 24 }, { friends: ['fr1', 'fr2', 'fr2'] }, {}];
console.log(nested[1].friends[2]);