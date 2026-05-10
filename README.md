# Unified IT Dashboard

A centralized Flask-based IT Management Dashboard designed for small organizations and educational environments.
This project combines asset management, ticketing, vendor management, document handling, monitoring, and authentication into a single web dashboard.

---

# Features

## Dashboard Monitoring

* Live system monitoring
* CPU, RAM, and Disk usage
* Simulated IoT server room monitoring
* KPI cards for quick statistics

## Asset Management

* Add, view, search, and delete IT assets
* Assign assets to users
* Link vendors with assets
* Filter documents by selected asset

## User Management

* Add and manage users
* Role-based user records
* Admin login system
* Session timeout support

## Ticket System

* Create support tickets
* Ticket priority management
* Open / Close ticket workflow
* Delete tickets

## Vendor Management

* Add and manage vendors
* Link vendors to assets and documents

## Document Management

* Upload invoices, quotations, and POs
* Link documents with assets and vendors
* View documents directly in browser
* Search documents
* Delete uploaded files safely

## Authentication & Security

* Admin login system
* Flask session management
* Automatic logout on inactivity
* Runtime file cleanup using `.gitignore`

---

# Technology Stack

| Technology            | Purpose                |
| --------------------- | ---------------------- |
| Python                | Backend programming    |
| Flask                 | Web framework          |
| SQLite                | Database               |
| HTML/CSS/JavaScript   | Frontend               |
| Flask-SQLAlchemy      | ORM                    |
| Flask-Session         | Session management     |
| psutil                | System monitoring      |
| Git & GitHub          | Version control        |
| Cloudflare Tunnel     | Secure remote access   |
| Raspberry Pi Zero 2 W | Self-hosted deployment |

---

# Project Structure

```text
Unified-IT-Dashboard/
│
├── app.py
├── config.py
├── init_db.py
├── requirements.txt
├── README.md
│
├── models/
├── routes/
├── services/
├── templates/
├── static/
│
├── uploads/
├── database/
├── flask_session/
└── venv/
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Swapnil-2023/Unified-IT-Dashboard.git
cd Unified-IT-Dashboard
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Raspberry Pi

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Create Runtime Folders

```bash
mkdir database
mkdir uploads
mkdir flask_session
```

---

## 5. Initialize Database

```bash
python init_db.py
```

This automatically creates:

* Database tables
* Default admin account

### Default Admin Login

| Field    | Value                                                 |
| -------- | ----------------------------------------------------- |
| Email    | [admin@dashboard.local](mailto:admin@dashboard.local) |
| Password | admin123                                              |

---

## 6. Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Deployment

This project is designed for deployment on:

* Raspberry Pi Zero 2 W
* Local servers
* AWS EC2
* Cloudflare Tunnel environments

Recommended deployment:

```text
Cloudflare Tunnel → Raspberry Pi → Flask Dashboard
```

---

# Future Improvements

* Role-based access control
* Real IoT sensor integration
* Email notifications
* Docker deployment
* AWS cloud migration
* Backup automation
* Dark mode UI

---

# Educational Purpose

This project was developed as a BCA Final Year Project to demonstrate:

* Full-stack web development
* CRUD operations
* Database integration
* Authentication systems
* Dashboard UI design
* Self-hosted deployment concepts

---

# Author

Swapnil Deorukhkar

GitHub Repository:
[https://github.com/Swapnil-2023/Unified-IT-Dashboard](https://github.com/Swapnil-2023/Unified-IT-Dashboard)
