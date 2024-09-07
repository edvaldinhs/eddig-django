function loadPlayerData() {
  fetch('/get')
  .then(response => response.json())
  .then(data => {
      let tableBody = document.querySelector('#rankingTable tbody');
      tableBody.innerHTML = '';

      data.forEach(player => {
          let row = document.createElement('tr');

          let idCell = document.createElement('td');
          idCell.textContent = player.id;
          row.appendChild(idCell);

          let nameCell = document.createElement('td');
          nameCell.textContent = player.name;
          row.appendChild(nameCell);

          let flipsCell = document.createElement('td');
          flipsCell.textContent = player.flips;
          row.appendChild(flipsCell);

          let timeCell = document.createElement('td');
          timeCell.textContent = player.time;
          row.appendChild(timeCell);

          tableBody.appendChild(row);
      });
  })
  .catch(error => console.error('Error fetching player data:', error));
}

window.onload = loadPlayerData;