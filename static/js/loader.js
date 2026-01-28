export function showLoading() {
  document.getElementById("loading")?.classList.remove("hidden");
  document.getElementById("content")?.classList.add("hidden");
}

export function hideLoading() {
  document.getElementById("loading")?.classList.add("hidden");
  document.getElementById("content")?.classList.remove("hidden");
}

export function showError() {
  document.getElementById("loading")?.classList.add("hidden");
  document.getElementById("error")?.classList.remove("hidden");
}
