const loadData = () => {
  let searchText = document.getElementById('input-field').value;
  document.getElementById('meals').innerHTML = '';
  document.getElementById('input-field').value = '';
  if (searchText.trim() === '') {
    searchText = 'a';
  }
  fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${searchText}`)
    .then((res) => res.json())
    .then((data) => displayMenu(data.meals));
};

const displayModal = async (ID) => {
  try {
    const response = await fetch(
      `https://www.themealdb.com/api/json/v1/1/lookup.php?i=${ID}`
    );
    const data = await response.json();
    document.getElementById('description').innerText =
      data.meals[0].strInstructions;
  } catch (error) {
    console.log(error);
  }
};

const displayMenu = (data) => {
  console.log(data);
  document.getElementById('meal-count').innerText = data.length;
  const meals = document.getElementById('meals');

  data.forEach((meal) => {
    const instructions = meal.strInstructions;
    const words = instructions.split(' ');
    const numWordsToShow = 10;
    const truncatedInstructions = words.slice(0, numWordsToShow).join(' ');
    const card = document.createElement('div');
    card.innerHTML = `
        <div class="card m-3" style="width: 18rem;">
        <img src="${meal.strMealThumb}" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">${meal.strMeal}</h5>
            <p class="card-text">${truncatedInstructions}.....</p>
            <button
            onclick = "displayModal('${meal.idMeal}')"
            type="button"
            class="btn btn-primary"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
            >
            Details
            </button>
        </div>
        </div>
    `;
    meals.appendChild(card);
  });
};

loadData();
