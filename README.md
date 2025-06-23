# Nicodemus N Mapogha - AI Developer Portfolio

[![Deploy static content to Pages](https://github.com/USERNAME/REPOSITORY/actions/workflows/static.yml/badge.svg)](https://github.com/USERNAME/REPOSITORY/actions/workflows/static.yml)

A modern, responsive portfolio website showcasing AI development expertise, computer vision projects, and professional experience.

## 🚀 Live Demo

Visit the live portfolio: [https://USERNAME.github.io/REPOSITORY](https://USERNAME.github.io/REPOSITORY)

## ✨ Features

- **Modern Design**: Dark theme with neural network animations
- **Responsive**: Optimized for desktop, tablet, and mobile devices
- **Interactive**: Smooth scrolling, fade-in animations, and hover effects
- **Performance**: Lightweight with optimized animations and fast loading
- **SEO Optimized**: Proper meta tags and semantic HTML structure

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Animations**: CSS animations and Intersection Observer API
- **Typography**: Inter and JetBrains Mono fonts
- **Deployment**: GitHub Pages with GitHub Actions

## 📂 Project Structure

```
resume/
├── .github/
│   └── workflows/
│       ├── deploy.yml       # Jekyll-based deployment (backup)
│       └── static.yml       # Static HTML deployment (main)
├── index.html               # Main portfolio page
├── portfolio.html           # Development version
├── portfolio2.html          # Alternative version
└── README.md               # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Git installed on your system
- A GitHub account
- Basic knowledge of HTML/CSS (for customization)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/USERNAME/REPOSITORY.git
   cd REPOSITORY
   ```

2. **Open locally**
   ```bash
   # Open index.html in your browser
   # On Windows
   start index.html
   # On macOS
   open index.html
   # On Linux
   xdg-open index.html
   ```

### GitHub Pages Deployment

1. **Fork or upload to GitHub**
   - Create a new repository on GitHub
   - Upload these files or push your local repository

2. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: "main" or "master"
   - Folder: "/ (root)"

3. **Automatic Deployment**
   - GitHub Actions will automatically deploy on every push
   - Check the Actions tab for deployment status
   - Site will be available at `https://USERNAME.github.io/REPOSITORY`

## 🎨 Customization

### Personal Information
Edit the content in `index.html`:

```html
<!-- Update these sections -->
<h1 class="hero-title">Your Name</h1>
<p class="hero-subtitle">Your Title</p>
<p class="hero-description">Your description...</p>

<!-- Contact information -->
<a href="mailto:your.email@example.com" class="contact-item">
    <span>✉</span> your.email@example.com
</a>
```

### Colors and Styling
Modify CSS variables in the `:root` section:

```css
:root {
    --primary-dark: #0a0a0a;      /* Background color */
    --accent-blue: #0066ff;       /* Primary accent */
    --accent-green: #00ff88;      /* Secondary accent */
    --text-primary: #ffffff;      /* Primary text */
    /* ... other variables */
}
```

### Content Sections
Update the timeline, projects, and skills sections with your own:
- Experience timeline
- Featured projects
- Technical skills
- Contact information

## 🔧 GitHub Actions Workflows

### Static Deployment (Recommended)
- **File**: `.github/workflows/static.yml`
- **Purpose**: Direct static HTML deployment
- **Triggers**: Push to main/master branch, manual dispatch
- **Speed**: Fast deployment (~1-2 minutes)

### Jekyll Deployment (Backup)
- **File**: `.github/workflows/deploy.yml`
- **Purpose**: Jekyll-based deployment with build process
- **Use**: If you want to add Jekyll features later

## 📱 Browser Support

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ⚠️ Internet Explorer (not recommended)

## 🐛 Troubleshooting

### Common Issues

1. **GitHub Pages not loading**
   - Check if GitHub Actions completed successfully
   - Verify repository settings → Pages configuration
   - Ensure `index.html` exists in the root directory

2. **Animations not working**
   - Check browser console for JavaScript errors
   - Ensure browser supports modern CSS features

3. **Fonts not loading**
   - Check internet connection (Google Fonts dependency)
   - Fonts will fallback to system fonts if unavailable

### Performance Tips

- Images: Compress images before adding to reduce load time
- Animations: Can be disabled by setting `prefers-reduced-motion`
- Fonts: Consider self-hosting fonts for better performance

## 📈 Analytics & SEO

To add Google Analytics:

```html
<!-- Add before closing </head> tag -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Design inspiration from modern AI/tech portfolios
- Neural network animations concept
- Inter and JetBrains Mono fonts from Google Fonts

---

**Note**: Remember to replace `USERNAME` and `REPOSITORY` with your actual GitHub username and repository name throughout this README and in the badge links. 