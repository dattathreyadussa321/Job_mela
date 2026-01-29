// ========================================
// JOB MELA - ENHANCED JAVASCRIPT
// ========================================

// ========================================
// PAGE INITIALIZATION
// ========================================
document.addEventListener("DOMContentLoaded", () => {
  initPageTransitions();
  initScrollToTop();
  initLocationHashing();
});

// ========================================
// PAGE FADE-IN ANIMATION
// ========================================
function initPageTransitions() {
  // Smooth page fade-in
  document.body.style.opacity = 0;
  document.body.style.transition = "opacity 0.4s ease-in";
  
  requestAnimationFrame(() => {
    document.body.style.opacity = 1;
  });
}

// ========================================
// LOADING INDICATOR ON NAVIGATION
// ========================================
document.addEventListener("click", (e) => {
  const link = e.target.closest("a");
  
  // Skip if not a link or opens in new tab
  if (!link || link.target === "_blank") return;
  
  // Skip hash links (anchor navigation)
  if (link.href && link.href.includes("#")) return;
  
  // Show loader for internal navigation
  if (link.href && link.href.startsWith(window.location.origin)) {
    showLoadingIndicator();
  }
});

function showLoadingIndicator() {
  let loader = document.getElementById("page-loader");
  
  if (!loader) {
    loader = document.createElement("div");
    loader.id = "page-loader";
    loader.innerHTML = `
      <div style="
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(4px);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        animation: fadeIn 0.2s ease-out;
      ">
        <div class="spinner" style="margin-bottom: 1rem;"></div>
        <div style="color: white; font-weight: 600; font-size: 1.1rem;">Loading...</div>
      </div>
    `;
    document.body.appendChild(loader);
  }
}

// ========================================
// SCROLL TO TOP BUTTON
// ========================================
function initScrollToTop() {
  const scrollBtn = document.getElementById("scroll-to-top");
  
  if (!scrollBtn) return;
  
  // Show/hide based on scroll position
  window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
      scrollBtn.classList.add("visible");
    } else {
      scrollBtn.classList.remove("visible");
    }
  });
  
  // Scroll to top on click
  scrollBtn.addEventListener("click", () => {
    window.scrollTo({ 
      top: 0, 
      behavior: "smooth" 
    });
  });
}

// ========================================
// SMOOTH SCROLL FOR HASH LINKS
// ========================================
function initLocationHashing() {
  // Handle hash links for smooth scrolling
  document.addEventListener("click", (e) => {
    const link = e.target.closest("a");
    
    if (!link) return;
    
    const href = link.getAttribute("href");
    
    // Check if it's a hash link
    if (href && href.startsWith("#")) {
      e.preventDefault();
      
      const targetId = href.substring(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
        
        // Update URL without triggering page reload
        history.pushState(null, null, href);
      }
    }
  });
}

// ========================================
// CARD HOVER EFFECTS (ENHANCED)
// ========================================
document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card, .quick-card");
  
  cards.forEach(card => {
    card.addEventListener("mouseenter", function() {
      this.style.transition = "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)";
    });
  });
});

// ========================================
// SEARCH DEBOUNCING (PERFORMANCE)
// ========================================
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// ========================================
// MOBILE MENU ACTIVE STATE
// ========================================
document.addEventListener("DOMContentLoaded", () => {
  const currentPath = window.location.pathname;
  const navItems = document.querySelectorAll(".bottom-nav-item");
  
  navItems.forEach(item => {
    const itemPath = new URL(item.href).pathname;
    
    if (itemPath === currentPath) {
      item.classList.add("active");
    }
  });
});

// ========================================
// FORM VALIDATION HELPER
// ========================================
function validateForm(formElement) {
  const inputs = formElement.querySelectorAll("input[required], select[required]");
  let isValid = true;
  
  inputs.forEach(input => {
    if (!input.value.trim()) {
      isValid = false;
      input.style.borderColor = "var(--color-secondary)";
      
      // Reset border color after a delay
      setTimeout(() => {
        input.style.borderColor = "";
      }, 2000);
    }
  });
  
  return isValid;
}

// ========================================
// TOAST NOTIFICATIONS (SIMPLE)
// ========================================
function showToast(message, type = "info") {
  const toast = document.createElement("div");
  toast.style.cssText = `
    position: fixed;
    bottom: 100px;
    left: 50%;
    transform: translateX(-50%) translateY(100px);
    background: ${type === "success" ? "var(--gradient-primary)" : "var(--gradient-secondary)"};
    color: white;
    padding: 1rem 2rem;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    font-weight: 600;
    z-index: 10000;
    transition: transform 0.3s ease-out;
    max-width: 90%;
  `;
  toast.textContent = message;
  
  document.body.appendChild(toast);
  
  // Slide in
  requestAnimationFrame(() => {
    toast.style.transform = "translateX(-50%) translateY(0)";
  });
  
  // Remove after 3 seconds
  setTimeout(() => {
    toast.style.transform = "translateX(-50%) translateY(100px)";
    setTimeout(() => {
      document.body.removeChild(toast);
    }, 300);
  }, 3000);
}

// ========================================
// ACCESSIBILITY ENHANCEMENTS
// ========================================
document.addEventListener("DOMContentLoaded", () => {
  // Add keyboard navigation support
  document.addEventListener("keydown", (e) => {
    // Escape key closes modals/overlays
    if (e.key === "Escape") {
      const loader = document.getElementById("page-loader");
      if (loader) {
        loader.remove();
      }
    }
  });
  
  // Focus visible for keyboard navigation
  document.addEventListener("keydown", (e) => {
    if (e.key === "Tab") {
      document.body.classList.add("keyboard-nav");
    }
  });
  
  document.addEventListener("mousedown", () => {
    document.body.classList.remove("keyboard-nav");
  });
});

// ========================================
// PERFORMANCE: LAZY LOADING IMAGES
// ========================================
document.addEventListener("DOMContentLoaded", () => {
  if ("IntersectionObserver" in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          if (img.dataset.src) {
            img.src = img.dataset.src;
            img.removeAttribute("data-src");
            observer.unobserve(img);
          }
        }
      });
    });
    
    const lazyImages = document.querySelectorAll("img[data-src]");
    lazyImages.forEach(img => imageObserver.observe(img));
  }
});

// ========================================
// ANALYTICS HELPER (OPTIONAL)
// ========================================
function trackEvent(category, action, label) {
  // Placeholder for analytics integration
  console.log(`Event: ${category} - ${action} - ${label}`);
  
  // Example: Google Analytics
  // if (typeof gtag !== 'undefined') {
  //   gtag('event', action, {
  //     'event_category': category,
  //     'event_label': label
  //   });
  // }
}

// ========================================
// EXPORT FOR USE IN OTHER SCRIPTS
// ========================================
window.jobMela = {
  showToast,
  showLoadingIndicator,
  validateForm,
  trackEvent,
  debounce
};
