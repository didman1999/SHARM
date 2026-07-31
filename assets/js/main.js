/* ============================================================
   SHARM EXCURSIONS — Main JavaScript
   Handles: Navigation, Slider, Animations, Gallery, FAQ,
            Language Switching, Scroll Effects
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initHeroSlider();
  initScrollAnimations();
  initGalleryLightbox();
  initFaqAccordion();
  initBackToTop();
  initScrollProgress();
  initNewsletterForm();
  initGuestCounters();
  initTripTabs();
  initMobileFilters();
  initSearchForm();
  initCategoryCarousel();
  initReviewsCarousel();
});

/* ==========================================================
   NAVBAR
   ========================================================== */
function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const toggle = document.querySelector('.navbar-toggle');
  const menu = document.querySelector('.navbar-menu');

  if (!navbar) return;

  // Scroll effect
  let lastScrollY = 0;
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (scrollY > 50) {
      navbar.classList.add('scrolled');
      navbar.classList.remove('transparent');
    } else {
      navbar.classList.remove('scrolled');
      // Only add transparent if on homepage
      if (navbar.dataset.transparent === 'true') {
        navbar.classList.add('transparent');
      }
    }
    lastScrollY = scrollY;
  });

  // Initial state
  if (window.scrollY <= 50 && navbar.dataset.transparent === 'true') {
    navbar.classList.add('transparent');
  } else if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  }

  // Mobile toggle
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      toggle.classList.toggle('active');
      menu.classList.toggle('active');
      document.body.style.overflow = menu.classList.contains('active') ? 'hidden' : '';
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (menu.classList.contains('active') && !menu.contains(e.target) && !toggle.contains(e.target)) {
        toggle.classList.remove('active');
        menu.classList.remove('active');
        document.body.style.overflow = '';
      }
    });

    // Close on link click
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        toggle.classList.remove('active');
        menu.classList.remove('active');
        document.body.style.overflow = '';
      });
    });
  }

  // Language switcher (Dropdown)
  const langSelect = document.getElementById('langSelect');
  if (langSelect) {
    langSelect.addEventListener('change', (e) => {
      switchLanguage(e.target.value);
    });
  }
  
  // Apply saved language on load immediately to select
  const savedLang = localStorage.getItem('sharm_lang') || 'en';
  if (langSelect && savedLang !== 'en') {
    langSelect.value = savedLang;
    switchLanguage(savedLang);
  }
}

/* ==========================================================
   LANGUAGE SWITCHING
   ========================================================== */
function switchLanguage(lang) {
  const isRtl = (lang === 'ar' || lang === 'he');
  document.body.setAttribute('dir', isRtl ? 'rtl' : 'ltr');
  document.documentElement.setAttribute('lang', lang);

  // Update active button if they exist
  document.querySelectorAll('.lang-switch button').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
  
  const langSelect = document.getElementById('langSelect');
  if (langSelect && langSelect.value !== lang) {
    langSelect.value = lang;
  }

  // If language is English or Arabic, we use manual data-lang attributes
  // Otherwise, we let Google Translate handle it.
  if (lang === 'ar' || lang === 'en') {
      // Manual translation fallback for EN and AR
      document.querySelectorAll('[data-lang-en]').forEach(el => {
        let attr = 'lang' + lang.charAt(0).toUpperCase() + lang.slice(1);
        let text = el.dataset[attr];
        
        if (!text) {
          if (lang === 'ar' && el.dataset.langAr) text = el.dataset.langAr;
          else text = el.dataset.langEn;
        }
        
        if (text) {
          if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') el.placeholder = text;
          else el.innerHTML = text;
        }
      });
      
      // Trigger Google Translate back to original (English) if switching back to manual EN/AR
      const googleSelect = document.querySelector('.goog-te-combo');
      if (googleSelect && googleSelect.value !== '') {
          googleSelect.value = 'en'; // set to default
          googleSelect.dispatchEvent(new Event('change'));
      }
  } else {
      // Trigger Google Translate with retry mechanism
      let retries = 0;
      function tryTranslate() {
          const googleSelect = document.querySelector('.goog-te-combo');
          if (googleSelect && googleSelect.options.length > 0) {
              // Google sometimes uses 'iw' for Hebrew instead of 'he'
              let targetLang = lang;
              if (lang === 'he') targetLang = 'iw';
              
              googleSelect.value = targetLang;
              googleSelect.dispatchEvent(new Event('change'));
          } else if (retries < 20) { // Try for 10 seconds max
              retries++;
              setTimeout(tryTranslate, 500);
          }
      }
      tryTranslate();
  }

  document.querySelectorAll('[data-lang]').forEach(el => {
    el.style.display = el.dataset.lang === lang ? '' : 'none';
  });

  // Store preference
  localStorage.setItem('sharm_lang', lang);
}
// Apply saved language on load
(function() {
  const savedLang = localStorage.getItem('sharm_lang') || 'en';
  if (savedLang === 'ar') {
    document.body.setAttribute('dir', 'rtl');
    document.documentElement.setAttribute('lang', 'ar');
  }
})();

