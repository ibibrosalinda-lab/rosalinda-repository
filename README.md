Rosalinda P. Ib-ib | Portfolio Website

A modern, dynamic portfolio website built with Django, featuring a fully customizable admin interface for content management.

## 🌟 Features

- **Dynamic Content Management**: All content is editable through Django's powerful admin interface
- **Responsive Design**: Fully responsive layout that works on all devices
- **Skills Section**: Categorized skills with proficiency levels, experience years, and visual progress bars
- **Projects Gallery**: Showcase your work with images, descriptions, and tags
- **Education Timeline**: Display your educational background chronologically
- **Contact Section**: Social media links and contact information
- **About Section**: Personal bio and goals/drives
- **Hero Section**: Customizable tagline and call-to-action buttons

## 🛠️ Technology Stack

- **Backend**: Django 6.0.2
- **Database**: SQLite (default), can be switched to PostgreSQL/MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Admin Interface**: Django Admin with customizations
- **Image Processing**: Pillow

## 📦 Installation

### Prerequisites

- Python 3.14 or higher
- pip (Python package manager)
- Git (optional)

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd rosalinda-portfolio
Step 2: Create Virtual Environment
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Step 4: Environment Variables
Create a .env file in the project root:

env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
Step 5: Database Setup
bash
python manage.py makemigrations
python manage.py migrate
Step 6: Create Superuser
bash
python manage.py createsuperuser
Follow the prompts to create an admin account.

Step 7: Run Development Server
bash
python manage.py runserver
Visit http://127.0.0.1:8000 to view the site and http://127.0.0.1:8000/admin to access the admin panel.

🗂️ Project Structure
text
portfolio_project/
├── ib_ib/                  # Main app directory
│   ├── migrations/         # Database migrations
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   ├── admin.py           # Admin interface configuration
│   ├── models.py          # Database models
│   ├── views.py           # View controllers
│   ├── urls.py            # URL routing
│   └── context_processors.py # Global context data
├── media/                 # User-uploaded files
├── static/                # Collected static files
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── db.sqlite3            # SQLite database
🎨 Admin Panel Features
Hero/About Section
Edit tagline and bio paragraphs

Upload profile image

Customize CTA button text and link

Skills Management
Create skill categories (e.g., "Backend", "Frontend", "Tools")

Add skills with:

Name and icon

Proficiency level (Beginner/Intermediate/Advanced/Expert)

Percentage level (0-100%)

Years of experience

Active/inactive status

Projects Gallery
Add projects with titles and descriptions

Add tags (comma-separated)

Upload project images

Add live demo/GitHub links

Reorder projects

Education Timeline
Add degrees/certifications

School/institution names

Start and end years

Reorder entries

Contact Information
Custom intro message

Email address

Social media links (LinkedIn, GitHub, Instagram)

🔧 Customization
Styling
The main CSS file is located at:

text
ib_ib/static/css/style.css
Templates
All HTML templates are in:

text
ib_ib/templates/
Adding New Models
Add model class to models.py

Register model in admin.py

Run python manage.py makemigrations

Run python manage.py migrate

🚀 Deployment
Deploy to Render
Push your code to GitHub

Create a new Web Service on Render

Connect your repository

Use these settings:

Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

Start Command: gunicorn your_project.wsgi:application

Deploy to PythonAnywhere
Upload files to PythonAnywhere

Set up virtual environment

Configure WSGI file

Set up static files mapping

Environment Variables for Production
env
DEBUG=False
SECRET_KEY=your-strong-production-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
📝 Content Management Guide
Adding Skills
Go to Admin → Skill Categories → Add

Create a category (e.g., "Programming Languages")

Go to Skills → Add

Fill in skill details:

Name: "Python"

Category: Select from dropdown

Level: 70

Proficiency: Intermediate

Years of experience: 2.5

Icon: "fab fa-python" (FontAwesome class)

Adding Projects
Go to Admin → Projects → Add

Fill in:

Title: "E-commerce Website"

Description: "Full-featured online store"

Tags: "Django, Python, Stripe"

Link: "https://github.com/yourusername/project"

Link label: "View on GitHub"

Upload screenshot

🐛 Troubleshooting
Common Issues
Database errors after model changes:

bash
python manage.py makemigrations
python manage.py migrate
Static files not loading:

bash
python manage.py collectstatic
Admin panel not showing models:

Check if models are registered in admin.py

Ensure app is in INSTALLED_APPS

📄 License
This project is open-source and available under the MIT License.

👤 Author
Rosalinda P. Ib-ib

Portfolio: [your-portfolio-url]

GitHub: [your-github]

LinkedIn: [your-linkedin]

🙏 Acknowledgments
Django Documentation

FontAwesome for icons

Google Fonts for typography

📧 Contact
For questions or collaborations, reach out through the contact form on the website or email directly.

Happy Coding! 🎉

text

## requirements.txt

Also create a `requirements.txt` file:

```txt
Django==6.0.2
Pillow==11.2.1
python-dotenv==1.0.1
gunicorn==21.2.0
whitenoise==6.7.0