const VideoCards = (data) => {
  document.getElementById('videosContainer').innerHTML = '';
  data.forEach((ele) => {
    // console.log(ele);
    // console.log('from data');
    const postedDate = ele.others.posted_date;
    const h = postedDate / 60;
    const m = postedDate % 60;
    const cardContainer = document.getElementById('videosContainer');
    const card = document.createElement('div');
    card.className = 'card p-3 m-3';
    card.style.width = '18rem';
    card.innerHTML = `
        <div class="position-relative">
          <img src="${ele.thumbnail}" class="card-img-top" alt="picture" />
          <p
            class="position-absolute bottom-0 end-0 bg-dark text-light p-1 rounded"
          >
         ${h > 0 || m > 0 ? Math.ceil(h) + ' hours and ' + m + ' mins ago' : ''}
          </p>
        </div>
        <div class="d-flex p-2">
          <div class="mt-4 ms-2">
            <img
              class="rounded-circle"
              src=" ${ele.authors[0].profile_picture}"
              style="width: 35px; height: 35px"
              alt=""
            />
          </div>
          <div class="card-body">
            <h5 class="card-title">${ele.title}</h5>
            <p class="card-text">
              ${ele.authors[0].profile_name}
               ${
                 ele.authors[0].verified
                   ? '<span class="p-1"><i class="bi bi-patch-check-fill text-primary fs-5"></i></span>'
                   : ''
               }
            </p>
            <p class="card-text">${ele.others.views} views</p>
          </div>
        </div>
      `;
    cardContainer.appendChild(card);
  });
};

const noDataAvailable = () => {
  document.getElementById('sorry').innerHTML = '';
  const sorryContainer = document.getElementById('sorry');
  const card = document.createElement('div');
  card.className = 'card border-0 mt-5 text-center';
  card.style.width = ' 24rem';
  card.innerHTML = `
          <img src="resources/Icon.png" class="card-img-top mx-auto " style="width: 120px; height: 120px" alt="..." />
          <div class="card-body">
            
            <p>
             <h1>Oops!! Sorry, There is no content here</h1>
            </p>
           
          </div>
        `;
  sorryContainer.appendChild(card);
  console.log('child appended');
};

const videosByCategory = async (catId) => {
  try {
    const response = await fetch(
      `https://openapi.programming-hero.com/api/videos/category/${catId}`
    );
    const data = (await response.json()).data;
    console.log(data.length);

    if (data.length == 0) {
      noDataAvailable();
    }

    const sortByViewBtn = document.getElementById('sortByViewBtn');
    sortByViewBtn.addEventListener('click', () => {
      const flag = sortByViewBtn.classList.contains('ascending');
      console.log(flag);
      if (flag) {
        console.log('ascending');
        const sortDataAsc = [...data].sort((a, b) => {
          const viewCountA = parseInt(a.others.views);
          const viewCountB = parseInt(b.others.views);
          return viewCountA - viewCountB;
        });
        sortByViewBtn.title = 'Descending';
        sortByViewBtn.classList.remove('ascending');
        VideoCards(sortDataAsc);
      } else {
        console.log('descending');
        const sortDataDes = [...data].sort((a, b) => {
          const viewCountA = parseInt(a.others.views);
          const viewCountB = parseInt(b.others.views);
          return viewCountB - viewCountA;
        });
        sortByViewBtn.title = 'Ascending';
        sortByViewBtn.classList.add('ascending');
        VideoCards(sortDataDes);
      }
    });

    VideoCards(data);
  } catch (error) {
    console.log(error);
  }
};

const displayCategory = (data) => {
  console.log(data);
  data.forEach((cat) => {
    console.log(cat.category);
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn fw-bold m-1 btn-light-secondary btn-sm';
    btn.textContent = cat.category;

    if (cat.category == 'All') {
      btn.classList.add('btn-red');
      videosByCategory(cat.category_id);
    }
    const categories = document.getElementById('buttons');
    categories.appendChild(btn);

    btn.addEventListener('click', () => {
      document.getElementById('sorry').innerHTML = '';
      document.getElementById('videosContainer').innerHTML = '';
      const buttons = document.querySelectorAll(
        '.btn.btn-light-secondary.btn-sm'
      );
      buttons.forEach((button) => {
        button.classList.remove('btn-red');
      });
      btn.classList.add('btn-red');
      videosByCategory(cat.category_id);
    });
  });
};

const loadData = async () => {
  try {
    const response = await fetch(
      `https://openapi.programming-hero.com/api/videos/categories`
    );
    const data = await response.json();

    displayCategory(data.data);
  } catch (error) {
    console.log('failed to load');
  }

  // fetch(`https://openapi.programming-hero.com/api/videos/categories`)
  //   .then((res) => res.json())
  //   .then((data) => displayCategory(data.data));
};

loadData();
