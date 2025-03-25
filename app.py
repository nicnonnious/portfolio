from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Security headers
@app.after_request
def add_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Disable template caching
db = SQLAlchemy(app)

# Add context processor to make 'now' available to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Database Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    github_link = db.Column(db.String(200), nullable=True)
    live_link = db.Column(db.String(200), nullable=True)
    technologies = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Project {self.title}>'

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., Programming, Data Analysis, Machine Learning
    proficiency = db.Column(db.Integer, nullable=False)  # 1-100
    
    def __repr__(self):
        return f'<Skill {self.name}>'

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    field = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f'<Education {self.degree} at {self.institution}>'

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Experience {self.position} at {self.company}>'

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Contact {self.name}>'

# Routes
@app.route('/')
def index():
    projects = Project.query.order_by(Project.date_created.desc()).limit(3).all()
    skills = Skill.query.all()
    experiences = Experience.query.order_by(Experience.start_date.desc()).all()
    educations = Education.query.order_by(Education.start_date.desc()).all()
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)
    
    return render_template('index.html', 
                          projects=projects, 
                          skill_categories=skill_categories,
                          experiences=experiences,
                          educations=educations)

@app.route('/projects')
def projects():
    projects = Project.query.order_by(Project.date_created.desc()).all()
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:id>')
def project_detail(id):
    project = Project.query.get_or_404(id)
    return render_template('project_detail.html', project=project)

@app.route('/about')
def about():
    skills = Skill.query.all()
    experiences = Experience.query.order_by(Experience.start_date.desc()).all()
    educations = Education.query.order_by(Education.start_date.desc()).all()
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)
    
    return render_template('about.html', 
                          skill_categories=skill_categories,
                          experiences=experiences,
                          educations=educations)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()
        
        return redirect(url_for('thank_you'))
    
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/dashboard')
def dashboard():
    projects = Project.query.all()
    skills = Skill.query.all()
    
    # Prepare data for charts
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append({
            'name': skill.name,
            'proficiency': skill.proficiency
        })
    
    # Convert to JSON for JavaScript
    skill_data = json.dumps(skill_categories)
    
    return render_template('dashboard.html', 
                          projects=projects,
                          skill_data=skill_data)

# Create database tables
with app.app_context():
    db.create_all()
    
    # Add sample data if database is empty
    if not Project.query.first():
        sample_project = Project(
            title="Data Analysis Dashboard",
            description="A comprehensive dashboard for visualizing sales data and customer insights.",
            image="project1.jpg",
            github_link="https://github.com/nicmapogha/data-dashboard",
            live_link="https://data-dashboard-demo.herokuapp.com",
            technologies="Python, Flask, Pandas, Plotly, JavaScript, D3.js"
        )
        db.session.add(sample_project)
        
        # Add sample skills
        skills = [
            Skill(name="Python", category="Programming", proficiency=90),
            Skill(name="R", category="Programming", proficiency=85),
            Skill(name="SQL", category="Database", proficiency=80),
            Skill(name="Machine Learning", category="Data Science", proficiency=85),
            Skill(name="Data Visualization", category="Data Science", proficiency=90),
            Skill(name="Statistical Analysis", category="Data Science", proficiency=85),
            Skill(name="Deep Learning", category="Data Science", proficiency=75),
            Skill(name="Pandas", category="Libraries", proficiency=95),
            Skill(name="NumPy", category="Libraries", proficiency=90),
            Skill(name="Scikit-learn", category="Libraries", proficiency=85),
            Skill(name="TensorFlow", category="Libraries", proficiency=75),
            Skill(name="Tableau", category="Tools", proficiency=80),
            Skill(name="Power BI", category="Tools", proficiency=85),
            Skill(name="Git", category="Tools", proficiency=80),
            Skill(name="Docker", category="Tools", proficiency=70)
        ]
        db.session.add_all(skills)
        
        # Add sample education
        education = Education(
            institution="Lewis University",
            degree="Master of Science",
            field="Data Science",
            start_date=datetime(2023, 1, 5),
            end_date=datetime(2024, 12, 20),
            description="Focused on machine learning, statistical analysis, and big data technologies."
        )
        db.session.add(education)
        
        # Add sample experience
        experience = Experience(
            company="MDI AI Detection.",
            position="Lead Data Scientist",
            start_date=datetime(2025, 1, 20),
            end_date=None,  # Current position
            description="Designing and implementing advanced computer vision algorithms for real-time object detection and classification in surveillance systems"
        )
        db.session.add(experience)
        
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True) 