/* ==========================================================
   HERO SLIDER
   ========================================================== */
function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');
  if (slides.length <= 1) return;

  let current = 0;
  let interval;

  function showSlide(index) {
    slides.forEach((s, i) => {
      s.classList.toggle('active', i === index);
    });
    dots.forEach((d, i) => {
      d.classList.toggle('active', i === index);
    });
    current = index;
  }

  function nextSlide() {
    showSlide((current + 1) % slides.length);
  }

  function startAutoplay() {
    interval = setInterval(nextSlide, 5000);
  }

  function stopAutoplay() {
    clearInterval(interval);
  }

  // Dot clicks
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      showSlide(i);
      stopAutoplay();
      startAutoplay();
    });
  });

  // Touch/swipe support
  const slider = document.querySelector('.hero-slider');
  if (slider) {
    let startX;
    slider.addEventListener('touchstart', (e) => {
      startX = e.touches[0].clientX;
      stopAutoplay();
    });
    slider.addEventListener('touchend', (e) => {
      const diff = startX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) {
        if (diff > 0) {
          showSlide((current + 1) % slides.length);
        } else {
          showSlide((current - 1 + slides.length) % slides.length);
        }
      }
      startAutoplay();
    });
  }

  showSlide(0);
  startAutoplay();
}

/* ==========================================================
   SCROLL ANIMATIONS (Intersection Observer)
   ========================================================== */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.animate-on-scroll');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  elements.forEach(el => observer.observe(el));
}

/* ==========================================================
   GALLERY LIGHTBOX
   ========================================================== */
function initGalleryLightbox() {
  const items = document.querySelectorAll('.gallery-item, .trip-gallery-item');
  const lightbox = document.getElementById('lightbox');
  if (!lightbox || !items.length) return;

  const lightboxImg = lightbox.querySelector('img');
  const closeBtn = lightbox.querySelector('.lightbox-close');
  const prevBtn = lightbox.querySelector('.lightbox-prev');
  const nextBtn = lightbox.querySelector('.lightbox-next');
  let currentIndex = 0;
  const images = [];

  items.forEach((item, i) => {
    const img = item.querySelector('img');
    if (img) {
      images.push(img.src);
      item.addEventListener('click', () => {
        currentIndex = i;
        openLightbox(currentIndex);
      });
    }
  });

  function openLightbox(index) {
    lightboxImg.src = images[index];
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      currentIndex = (currentIndex - 1 + images.length) % images.length;
      lightboxImg.src = images[currentIndex];
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      currentIndex = (currentIndex + 1) % images.length;
      lightboxImg.src = images[currentIndex];
    });
  }

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') {
      currentIndex = (currentIndex - 1 + images.length) % images.length;
      lightboxImg.src = images[currentIndex];
    }
    if (e.key === 'ArrowRight') {
      currentIndex = (currentIndex + 1) % images.length;
      lightboxImg.src = images[currentIndex];
    }
  });
}

/* ==========================================================
   FAQ ACCORDION
   ========================================================== */
function initFaqAccordion() {
  const items = document.querySelectorAll('.faq-item');
  items.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (!question) return;

    question.addEventListener('click', () => {
      const wasActive = item.classList.contains('active');
      // Close all
      items.forEach(i => i.classList.remove('active'));
      // Toggle current
      if (!wasActive) {
        item.classList.add('active');
      }
    });
  });
}

/* ==========================================================
   BACK TO TOP
   ========================================================== */
function initBackToTop() {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 500);
  });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ==========================================================
   SCROLL PROGRESS BAR
   ========================================================== */
