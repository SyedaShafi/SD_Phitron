// map
const arr = [1, 2, 3, 4, 5];
const res = arr.map((x) => x * x);
console.log(...res);

// filter

const products = [
  { id: 1, name: 'apple', price: 500, color: 'golden' },
  { id: 2, name: 'xiaomi', price: 300, color: 'black' },
  { id: 3, name: 'samsung', price: 100, color: 'black' },
  { id: 4, name: 'samsung2', price: 123, color: 'black' },
  { id: 5, name: 'lenovo', price: 540, color: 'pink' },
  { id: 6, name: 'xiaomi', price: 506, color: 'pink' },
  { id: 7, name: 'lenovo', price: 509, color: 'golden' },
];

const result = products.filter((pd) => pd.color == 'black');
console.log(result);

// find
const re = products.find((pd) => pd.id == 1);
console.log(re);
