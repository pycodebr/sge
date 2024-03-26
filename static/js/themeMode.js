document.addEventListener('DOMContentLoaded', function() {
    const defaultTheme = 'light';
    const savedTheme = localStorage.getItem('themeMode');
    const checkDarkMode = document.getElementById('checkDarkMode');

    applyTheme(savedTheme ? savedTheme : defaultTheme);

    if (savedTheme === 'dark' || defaultTheme === 'dark') {
        checkDarkMode.checked = true;
    } else {
        checkDarkMode.checked = false;
    }
    
    checkDarkMode.addEventListener('change', function() {
        const checked = this.checked;
        const themeMode = checked ? 'dark' : 'light';
        applyTheme(themeMode);
        saveThemeMode(checked);
    });
});

function applyTheme(themeMode) {
    const html = document.querySelector('html');
    html.dataset.bsTheme = themeMode;
}

function saveThemeMode(checkedTheme) {
    const themeMode = checkedTheme ? 'dark' : 'light';
    localStorage.setItem('themeMode', themeMode);
}