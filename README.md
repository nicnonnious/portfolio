# Nic Mapogha - Data Scientist Portfolio

A modern, responsive portfolio website showcasing Nic Mapogha's data science projects, skills, and professional experience.

## Features

- **Responsive Design**: Optimized for both desktop and mobile devices
- **Interactive Dashboards**: Visualizations of skills, projects, and expertise
- **Project Showcase**: Detailed project descriptions with images and links
- **Skills Visualization**: Interactive charts showing proficiency in various data science skills
- **Contact Form**: Easy way for potential employers or collaborators to get in touch

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend**: Python, Flask
- **Database**: SQLite (SQLAlchemy ORM)
- **Data Visualization**: Chart.js, D3.js, Plotly
- **Deployment**: Ready for deployment on platforms like Heroku, Vercel, or Netlify

## Installation and Setup

### Python Version Compatibility

**Important**: This project requires Python 3.10 or 3.11 due to compatibility issues between SQLAlchemy and Python 3.13. If you're using Python 3.13, you may encounter typing-related errors in SQLAlchemy.

1. Clone the repository
```
git clone https://github.com/nicnonnious/portfolio.git
cd portfolio
```

2. Create and activate a virtual environment with Python 3.10 or 3.11
```
# Using Python 3.10 (recommended)
python3.10 -m venv venv
# OR using Python 3.11
python3.11 -m venv venv

# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the application
```
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
portfolio/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── instance/               # Database files
│   └── portfolio.db        # SQLite database
├── static/                 # Static files
│   ├── css/                # CSS stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Image files
└── templates/              # HTML templates
    ├── index.html          # Home page
    ├── about.html          # About page
    ├── projects.html       # Projects listing
    ├── project_detail.html # Individual project page
    ├── contact.html        # Contact form
    ├── thank_you.html      # Thank you page after contact
    ├── dashboard.html      # Data visualization dashboard
    └── layout.html         # Base template
```

## License

MIT

## Contact

Nic Mapogha - [nicmapogha@gmail.com](mailto:nicmapogha@gmail.com)

Project Link: [https://github.com/ninonnious/portfolio](https://github.com/nicnonnious/portfolio) 