function initScrollProgress() {
  const bar = document.querySelector('.scroll-progress');
  if (!bar) return;

  window.addEventListener('scroll', () => {
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = (window.scrollY / docHeight) * 100;
    bar.style.width = scrolled + '%';
  });
}

/* ==========================================================
   NEWSLETTER FORM
   ========================================================== */
function initNewsletterForm() {
  const form = document.querySelector('.newsletter-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = form.querySelector('input[type="email"]');
    if (!input || !input.value) return;

    // Simulate success
    showToast('Thank you for subscribing!', 'success');
    input.value = '';
  });
}

/* ==========================================================
   GUEST COUNTERS
   ========================================================== */
function initGuestCounters() {
  document.querySelectorAll('.guest-counter').forEach(counter => {
    const minusBtn = counter.querySelector('.guest-minus');
    const plusBtn = counter.querySelector('.guest-plus');
    const countEl = counter.querySelector('.count');
    if (!minusBtn || !plusBtn || !countEl) return;

    const min = parseInt(counter.dataset.min || '0');
    const max = parseInt(counter.dataset.max || '20');

    function updateCount(delta) {
      let val = parseInt(countEl.textContent) + delta;
      val = Math.max(min, Math.min(max, val));
      countEl.textContent = val;

      // Update hidden input if exists
      const input = counter.querySelector('input[type="hidden"]');
      if (input) input.value = val;

      minusBtn.disabled = val <= min;
      plusBtn.disabled = val >= max;

      // Trigger price recalculation
      calculateBookingTotal();
    }

    minusBtn.addEventListener('click', () => updateCount(-1));
    plusBtn.addEventListener('click', () => updateCount(1));

    // Initial state
    minusBtn.disabled = parseInt(countEl.textContent) <= min;
  });
}

/* ==========================================================
   TRIP TABS (Detail page)
   ========================================================== */
function initTripTabs() {
  const tabs = document.querySelectorAll('.trip-tab');
  const contents = document.querySelectorAll('.trip-tab-content');
  if (!tabs.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.dataset.tab;
      tabs.forEach(t => t.classList.remove('active'));
      contents.forEach(c => c.classList.remove('active'));
      tab.classList.add('active');
      const content = document.getElementById(target);
      if (content) content.classList.add('active');
    });
  });
}

/* ==========================================================
   MOBILE FILTERS
   ========================================================== */
function initMobileFilters() {
  const filterBtn = document.querySelector('.mobile-filter-btn');
  const sidebar = document.querySelector('.filters-sidebar');
  const overlay = document.querySelector('.mobile-drawer-overlay');

  if (!filterBtn || !sidebar) return;

  filterBtn.addEventListener('click', () => {
    sidebar.classList.toggle('mobile-visible');
    if (overlay) overlay.classList.toggle('active');
  });

  if (overlay) {
    overlay.addEventListener('click', () => {
      sidebar.classList.remove('mobile-visible');
      overlay.classList.remove('active');
    });
  }
}

/* ==========================================================
   SEARCH FORM
   ========================================================== */
function initSearchForm() {
  const form = document.querySelector('.search-box');
  if (!form) return;

  const searchBtn = form.querySelector('.search-btn');
  if (searchBtn) {
    searchBtn.addEventListener('click', (e) => {
      e.preventDefault();
      // Navigate to trips page with filters
      window.location.href = 'trips.html';
    });
  }
}

/* ==========================================================
   CATEGORY CAROUSEL (horizontal scroll)
   ========================================================== */
function initCategoryCarousel() {
  const carousel = document.querySelector('.categories-carousel');
  if (!carousel) return;

  let isDown = false;
  let startX;
  let scrollLeft;

  carousel.addEventListener('mousedown', (e) => {
    isDown = true;
    startX = e.pageX - carousel.offsetLeft;
    scrollLeft = carousel.scrollLeft;
  });

  carousel.addEventListener('mouseleave', () => isDown = false);
  carousel.addEventListener('mouseup', () => isDown = false);
  carousel.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - carousel.offsetLeft;
    carousel.scrollLeft = scrollLeft - (x - startX) * 2;
  });
}

/* ==========================================================
   REVIEWS CAROUSEL
   ========================================================== */
