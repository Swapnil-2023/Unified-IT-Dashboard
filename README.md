# Unified IT Dashboard

A centralized Flask-based IT Management Dashboard designed for small organizations and educational environments.
This project combines asset management, task management, vendor management, document handling, monitoring, and authentication into a single web dashboard.

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

## Task System

* Create task
* Task priority management
* Open / Close task workflow
* Delete task

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

| Technology            | Purpose                   |
| --------------------- | ----------------------    |
| Python                | Backend programming       |
| Flask                 | Web framework             |
| SQLite                | Database                  |
| HTML/CSS/JavaScript   | Frontend                  |
| Flask-SQLAlchemy      | ORM                       |
| Flask-Session         | Session management        |
| Python random module  | simulated monitoring data |
| Git & GitHub          | Version control           |
| Cloudflare Tunnel     | Secure remote access      |
| Raspberry Pi Zero 2 W | Self-hosted deployment    |

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

# Raspberry Pi Production Deployment

The application was successfully deployed on a Raspberry Pi Zero 2 W using:

* GitHub repository cloning
* Python virtual environment
* Flask production hosting
* Cloudflare Tunnel secure remote access
* Linux `systemd` service management

---

## Deployment Workflow

### 1. Clone Repository

```bash
git clone https://github.com/Swapnil-2023/Unified-IT-Dashboard.git
```

### 2. Create Runtime Directories

```bash
mkdir database
mkdir uploads
mkdir flask_session
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Initialize Database

```bash
python init_db.py
```

### 6. Production Flask Configuration

The Flask application was configured for network accessibility using:

```python
app.run(host='0.0.0.0', port=5000)
```

This allows access through:

* local network
* Raspberry Pi hosting
* Cloudflare Tunnel routing

---

## Cloudflare Tunnel Integration

Cloudflare Tunnel was used to securely expose the Flask dashboard to the internet without port forwarding.

Architecture:

```text
Public Domain
      ↓
Cloudflare Tunnel
      ↓
127.0.0.1:5000
      ↓
Flask Dashboard on Raspberry Pi
```

Benefits:

* Secure HTTPS access
* No router port forwarding required
* Public access through custom domain
* Additional Cloudflare security protection

---

## Linux systemd Service Setup

The dashboard was configured as a Linux background service using `systemd`.

Benefits:

* Automatic startup after reboot
* Runs without active terminal
* Production-style deployment
* Service auto-recovery support

Example service:

```ini
[Unit]
Description=Unified IT Dashboard
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/Unified-IT-Dashboard
ExecStart=/home/pi/Unified-IT-Dashboard/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## Version Control & GitHub

The project uses Git and GitHub for:

* Source code management
* Deployment workflow
* Backup and recovery
* Version tracking
* Production deployment through Git clone

GitHub Repository:

[https://github.com/Swapnil-2023/Unified-IT-Dashboard](https://github.com/Swapnil-2023/Unified-IT-Dashboard)

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
