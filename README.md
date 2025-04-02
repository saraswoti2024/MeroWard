# MeroWard

MeroWard is an e-governance project aimed at enhancing local government services through a digital platform.

---

## Features

- **Citizen Services**: Provides residents with access to various municipal services online.
- **Information Dissemination**: Shares important announcements, news, and updates from the local government.
- **complaints**: citizen can post complaints and other citizens can interact
- **Events**: all the events in the municipality will be posted and people can join
- **Feedback Mechanism**: Allows citizens to submit feedback and suggestions to local authorities.

---

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript

---

## Installation

To set up the project locally:


```bash
git clone https://github.com/saraswoti2024/MeroWard.git
cd MeroWard
python -m venv env
source env/bin/activate  # On Windows, use 'env\Scripts\activate'
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

The portfolio will be accessible at http://127.0.0.1:8000/.
