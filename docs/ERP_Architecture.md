# AcadFlow ERP Architecture

**Version:** 0.1.0 (MVP)

**Status:** Draft

**Author:** Kiran Kumar A

**Project:** AcadFlow – Academy Management ERP

**Last Updated:** July 2026

---

# 1. Overview

AcadFlow is a cloud-based ERP (Enterprise Resource Planning) platform designed to simplify and automate the day-to-day operations of training academies.

The system is intended for martial arts academies, dance schools, music institutes, sports academies, coaching centers, and similar educational organizations.

The primary objective of AcadFlow is to reduce manual work, centralize data management, improve operational efficiency, and provide a scalable platform capable of supporting multiple academies under a single SaaS application.

---

# 2. Architecture Philosophy

AcadFlow is designed using a modular architecture.

Each module is responsible for managing a specific business domain.

Modules communicate with each other through well-defined relationships while maintaining loose coupling to ensure scalability and future expansion.

The architecture follows these principles:

- Single Responsibility Principle
- Separation of Business Domains
- Modular Development
- Scalability
- Multi-Academy Support
- Future Ready

---

# 3. High-Level Architecture

```

AcadFlow Platform
│
├── Super User
│
└── Academy
│
├── Academy Owner
│
├── Branch
│ │
│ ├── Users
│ │ ├── Branch Admin
│ │ ├── Head Coach
│ │ ├── Coach
│ │ ├── Receptionist
│ │ └── Accountant (Future)
│ │
│ ├── Enrollments
│ │
│ ├── Students
│ │
│ ├── Programs
│ │
│ ├── Events
│ │
│ ├── Accounts
│ │
│ ├── Attendance
│ │
│ ├── Certificates
│ │
│ └── Reports


AcadFlow ERP Architecture v1.0

                                    ┌──────────────────────┐
                                    │     AcadFlow ERP     │
                                    │   (SaaS Platform)    │
                                    └──────────┬───────────┘
                                               │
                                  ┌────────────▼────────────┐
                                  │      Super User         │
                                  │ (Platform Administrator)│
                                  └────────────┬────────────┘
                                               │
                         ┌─────────────────────▼─────────────────────┐
                         │               Academy                      │
                         └─────────────────┬──────────────────────────┘
                                           │
                      ┌────────────────────┴────────────────────┐
                      │                                         │
              Academy Owner                              Academy Settings
                      │                           (Logo, Certificate Template,
                      │                           Fee Rules, Notifications...)
                      │
         ┌────────────┴────────────┐
         │                         │
     Branch 1                  Branch 2
         │                         │
         └──────────────┬──────────┘
                        │
                  Branch Database
                        │
 ┌──────────────────────┼──────────────────────────────┐
 │                      │                              │
 ▼                      ▼                              ▼
Users                Programs                     Events
 │                      │                              │
 │                      │                              │
 │                  Enrollments                 Tournament
 │                      │                       Belt Exam
 │                      │                       Workshop
 │                      │
 │                      ▼
 │                  Students
 │
 │
 ├── Branch Admin
 ├── Head Coach
 ├── Coach
 ├── Receptionist
 ├── Accountant (Future)
 └── Parent (Portal)

                        │
                        ▼
               Supporting Modules
 ┌──────────────────────────────────────────────────────────┐
 │                                                          │
 │ Attendance                                                │
 │ Accounts                                                  │
 │ Certificates                                              │
 │ Notifications                                              │
 │ Reports                                                   │
 │ Progress Reports                                          │
 │ Fee Collection                                            │
 └──────────────────────────────────────────────────────────┘

 4. Core Entities
4.1 AcadFlow Platform

Represents the SaaS application.

Responsibilities:

Manage multiple academies
Subscription management (Future)
Platform configuration
Global monitoring
Platform updates

Accessible only by the Super User.

4.2 Academy

Represents a customer organization using AcadFlow.

Responsibilities:

Academy profile
Branding
Certificate templates
Global academy settings
Branch management

Each academy is isolated from every other academy.

4.3 Branch

Represents a physical academy location.

Responsibilities:

Students
Programs
Coaches
Events
Fee collection
Attendance
Certificates

Each branch operates independently while remaining under its academy.

4.4 Users

Represents all authenticated users of the system.

Roles include:

Academy Owner
Branch Administrator
Head Coach
Coach
Receptionist
Parent / Student Portal
Accountant (Future)

Each role has different permissions.

4.5 Programs

Programs represent services offered by the academy.

Examples:

Taekwondo
Dance
Music
Chess
Silambam
Yoga

Programs exist independently of students.

4.6 Students

Represents individual students.

The Student entity stores only personal information.

Examples:

Student ID
Name
Contact Details
Guardian Information
Academy Information

The Student entity intentionally DOES NOT store:

Belt Information
Attendance
Fee History
Event History
Certificates

Those belong to their respective modules.

4.7 Enrollments

Enrollment is the core business entity of AcadFlow.

It represents a student's participation in a program.

Enrollment connects:

Student ←→ Program

while also maintaining:

Branch
Coach
Fee Plan
Batch
Joining Date
Status

Activity-specific data is stored here.

Example:

Taekwondo Enrollment

Current Belt
Belt History
Next Belt Exam

Dance Enrollment

Level
Performance Group

This design allows a student to join multiple programs without duplicating student information.

4.8 Events

Represents academy events.

Examples:

Belt Examination
Tournament
Workshop
Demonstration
Camp

Each event maintains:

Participants
Fees
Accounts
Certificates
Results
Status

Events also support external participants from schools or other academies.

4.9 Accounts

Responsible for financial records.

Includes:

Admission Fees
Monthly Fees
Event Accounts
Receipts
Payment History

4.10 Attendance

Responsible for attendance management.

Version 1

Manual Attendance

Future Versions

QR Attendance
RFID
Fingerprint
Face Recognition

4.11 Certificates

Responsible for automatic certificate generation.

Supports:

Belt Certificates
Tournament Certificates
Participation Certificates

Certificates are generated using predefined templates.

4.12 Reports

Provides analytical information.

Examples:

Student Reports
Fee Reports
Attendance Reports
Coach Performance
Event Statistics

5. User Hierarchy

Super User

↓

Academy Owner

↓

Branch Administrator

↓

Head Coach

↓

Coach

↓

Receptionist

↓

Parent / Student


Each role receives only the permissions required to perform its responsibilities.

6. Architecture Decisions

ADR-001:

"A student record is created only once."

Reason:

Students may join multiple programs without duplicating personal information.

Status:

Accepted

ADR-002:

"Programs exist independently of students."

Reason:

Students enroll into programs.

Programs are not created because students join.

Status:

Accepted

ADR-003:

"Enrollment is the central business entity."

Reason:

Enrollment connects students, programs, coaches, branches, fees, attendance, and progress while preserving historical records.

Status:

Accepted

ADR-004:

"Program-specific information is stored inside Enrollment."

Examples:

Taekwondo

Belt
Belt History

Dance

Level

Music

Instrument

Status:

Accepted

ADR-005:

"The system supports multiple academies."

Each academy is isolated from all other academies.

Status:

Accepted

7. Development Roadmap

Phase 1:

Academy
Branch
Users
Programs
Students
Enrollments

Phase 2:

Fee Management
Attendance
Progress Tracking

Phase 3:

Events
Certificates
Accounts

Phase 4:

Reports
Notifications
Parent Portal

Phase 5:

Mobile Application
AI Features
Biometric Integration
Analytics Dashboard

8. Future Scope

Future versions of AcadFlow may include:

AI-powered student performance analysis
WhatsApp notifications
Online fee payment
Parent mobile application
Multi-language support
Online admission
Digital ID cards
QR Code attendance
Fingerprint attendance
Face Recognition
Cloud backup
Multi-country deployment

9. Conclusion

AcadFlow is designed as a scalable, modular, and extensible ERP platform capable of managing multiple academies from a single SaaS application.

The architecture emphasizes maintainability, flexibility, and business-driven design by separating responsibilities into dedicated modules while ensuring minimal data duplication.

This document serves as the foundation for database design, backend development, and future product expansion.


---

## ⭐
                Student
                   │
                   │
                   ▼
             Enrollment
             /    |    \
            /     |     \
           ▼      ▼      ▼
      Program   Branch  Coach
```

This diagram tells the real story:

- A **Student** enrolls.
- The **Enrollment** belongs to a **Program**.
- It happens at a **Branch**.
- It is assigned to a **Coach**.

This one diagram is so important that I think it should become the **official architecture diagram of AcadFlow**. It captures the core business process more accurately than a simple hierarchy, and we'll refer back to it when we design the database and Django models.

⭐Organizational Hierarchy:

AcadFlow Platform
│
├── Super User
│
└── Academy
    │
    ├── Academy Owner
    │
    └── Branch
          │
          ├── Branch Admin
          ├── Head Coach
          ├── Coach
          ├── Receptionist
          └── Accountant
          
⭐Business Module Relationships:

                    Student
                       │
                       │
                       ▼
                 Enrollment
                /     |      \
               /      |       \
              ▼       ▼        ▼
         Program    Branch    Coach
              │
              ▼
        Attendance
              │
              ▼
        Progress Report
              │
              ▼
         Belt Progress*
              │
              ▼
         Certificates
              │
              ▼
            Events
              │
              ▼
           Accounts
