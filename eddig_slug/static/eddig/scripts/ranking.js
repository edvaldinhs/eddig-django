function loadPlayerData() {
    fetch('/get')
        .then(response => response.json())
        .then(data => {
            let tableBody = document.querySelector('#rankingTable tbody');
            tableBody.innerHTML = '';

            data.forEach(player => {
                let row = document.createElement('tr');

                let cellContent = document.createElement('td');
                cellContent.classList.add('cell-content');
                cellContent.innerHTML = `
                  <div class="name">
                      <p>${player.name}</p>
                  </div>
                  <div class="circle flips">${player.flips}</div>
                  <div class="circle time">${player.time}</div>
              `;
                row.appendChild(cellContent);

                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching player data:', error));
}

window.onload = loadPlayerData;
