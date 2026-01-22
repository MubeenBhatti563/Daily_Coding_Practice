/**
 * HTMX Configuration and Interceptors
 * Centralized HTMX settings and global event handlers
 */

// HTMX Configuration
htmx.config.timeout = 10000; // 10 second timeout
htmx.config.refreshOnHistoryMiss = true;
htmx.config.historyCacheSize = 10;

/**
 * Handle HTMX request errors
 */
document.body.addEventListener('htmx:responseError', (event) => {
  console.error('HTMX Error:', event.detail.xhr.status, event.detail.xhr.statusText);
  showNotification('An error occurred. Please try again.', 'error');
});

/**
 * Handle HTMX timeout errors
 */
document.body.addEventListener('htmx:timeout', (event) => {
  console.error('HTMX Timeout');
  showNotification('Request timed out. Please try again.', 'error');
});

/**
 * Show notification message
 * @param {string} message - Notification message
 * @param {string} type - 'success', 'error', 'warning', 'info'
 */
function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification--${type}`;
  notification.setAttribute('role', 'alert');
  notification.textContent = message;
  
  document.body.appendChild(notification);
  
  // Auto-remove after 5 seconds
  setTimeout(() => {
    notification.style.animation = 'slideUp 0.3s ease-out forwards';
    setTimeout(() => notification.remove(), 300);
  }, 5000);
}