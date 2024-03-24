var tmp = document.getElementsByTagName('h1');
// console.log(tmp);
document.getElementById('tmp').style.color = 'red';

var img = document.getElementById('img');

console.log(img.getAttribute('src'));

img.setAttribute('alt', 'picture');
console.log(img.getAttribute('alt'));

var hero = document.getElementById('hero');

console.log(hero.innerText);

var newDiv = document.getElementById('newDiv');

var p = document.createElement('p');
p.innerText = 'This is created using JS.';

newDiv.appendChild(p);

document.getElementById('submit-btn').addEventListener('click', function (e) {
  console.log('Yessss s');
});
