// Loader functionality
class LoaderManager {
    constructor() {
        this.loader = document.getElementById('loaderOverlay');
        this.init();
    }

    init() {
        // Hide loader when page loads
        this.hide();
        
        // Handle page refresh/back navigation
        window.addEventListener('pageshow', () => {
            this.hide();
            this.enableFormButtons();
        });

        // Handle beforeunload to show loader when leaving page
        window.addEventListener('beforeunload', () => {
            this.show();
        });
    }

    show() {
        if (this.loader) {
            this.loader.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }
    }

    hide() {
        if (this.loader) {
            this.loader.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }

    enableFormButtons() {
        const submitButtons = document.querySelectorAll('button[type="submit"]');
        submitButtons.forEach(button => {
            button.disabled = false;
            if (button.classList.contains('submit-btn')) {
                button.innerHTML = 'Generate Fitness Plan';
            }
        });
    }
}

// Initialize loader manager when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.loaderManager = new LoaderManager();
});

// Global function to show loader (for form onsubmit)
function showLoader() {
    if (window.loaderManager) {
        window.loaderManager.show();
    } else {
        // Fallback
        const loader = document.getElementById('loaderOverlay');
        if (loader) {
            loader.style.display = 'flex';
        }
    }
    return true;
}