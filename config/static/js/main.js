// ===============================
// PAGE FADE-IN
// ===============================
document.addEventListener("DOMContentLoaded", () => {
  document.body.style.opacity = 0;
  document.body.style.transition = "opacity 0.3s ease-in";
  requestAnimationFrame(() => {
    document.body.style.opacity = 1;
  });
});

// ===============================
// LOADING INDICATOR ON NAVIGATION
// ===============================
document.addEventListener("click", (e) => {
  const link = e.target.closest("a");
  if (!link || link.target === "_blank") return;

  if (link.href && link.href.startsWith(window.location.origin)) {
    showLoader();
  }
});

function showLoader() {
  let loader = document.getElementById("page-loader");

  if (!loader) {
    loader = document.createElement("div");
    loader.id = "page-loader";
    loader.innerHTML = `
      <div style="
        position: fixed;
        inset: 0;
        background: rgba(255,255,255,0.7);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 2000;
      ">
        <div class="spinner-border text-primary"></div>
      </div>
    `;
    document.body.appendChild(loader);
  }
}

// ===============================
// SCROLL TO TOP BUTTON (OPTIONAL)
// ===============================
const scrollBtn = document.createElement("button");
scrollBtn.innerHTML = "⬆";
scrollBtn.style.cssText = `
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px;
  border-radius: 50%;
  border: none;
  background: #0d6efd;
  color: white;
  display: none;
  z-index: 1500;
`;
document.body.appendChild(scrollBtn);

window.addEventListener("scroll", () => {
  scrollBtn.style.display = window.scrollY > 200 ? "block" : "none";
});

scrollBtn.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});
