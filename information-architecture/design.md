# Building Strong Units

## Website Design Document

**Project Status:** Draft 2
**Last Updated:** July 7, 2026

---

# Purpose

Building Strong Units is a resource website developed for volunteers in the Kettle Country district. The site provides practical guidance, downloadable resources, and connections to local Scouting units.

The website is designed to support leaders through structured learning rather than simply presenting a collection of documents.

---

# Design Principles

The site should be:

* Simple to navigate
* Mobile friendly
* Easy to maintain
* Consistent across pages
* Focused on helping volunteers succeed

Every page should have a clear purpose.

---

# Information Architecture

```text
Home
│
├── Guides
│   │
│   ├── Building on What Works
│   │   │
│   │   ├── Overview (index.html)
│   │   ├── Session 1
│   │   ├── Session 2
│   │   ├── Session 3
│   │   └── Additional Sessions
│   │
│   └── Future Guide
│
├── Resources
│   │
│   ├── Resource Category
│   │   │
│   │   ├── Resource
│   │   ├── Resource
│   │   └── Resource
│   │
│   └── Additional Categories
│
├── Units
│   │
│   ├── Packs
│   ├── Troops
│   ├── Crews
│   └── Ships
│
└── About
```

---

# Purpose of Each Major Section

## Home

Introduces Building Strong Units and directs visitors to the major sections of the site.

---

## Guides

Guides provide structured learning experiences.

Each guide consists of:

* Overview page
* One or more learning sessions
* Links to supporting resources

Guides teach concepts.

---

## Resources

Resources form the site's reference library.

Resources are organized by category.

Each resource has its own page containing:

* Description
* Purpose
* When to use it
* Download links
* Related guides or sessions

Resources support learning.

---

## Units

Units is a directory of Scouting units within the Kettle Country district.

Units are organized by program type:

* Packs
* Troops
* Crews
* Ships

Each category contains a list of units with links to the unit's public website or Facebook page.

Units help visitors connect with local Scouting organizations.

---

## About

Explains the purpose of the website, its intended audience, and the organization responsible for maintaining it.

---

# Navigation Model

The website uses multiple navigation systems because visitors have different navigation needs at different levels.

---

## Global Navigation

Global navigation appears on every public page.

Purpose:

Provide access to the major sections of the website.

Primary navigation:

* Home
* Guides
* Resources
* Units
* About

The current section should be visually highlighted.

The site title/logo should return visitors to the Home page.

---

## Breadcrumb Navigation

Breadcrumbs show a visitor's location within the site hierarchy.

Examples:

Guide overview:

```
Home > Guides > Building on What Works
```

Session page:

```
Home > Guides > Building on What Works > Session 3
```

Resource page:

```
Home > Resources > Calendar Templates > Annual Calendar
```

Breadcrumbs support navigation but do not replace the main navigation.

---

## Local Navigation

Local navigation is used within major content areas.

Different sections may use different local navigation styles based on their purpose.

This is intentional.

---

### Guides Local Navigation

Guides that contain multiple sessions use side navigation.

Example:

```
Building on What Works

Overview

Session 1
Session 2
Session 3
Session 4
...
Session 9
```

The side navigation:

* identifies the visitor's location
* provides access to all sessions
* supports a course-like learning experience

On mobile devices, the side navigation should collapse into an accessible menu.

---

### Resources Local Navigation

Resources use category navigation.

Example:

```
Resources

Calendar Templates

Communication Tools

Recruiting Tools
```

Resource categories help visitors browse the library while individual resources remain the primary destination.

---

### Units Local Navigation

Units use program-category navigation.

Example:

```
Units

Packs

Troops

Crews

Ships
```

Each category provides access to a directory of local units.

---

## Sequential Navigation

Sequential navigation is used for learning content such as sessions.

At the bottom of session pages:

```
Previous Session | Guide Home | Next Session
```

This allows visitors to move through a guide without repeatedly returning to the guide overview page.

---

# Responsive Design

The site must provide a usable experience on desktop and mobile devices.

## Desktop

Possible layout:

```
---------------------------------
Site Header and Global Navigation
---------------------------------

Breadcrumbs

---------------------------------

Local Navigation | Content Area

---------------------------------

Footer
---------------------------------
```

---

## Mobile

Navigation should collapse while preserving access.

Example:

```
Site Title

Menu

Breadcrumbs

Page Title

Content

Local Navigation Menu

Footer
```

The goal is to reduce clutter without removing functionality.

---

# Learning Model

The intended learning path is:

```
Home
    ↓
Guides
    ↓
Guide Overview
    ↓
Session
    ↓
Supporting Resource
    ↓
Download
```

Resources may also be browsed independently, but their primary role is to support learning experiences.

---

# Guiding Philosophy

The four primary sections each serve a distinct purpose:

* Guides teach.
* Resources support.
* Units connect.
* About explains.

New content should fit naturally into one of these categories.
