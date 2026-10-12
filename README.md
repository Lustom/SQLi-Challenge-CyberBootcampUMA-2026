# CTF Challenge: The Intruder (SQL Injection)

## Overview
This repository contains "The Intruder", a custom-designed web vulnerability challenge created for the **Cyber Bootcamp Málaga**. The challenge was engineered to evaluate and train participants in web security, specifically focusing on identifying and exploiting SQL Injection (SQLi) vulnerabilities within a SQLite environment.

As part of the training curriculum, the challenge intentionally avoids requiring blind injection techniques, focusing instead on fundamental set operations (`UNION`-based injections) and database schema reconnaissance.

## Learning Objectives
The challenge was designed to test the following competencies:
* **Vulnerability Identification:** Detecting unescaped input vectors in search queries.
* **Arity Matching:** Understanding and mapping the exact number of columns required for a successful `UNION` operation.
* **Schema Reconnaissance:** Querying internal database dictionaries (specifically `sqlite_master` in SQLite) to extract hidden table structures.
* **Data Exfiltration:** Crafting precise queries to bypass application logic and extract sensitive tokens.

## Repository Structure
* **`challenge.md`:** The original challenge description, metadata, and hints provided to the participants.
* **`writeup.md`:** A comprehensive, step-by-step solution detailing the intended exploitation path and payloads.
* **`src/`**: Source code and configuration required to deploy the vulnerable environment locally.

## Technologies Used
* SQLite (Relational Database)
* Web Application Framework
* CTFd (Validation & Scoring Integration)
