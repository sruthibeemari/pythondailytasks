document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.querySelector('#search-name');
    const table = document.querySelector('#employee-table');
    const themeToggle = document.querySelector('#theme-toggle');
    const sidebarToggle = document.querySelector('#sidebar-toggle');
    const sidebarClose = document.querySelector('#sidebar-close');
    const appShell = document.querySelector('#app-shell');
    const THEME_KEY = 'ems-theme';
    const SIDEBAR_KEY = 'ems-sidebar';

    if (searchInput && table && table.tBodies[0]) {
        const rows = Array.from(table.tBodies[0].querySelectorAll('tr'));

        searchInput.addEventListener('input', function () {
            const query = this.value.trim().toLowerCase();

            rows.forEach(row => {
                const cells = Array.from(row.querySelectorAll('td'));
                const rowText = cells.map(cell => cell.textContent.toLowerCase()).join(' ');
                row.style.display = rowText.includes(query) ? '' : 'none';
            });
        });
    }

    function setTheme(isLight) {
        document.body.classList.toggle('light-theme', isLight);
        try {
            localStorage.setItem(THEME_KEY, isLight ? 'light' : 'dark');
        } catch (e) {}
        if (themeToggle) {
            themeToggle.textContent = isLight ? 'Dark mode' : 'Light mode';
        }
    }

    if (themeToggle) {
        const isLight = document.body.classList.contains('light-theme');
        themeToggle.textContent = isLight ? 'Dark mode' : 'Light mode';

        themeToggle.addEventListener('click', function () {
            setTheme(!document.body.classList.contains('light-theme'));
        });
    }

    function setSidebarCollapsed(collapsed) {
        if (!appShell || !sidebarToggle) {
            return;
        }

        appShell.classList.toggle('sidebar-collapsed', collapsed);
        document.documentElement.classList.toggle('sidebar-collapsed', collapsed);
        sidebarToggle.setAttribute('aria-expanded', collapsed ? 'false' : 'true');

        try {
            localStorage.setItem(SIDEBAR_KEY, collapsed ? 'collapsed' : 'open');
        } catch (e) {}
    }

    function isSidebarCollapsed() {
        return appShell && appShell.classList.contains('sidebar-collapsed');
    }

    if (appShell && sidebarToggle) {
        const collapsed = document.documentElement.classList.contains('sidebar-collapsed');
        if (collapsed) {
            setSidebarCollapsed(true);
        }

        sidebarToggle.addEventListener('click', function () {
            setSidebarCollapsed(!isSidebarCollapsed());
            // remove keyboard focus from the toggle to avoid browser auto-scrolling
            try { sidebarToggle.blur(); } catch (e) {}
        });

        if (sidebarClose) {
            sidebarClose.addEventListener('click', function () {
                setSidebarCollapsed(true);
                try { sidebarClose.blur(); } catch (e) {}
            });
        }
    }

    function showToast(message, type = 'success') {
        const container = document.querySelector('#toast-container');
        if (!container) return;
        const toast = document.createElement('div');
        toast.className = 'toast show ' + (type === 'success' ? 'alert-success' : type === 'danger' ? 'alert-danger' : 'alert-warning');
        toast.textContent = message;
        container.appendChild(toast);
        setTimeout(() => toast.classList.remove('show'), 3000);
        setTimeout(() => toast.remove(), 3400);
    }

    // Handle inline leave approve/reject forms via AJAX to update the UI immediately.
    document.querySelectorAll('.inline-action-form').forEach(form => {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const action = form.getAttribute('action');
            const row = form.closest('tr');

            fetch(action, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json'
                }
            }).then(resp => resp.json())
              .then(data => {
                  if (data && data.status) {
                      const statusEl = row.querySelector('.status-pill');
                      if (statusEl) {
                          statusEl.textContent = data.status;
                          statusEl.className = 'status-pill ' + data.status.toLowerCase();
                      }
                      const actions = row.querySelector('.leave-actions');
                      if (actions) {
                          actions.innerHTML = '<span class="dashboard-copy">—</span>';
                      }
                      showToast(data.message || 'Leave status updated successfully.', 'success');
                  } else if (data && data.error) {
                      showToast(data.error, 'danger');
                  } else {
                      showToast('Unexpected response from server.', 'danger');
                  }
              }).catch(err => {
                  console.error('Leave action failed', err);
                  showToast('Unable to update leave status. Try again.', 'danger');
              });
        });
    });
});
