/* SGE Modern JavaScript - Sistema de Gestão de Estoque */

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize modern features
    initSidebar();
    initAnimations();
    initThemeToggle();
    initSearchEnhancements();
    initTableEnhancements();
    initFormEnhancements();
    initTooltips();
    initNotifications();
    
    // Sidebar functionality
    function initSidebar() {
        const sidebarToggle = document.querySelector('.sidebar-toggle');
        const sidebar = document.querySelector('.sidebar');
        
        // Remove any existing overlay first
        const existingOverlay = document.querySelector('.sidebar-overlay');
        if (existingOverlay) {
            existingOverlay.remove();
        }
        
        const sidebarOverlay = document.createElement('div');
        
        // Create overlay for mobile
        sidebarOverlay.className = 'sidebar-overlay';
        sidebarOverlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(2px);
            -webkit-backdrop-filter: blur(2px);
            z-index: 1040;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        `;
        document.body.appendChild(sidebarOverlay);
        
        // Toggle sidebar on mobile
        if (sidebarToggle && sidebar) {
            sidebarToggle.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                
                console.log('Sidebar toggle clicked'); // Debug log
                
                sidebar.classList.toggle('show');
                if (sidebar.classList.contains('show')) {
                    sidebarOverlay.style.opacity = '1';
                    sidebarOverlay.style.visibility = 'visible';
                    document.body.style.overflow = 'hidden';
                    console.log('Sidebar opened'); // Debug log
                } else {
                    closeSidebar();
                }
            });
        } else {
            console.warn('Sidebar toggle or sidebar element not found');
        }
        
        // Close sidebar when clicking overlay
        sidebarOverlay.addEventListener('click', closeSidebar);
        
        function closeSidebar() {
            if (sidebar) {
                sidebar.classList.remove('show');
                console.log('Sidebar closed'); // Debug log
            }
            sidebarOverlay.style.opacity = '0';
            sidebarOverlay.style.visibility = 'hidden';
            document.body.style.overflow = '';
        }
        
        // Close sidebar on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && sidebar?.classList.contains('show')) {
                closeSidebar();
            }
        });
        
        // Close sidebar when clicking outside (for better UX)
        document.addEventListener('click', function(e) {
            if (sidebar?.classList.contains('show') && 
                !sidebar.contains(e.target) && 
                !sidebarToggle?.contains(e.target)) {
                closeSidebar();
            }
        });
        
        // Highlight active menu item
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.sidebar .nav-link');
        
        navLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active');
            }
        });
    }
    
    // Animation system
    function initAnimations() {
        // Observe elements for scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-up');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        
        // Observe cards and metrics
        document.querySelectorAll('.card, .metrics-card').forEach(el => {
            observer.observe(el);
        });
        
        // Staggered animation for table rows
        const tableRows = document.querySelectorAll('tbody tr');
        tableRows.forEach((row, index) => {
            row.style.animationDelay = `${index * 0.05}s`;
            row.classList.add('fade-in-up');
        });
    }
    
    // Theme toggle functionality
    function initThemeToggle() {
        // Get saved theme preference or default to dark
        const savedTheme = localStorage.getItem('sge-theme') || 'dark';
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        
        // Apply saved theme
        document.documentElement.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);
        
        // Theme toggle event
        if (themeToggle) {
            themeToggle.addEventListener('click', function() {
                // Add transition class
                this.classList.add('transitioning');
                
                const currentTheme = document.documentElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                
                // Add smooth transition effect
                document.body.style.transition = 'all 0.3s ease';
                
                // Apply new theme
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('sge-theme', newTheme);
                
                // Update icon with animation
                updateThemeIcon(newTheme);
                
                // Remove transition classes after animation
                setTimeout(() => {
                    this.classList.remove('transitioning');
                    document.body.style.transition = '';
                }, 300);
            });
        }
        
        function updateThemeIcon(theme) {
            if (themeIcon) {
                // Add rotation animation
                themeIcon.style.transform = 'rotate(180deg)';
                
                setTimeout(() => {
                    themeIcon.className = theme === 'dark' ? 'bi bi-sun fs-5' : 'bi bi-moon fs-5';
                    themeIcon.style.transform = 'rotate(0deg)';
                }, 150);
            }
        }
    }
    
    // Enhanced search functionality
    function initSearchEnhancements() {
        const searchInputs = document.querySelectorAll('input[type="text"], input[type="search"]');
        
        searchInputs.forEach(input => {
            // Add search icon if not present
            if (!input.parentElement.querySelector('.search-icon')) {
                const icon = document.createElement('i');
                icon.className = 'bi bi-search search-icon';
                icon.style.cssText = `
                    position: absolute;
                    right: 12px;
                    top: 50%;
                    transform: translateY(-50%);
                    color: var(--text-muted);
                    pointer-events: none;
                `;
                
                input.parentElement.style.position = 'relative';
                input.parentElement.appendChild(icon);
                input.style.paddingRight = '40px';
            }
            
            // Live search functionality
            let searchTimeout;
            input.addEventListener('input', function() {
                clearTimeout(searchTimeout);
                searchTimeout = setTimeout(() => {
                    // Add loading state
                    this.classList.add('searching');
                    
                    // Remove loading state after delay
                    setTimeout(() => {
                        this.classList.remove('searching');
                    }, 500);
                }, 300);
            });
        });
    }
    
    // Table enhancements
    function initTableEnhancements() {
        const tables = document.querySelectorAll('.table');
        
        tables.forEach(table => {
            // Add hover effects to rows
            const rows = table.querySelectorAll('tbody tr');
            rows.forEach(row => {
                row.addEventListener('mouseenter', function() {
                    this.style.transform = 'scale(1.01)';
                });
                
                row.addEventListener('mouseleave', function() {
                    this.style.transform = 'scale(1)';
                });
            });
            
            // Make table more responsive
            if (!table.closest('.table-responsive')) {
                const wrapper = document.createElement('div');
                wrapper.className = 'table-responsive';
                table.parentNode.insertBefore(wrapper, table);
                wrapper.appendChild(table);
            }
        });
        
        // Enhanced action buttons
        const actionButtons = document.querySelectorAll('.btn-sm');
        actionButtons.forEach(btn => {
            btn.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px) scale(1.05)';
            });
            
            btn.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
            });
        });
    }
    
    // Form enhancements
    function initFormEnhancements() {
        const forms = document.querySelectorAll('form');
        
        forms.forEach(form => {
            // Add floating labels effect
            const inputs = form.querySelectorAll('.form-control, .form-select');
            inputs.forEach(input => {
                // Focus effects
                input.addEventListener('focus', function() {
                    this.parentElement.classList.add('focused');
                });
                
                input.addEventListener('blur', function() {
                    if (!this.value) {
                        this.parentElement.classList.remove('focused');
                    }
                });
                
                // Initial state
                if (input.value) {
                    input.parentElement.classList.add('focused');
                }
            });
            
            // Form validation feedback
            form.addEventListener('submit', function(e) {
                const submitBtn = this.querySelector('button[type="submit"]');
                if (submitBtn) {
                    submitBtn.innerHTML = '<span class="loading"></span> Processando...';
                    submitBtn.disabled = true;
                }
            });
        });
    }
    
    // Initialize tooltips
    function initTooltips() {
        // Simple tooltip system
        const tooltipElements = document.querySelectorAll('[data-tooltip]');
        
        tooltipElements.forEach(element => {
            element.addEventListener('mouseenter', function(e) {
                const tooltip = document.createElement('div');
                tooltip.className = 'custom-tooltip';
                tooltip.textContent = this.getAttribute('data-tooltip');
                tooltip.style.cssText = `
                    position: absolute;
                    background: var(--bg-secondary);
                    color: var(--text-primary);
                    padding: 8px 12px;
                    border-radius: 8px;
                    font-size: 0.875rem;
                    border: 1px solid var(--border-color);
                    box-shadow: var(--shadow-md);
                    z-index: 1060;
                    pointer-events: none;
                    opacity: 0;
                    transition: opacity 0.2s ease;
                `;
                
                document.body.appendChild(tooltip);
                
                // Position tooltip
                const rect = this.getBoundingClientRect();
                tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
                tooltip.style.top = rect.top - tooltip.offsetHeight - 8 + 'px';
                
                // Show tooltip
                setTimeout(() => {
                    tooltip.style.opacity = '1';
                }, 10);
                
                // Store reference for cleanup
                this._tooltip = tooltip;
            });
            
            element.addEventListener('mouseleave', function() {
                if (this._tooltip) {
                    this._tooltip.remove();
                    this._tooltip = null;
                }
            });
        });
    }
    
    // Chart enhancements
    function enhanceCharts() {
        // Wait for Chart.js to load
        if (typeof Chart !== 'undefined') {
            Chart.defaults.color = 'rgba(255, 255, 255, 0.8)';
            Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.1)';
            Chart.defaults.backgroundColor = 'rgba(108, 92, 231, 0.2)';
            
            // Update existing charts with modern colors
            Chart.instances.forEach(chart => {
                if (chart.data.datasets) {
                    chart.data.datasets.forEach(dataset => {
                        if (!dataset.backgroundColor || dataset.backgroundColor.includes('rgb')) {
                            dataset.backgroundColor = 'rgba(108, 92, 231, 0.2)';
                            dataset.borderColor = 'rgba(108, 92, 231, 1)';
                        }
                    });
                    chart.update();
                }
            });
        }
    }
    
    // Call chart enhancements after a delay to ensure Chart.js is loaded
    setTimeout(enhanceCharts, 1000);
    
    // Utility functions
    window.SGE = {
        showNotification: function(message, type = 'info') {
            const notification = document.createElement('div');
            notification.className = `alert alert-${type} notification-toast`;
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 1070;
                max-width: 300px;
                border-radius: 12px;
                box-shadow: var(--shadow-lg);
                transform: translateX(100%);
                transition: var(--transition-smooth);
            `;
            notification.innerHTML = `
                <i class="bi bi-info-circle me-2"></i>
                ${message}
                <button type="button" class="btn-close" onclick="this.parentElement.remove()"></button>
            `;
            
            document.body.appendChild(notification);
            
            // Show notification
            setTimeout(() => {
                notification.style.transform = 'translateX(0)';
            }, 100);
            
            // Auto remove
            setTimeout(() => {
                notification.style.transform = 'translateX(100%)';
                setTimeout(() => {
                    notification.remove();
                }, 300);
            }, 5000);
        },
        
        confirmDelete: function(url, message = 'Tem certeza que deseja excluir este item?') {
            if (confirm(message)) {
                window.location.href = url;
            }
        }
    };
    
    // Global error handling
    window.addEventListener('error', function(e) {
        console.error('SGE Error:', e.error);
    });
    
    // Initialize notifications functionality
    function initNotifications() {
        // Mark notifications as read when dropdown is opened
        const notificationsDropdown = document.getElementById('notificationsDropdown');
        if (notificationsDropdown) {
            notificationsDropdown.addEventListener('shown.bs.dropdown', function() {
                // Simulate marking as read
                setTimeout(() => {
                    const badge = this.querySelector('.badge.bg-danger');
                    if (badge) {
                        badge.style.animation = 'fadeOut 0.3s ease forwards';
                        setTimeout(() => badge.style.display = 'none', 300);
                    }
                }, 1000);
            });
        }
        
        // Add click handlers for notification items
        const notificationItems = document.querySelectorAll('.notification-item');
        notificationItems.forEach(item => {
            item.addEventListener('click', function(e) {
                e.preventDefault();
                this.style.opacity = '0.7';
                
                // Simulate navigation or action
                console.log('Notification clicked:', this.querySelector('.notification-title').textContent);
            });
        });
    }
    
    // Performance monitoring
    if ('performance' in window) {
        window.addEventListener('load', function() {
            setTimeout(() => {
                const perfData = performance.getEntriesByType('navigation')[0];
                console.log('SGE Load Time:', Math.round(perfData.loadEventEnd - perfData.fetchStart) + 'ms');
            }, 0);
        });
    }
});

