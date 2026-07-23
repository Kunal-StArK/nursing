/* ===========================================================
   Suganti Nursing Home — shared script.js
   Works with header.html (mobile menu) on every page
=========================================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* ---- Mobile nav toggle (expects #navToggle + #navMenu in header.html) ---- */
  var navToggle = document.getElementById('navToggle');
  var navMenu   = document.getElementById('navMenu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', function () {
      navMenu.classList.toggle('open');
      navToggle.classList.toggle('active');
    });
  }

  /* ---- Highlight current page link in nav ---- */
  var here = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-menu a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === here) a.classList.add('active');
  });

  /* ---- Animated stat counters (elements with .stat-num and data-count) ---- */
  var counters = document.querySelectorAll('.stat-num[data-count]');
  if (counters.length) {
    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var target = parseInt(el.getAttribute('data-count'), 10) || 0;
        var current = 0;
        var step = Math.max(1, Math.round(target / 60));
        var timer = setInterval(function () {
          current += step;
          if (current >= target) { current = target; clearInterval(timer); }
          el.textContent = current + (el.getAttribute('data-suffix') || '');
        }, 20);
        counterObserver.unobserve(el);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (c) { counterObserver.observe(c); });
  }

  /* ---- Simple reveal-on-scroll for cards/sections ---- */
  var revealEls = document.querySelectorAll('.card, .doctor-card, .testi-card, .gallery-item');
  if ('IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(18px)';
      el.style.transition = 'opacity .5s ease, transform .5s ease';
      revealObserver.observe(el);
    });
  }



  /* ---- Appointment form (expects #appointmentForm) ---- */
  var apptForm = document.getElementById('appointmentForm');
  if (apptForm) {
    apptForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = document.getElementById('apptNote');
      if (note) {
        note.textContent = 'Your appointment request has been sent. We will call to confirm your slot.';
        note.style.color = '#1F8FC4';
      }
      apptForm.reset();
    });
  }

});
