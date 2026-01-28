document.addEventListener("DOMContentLoaded", () => {
  const loading = document.getElementById("loading");
  const error = document.getElementById("error");
  const content = document.getElementById("perfil-content");

  if (!content) return;

  loading.classList.remove("hidden");

  fetch(`/api/player/${window.CURRENT_USER}`)
    .then(res => {
      if (!res.ok) throw new Error("Error HTTP");
      return res.json();
    })
    .then(data => {
      document.getElementById("username").textContent = data.user.username;
      document.getElementById("kd").textContent = data.kd;
      document.getElementById("hs").textContent = data.headshot_pct;

      content.classList.remove("hidden");
    })
    .catch(err => {
      console.error(err);
      error.classList.remove("hidden");
    })
    .finally(() => {
      loading.classList.add("hidden");
    });
});
