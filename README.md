#  Distributed Room Reservation System

This project implements a distributed meeting room reservation system using a **MongoDB Replica Set** and a **Flask-based web application**.

##  Overview

The main objectives of the project are:

- To build a **MongoDB Replica Set** environment across two Ubuntu-based virtual machines with one **Primary**, one **Secondary**, and one **Arbiter** node.
- To implement a **web-based room reservation system** that interacts directly with the Primary node using Flask.
- To test **automatic failover and leader election** when the Primary node fails.
- To ensure data is **replicated in real-time** between nodes, and all user actions (reservation creation, viewing, etc.) are reflected in the distributed database.

##  Technologies Used

- **MongoDB 6.0.24** (Replica Set: Primary + Secondary + Arbiter)
- **Flask** web framework with **PyMongo** for DB interaction
- **Python 3.12.3**
- **Ubuntu 24.04.2 (via VMware Workstation Pro)**

##  Key Features

- **Real-time replication** between MongoDB nodes
- **Automatic leader re-election** using Arbiter voting when Primary fails
- **User, Room, and Reservation** data management via a web interface
- **Failover testing**, including recovery and synchronization after node reboot

##  Web Interface

| Route         | Description                              |
|---------------|------------------------------------------|
| `/users`      | View list of users                       |
| `/rooms`      | View list of meeting rooms               |
| `/reservations` | View all reservations                   |
| `/reserve`    | Create a new room reservation            |

##  Database Design

- `users` collection: Stores user information (name, email, role)
- `rooms` collection: Stores room details (location, capacity, projector, etc.)
- `reservations` collection: Links users to rooms with timestamps and status

##  Requirements Implemented

- RQ-1: Replica Set configuration across two machines + Arbiter
- RQ-2: MongoDB schema and test data population
- RQ-3: Input of 5 users and 10 rooms
- RQ-4: Real-time replication verification
- RQ-5: Failover test (leader down → secondary promoted)
- RQ-6: Web-based reservation interface using Flask

---