function initReviewsCarousel() {
  const track = document.querySelector('.reviews-track');
  const prevBtn = document.querySelector('.reviews-prev');
  const nextBtn = document.querySelector('.reviews-next');
  if (!track) return;

  const cards = track.querySelectorAll('.review-card');
  if (cards.length <= 3) return;

  let position = 0;
  const cardWidth = cards[0].offsetWidth + 24; // card width + gap
  const maxPosition = -(cards.length - 3) * cardWidth;

  function updatePosition() {
    track.style.transform = `translateX(${position}px)`;
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      position = Math.min(position + cardWidth, 0);
      updatePosition();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      position = Math.max(position - cardWidth, maxPosition);
      updatePosition();
    });
  }
}

/* ==========================================================
   BOOKING PRICE CALCULATOR
   ========================================================== */
function calculateBookingTotal() {
  const priceAdult = parseFloat(document.querySelector('[data-price-adult]')?.dataset.priceAdult || '0');
  const priceChild = parseFloat(document.querySelector('[data-price-child]')?.dataset.priceChild || '0');
  const priceInfant = parseFloat(document.querySelector('[data-price-infant]')?.dataset.priceInfant || '0');

  const adults = parseInt(document.querySelector('.guest-counter[data-type="adults"] .count')?.textContent || '1');
  const children = parseInt(document.querySelector('.guest-counter[data-type="children"] .count')?.textContent || '0');
  const infants = parseInt(document.querySelector('.guest-counter[data-type="infants"] .count')?.textContent || '0');

  const subtotal = (priceAdult * adults) + (priceChild * children) + (priceInfant * infants);

  // Get discount
  const discountEl = document.querySelector('[data-discount]');
  const discountPercent = parseFloat(discountEl?.dataset.discount || '0');
  const discountAmount = subtotal * (discountPercent / 100);

  const total = subtotal - discountAmount;

  // Update UI
  const summaryEl = document.querySelector('.booking-summary');
  if (summaryEl) {
    const adultLine = summaryEl.querySelector('.summary-adults');
    const childLine = summaryEl.querySelector('.summary-children');
    const infantLine = summaryEl.querySelector('.summary-infants');
    const discountLine = summaryEl.querySelector('.summary-discount');
    const totalLine = summaryEl.querySelector('.summary-total');

    if (adultLine) adultLine.querySelector('.summary-value').textContent = `$${(priceAdult * adults).toFixed(0)}`;
    if (childLine) childLine.querySelector('.summary-value').textContent = `$${(priceChild * children).toFixed(0)}`;
    if (infantLine) infantLine.querySelector('.summary-value').textContent = `$${(priceInfant * infants).toFixed(0)}`;
    if (discountLine) {
      discountLine.style.display = discountPercent > 0 ? 'flex' : 'none';
      discountLine.querySelector('.summary-value').textContent = `-$${discountAmount.toFixed(0)}`;
    }
    if (totalLine) totalLine.querySelector('.summary-value').textContent = `$${total.toFixed(0)}`;
  }
}

/* ==========================================================
   TOAST NOTIFICATIONS
   ========================================================== */
function showToast(message, type = 'success') {
  const existing = document.querySelector('.toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.innerHTML = `
    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      ${type === 'success'
        ? '<path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>'
        : '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>'
      }
    </svg>
    <span>${message}</span>
  `;
  document.body.appendChild(toast);

  requestAnimationFrame(() => {
    toast.classList.add('show');
  });

  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

/* ==========================================================
   SMOOTH SCROLL FOR ANCHOR LINKS
   ========================================================== */
document.addEventListener('click', (e) => {
  const link = e.target.closest('a[href^="#"]');
  if (!link) return;
  const target = document.querySelector(link.getAttribute('href'));
  if (target) {
    e.preventDefault();
    const offset = 80;
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  }
});

/* ==========================================================
   LAZY IMAGE LOADING
   ========================================================== */
(function() {
  if ('IntersectionObserver' in window) {
    const imgObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          if (img.dataset.src) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
          }
          imgObserver.unobserve(img);
        }
      });
    });

    document.querySelectorAll('img[data-src]').forEach(img => imgObserver.observe(img));
  }
})();

/* ==========================================================
   SCROLL ANIMATIONS (INTERSECTION OBSERVER)
   ========================================================== */
document.addEventListener('DOMContentLoaded', () => {
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target); // Only animate once
      }
    });
  }, observerOptions);

  document.querySelectorAll('.fade-up').forEach(el => {
    observer.observe(el);
  });
});
