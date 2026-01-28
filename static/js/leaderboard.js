const loadingEl = document.getElementById("loading");
const errorEl = document.getElementById("error");
const tableEl = document.getElementById("leaderboard-table");
const tbody = tableEl.querySelector("tbody");

fetch("/api/leaderboard")
  .then(res => {
    if (!res.ok) throw new Error("API error");
    return res.json();
  })
  .then(players => {
    loadingEl.classList.add("hidden");
    tableEl.classList.remove("hidden");

    players.forEach((p, index) => {
      const tr = document.createElement("tr");

      if (p.username === window.CURRENT_USER) tr.classList.add("highlight");

      tr.innerHTML = `
        <td>${index + 1}</td>
        <td>${p.username}</td>
        <td>${p.kills}</td>
        <td>${p.kd}</td>
        <td>${p.hs_percent}%</td>
      `;
      tbody.appendChild(tr);
    });
  })
  .catch(err => {
    console.error(err);
    loadingEl.classList.add("hidden");
    errorEl.classList.remove("hidden");
  });
