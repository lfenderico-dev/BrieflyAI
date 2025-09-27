module.exports = {
content: [
    "./src/**/*.{js,ts,jsx,tsx,html}", // Make sure your content paths are correct
    // Add other paths where you use Tailwind classes
],
theme: {
    extend: {
    colors: {
        'accent': 'var(--color-accent)',
        'accent2': 'var(--color-accent2)',
    }
    },
},
plugins: [],
}