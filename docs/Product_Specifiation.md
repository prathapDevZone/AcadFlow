# AcadFlow ERP Architecture

## Version
0.1 (Draft)

## Purpose

This document defines the high-level architecture of AcadFlow ERP.

The architecture is designed to be scalable, modular, and support multiple academies, branches, users, and Programs.

The purpose is to avoid major redesign as the software grows.

---

# Core Architecture

Academy
    ↓
Branch
    ↓
Users
    ↓
Students
    ↓
Enrollments
    ↓
Programs
    ↓
Events

---

# Architecture Principles

- One software can support multiple academies.
- One academy can have multiple branches.
- Every branch contains its own users.
- Students belong to an academy through a branch.
- One student can enroll in multiple Programs.
- Every activity manages its own progress and records.
- Events are independent modules shared across Programs.

---

# Core Modules

1. Academy
2. Branch
3. Users
4. Students
5. Enrollments
6. Program
7. Events
8. Certificates
9. Accounts
10. Notifications
11. Attendance

# Architecture Decisions

## ADR-001

Student information is stored only once.

Reason:

A student may join multiple Program without duplicating personal information.

Status:
Accepted

---

## ADR-002

Program-specific information is NOT stored inside Student.

Reason:

Different programs have different requirements.

Example:

Taekwondo → Belt

Dance → Level

Music → Instrument

Status:
Accepted

---

## ADR-003

The software is designed as a multi-academy ERP.

Reason:

Future customers may include dance, music, martial arts and sports academies.

Status:
Accepted

---

## ADR-004

Architecture hierarchy

Academy

↓

Branch

↓

Users

↓

Students

↓

Enrollments

↓

Programs

↓

Events

Status:
Accepted

# Development Order

Phase 1

- Academy
- Branch
- Users
- Students

Phase 2

- Programs
- Enrollments
- Fees

Phase 3

- Events
- Certificates
- Accounts

Phase 4

- Attendance
- Notifications
- Reports