// CSS additions for JavaScript features
const additionalStyles = `
    .searching {
        background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%236c5ce7' fill-opacity='0.4'%3E%3Cpath d='M10 2C10.5523 2 11 2.44772 11 3V4C11 4.55228 10.5523 5 10 5C9.44772 5 9 4.55228 9 4V3C9 2.44772 9.44772 2 10 2Z' transform='rotate(0 10 10)'%3E%3CanimateTransform attributeName='transform' attributeType='XML' type='rotate' from='0 10 10' to='360 10 10' dur='1s' repeatCount='indefinite'/%3E%3C/path%3E%3C/g%3E%3C/g%3E%3C/svg%3E") !important;
        background-repeat: no-repeat !important;
        background-position: right 12px center !important;
        background-size: 16px !important;
    }
    
    .notification-toast {
        backdrop-filter: blur(20px) !important;
    }
    
    .sidebar-overlay {
        backdrop-filter: blur(2px) !important;
        -webkit-backdrop-filter: blur(2px) !important;
        background: rgba(0, 0, 0, 0.25) !important;
    }
    
    @media (max-width: 768px) {
        .sidebar.show {
            transform: translateX(0);
        }
    }
`;

// Inject additional styles
const styleSheet = document.createElement('style');
styleSheet.textContent = additionalStyles;
document.head.appendChild(styleSheet);