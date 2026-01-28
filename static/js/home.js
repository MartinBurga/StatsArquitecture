showLoading();

fetch("/api/home-stats")
  .then(r => r.json())
  .then(data => {
    renderHome(data);
    hideLoading();
  })
  .catch(() => showError());
