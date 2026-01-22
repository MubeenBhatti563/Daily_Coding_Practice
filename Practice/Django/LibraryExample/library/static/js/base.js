/**
 * Base JavaScript functionality
 * Handles common UI interactions and HTMX configuration
 */

document.addEventListener('DOMContentLoaded', () => {
  initializeNavbar();
  initializeMessageAutoClose();
  initializeHTMXConfig();
});

/**
 * Initialize navbar hamburger menu
 */
function initializeNavbar() {
  const hamburger = document.querySelector('.navbar__hamburger');
  const navbarMenu = document.querySelector('.navbar__menu');

  if (!hamburger || !navbarMenu) {
    console.warn('Navbar elements not found');
    return;
  }

  hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    const isActive = hamburger.classList.toggle('active');
    navbarMenu.classList.toggle('active');
    hamburger.setAttribute('aria-expanded', isActive.toString());
  });

  // Close menu when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('nav')) {
      closeNavbarMenu();
    }
  });

  // Close menu on menu item click
  navbarMenu.querySelectorAll('.navbar__link').forEach((link) => {
    link.addEventListener('click', () => {
      closeNavbarMenu();
    });
  });

  function closeNavbarMenu() {
    hamburger.classList.remove('active');
    navbarMenu.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
  }
}

/**
 * Auto-close messages after 5 seconds
 */
function initializeMessageAutoClose() {
  const messages = document.querySelectorAll('[role="alert"]');
  
  if (messages.length === 0) return;

  messages.forEach((msg) => {
    setTimeout(() => {
      msg.style.animation = 'slideUp 0.3s ease-out forwards';
      setTimeout(() => {
        if (msg.parentNode) {
          msg.remove();
        }
      }, 300);
    }, 5000);
  });
}

/**
 * Initialize HTMX CSRF token configuration
 */
function initializeHTMXConfig() {
  document.body.addEventListener('htmx:configRequest', (event) => {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
    
    if (csrfToken) {
      event.detail.headers['X-CSRFToken'] = csrfToken;
    } else {
      console.warn('CSRF token not found on page');
    }
  });
}

/**
 * Add slideUp animation if not in CSS
 */
const style = document.createElement('style');
style.textContent = `
  @keyframes slideUp {
    from {
      opacity: 1;
      transform: translateY(0);
    }
    to {
      opacity: 0;
      transform: translateY(-20px);
    }
  }
`;
document.head.appendChild(style);