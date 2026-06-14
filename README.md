
# Backup-Verification-Simulator

## 👥 Team Details
* **Team Name:** [Insert Your Team Name Here]

| Name                   | Role                      |
| ---------------------- | ------------------------- |
| Neha Reddy             | Backend & Documentation   |
| Charugundla Santhisree | AI Integration            |
| Dadi Lakshmi Bhavana   | UI Development            |
| Boda Meenakshi         | Database Development      |
---
=======

## Features Implemented
>>>>>>> 8f8e9ae6d3a64d69cdcb2697c043aba3aa99a759

## 🎥 Demo Video Link
👉 **[https://drive.google.com/file/d/1SpUh4oJrUSeFMU1WbGIwB0evZMR9-sS8/view?usp=drivesdk]*(5-7 minute demonstration showcasing happy path execution, sandbox restoration failures, LLM reporting, and live automated GitHub ticketing).*

---

## 📋 Problem Statement
**Business Problem:** Database backups run automatically every night, but nobody checks whether they are actually restorable. If a silent file corruption or schema failure occurs, it goes completely unnoticed until a real data disaster strikes, rendering the backups useless.

**Our Solution:** A **Backup Verification Simulator** that sets up a mock pipeline where an autonomous workflow agent restores a random database backup into an isolated sandbox SQLite environment, runs verification queries (checking row counts and mathematical checksum integrity), uses an LLM to generate an analysis, and automatically files an actionable GitHub Issue if a failure state is caught.

---

## 🛠️ Features Implemented
* **Automated Testing Sandbox:** Dynamically connects to and provisions background SQLite database instances from historical backup files.
* **Data Integrity Checkers:** Automated execution of structural assertions (table checking, missing schema tracking) and mathematical validation aggregates.
* **AI Narrative Summarization:** Integrates an LLM to dynamically turn technical raw database metrics or system error traces into human-readable executive summaries.
* **Autonomous Remediation Loop (Agent System):** Evaluates test outputs and directly orchestrates an external API action by filing GitHub issue tickets completely autonomously on validation failure.
* **Audit Report Exporting:** Features one-click extraction loops allowing administrators to download verification data tables as **CSV** logs or generate clean summary **PDF** reports.

---

<<<<<<< HEAD
## 🏗️ Architecture Overview
=======
1. Clone the repository:
   ```bash
   git clone https://github.com/Santhisree16/backup-verification-simulator.git
   cd backup-verification-simulator
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows (PowerShell/CMD):
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   Create a `.env` file in the root directory (you can use `.env.example` as a reference) and add the following keys:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   GITHUB_TOKEN=your_github_personal_access_token_here
   GITHUB_REPO=yourusername/your-repo-name
   ```
>>>>>>> 8f8e9ae6d3a64d69cdcb2697c043aba3aa99a759

The application implements a linear **Input ➡️ Processing ➡️ AI Layer ➡️ Output** workflow architecture matching corporate prototype guidelines:


```
[ Input Layer ]           [ Processing Layer ]       [ AI Layer ]            [ Output Layer ]
+-------------------+     +--------------------+     +-----------------+     +-----------------------+
|  Select Backup    | --> | Isolated Sandbox   | --> | LLM Analysis    | --> | UI Health Dashboard   |
|  (.db Schema File)|     | Validation Queries |     | & Report Engine |     | CSV / PDF Logs Export |
+-------------------+     +--------------------+     +-----------------+     +-----------------------+
|                                                    |
v (If Failure Detected)                              |
+--------------------+                                         |
| Autonomous Agent   | ----------------------------------------+
| GitHub API Trigger | (Generates Live Issue Link)
+--------------------+
```

* **Input Stage:** Reads historical backup sequences (`.db` format) via an interactive administrative sidebar.
* **Processing Stage:** Mounts targets inside a runtime isolated environment to evaluate structural indices against standard reference models.
* **AI Layer Stage:** Context window prompt evaluation that reasons through execution statuses and structures natural language reporting summaries.
* **Output Stage:** Renders live, responsive metric visual dashboards, files external tracker tickets via webhooks, and exports physical operational reports.

---

## 🧰 Tools and Technologies Used
* **Frontend User Interface:** Streamlit (Python Core Framework)
* **Database Sandbox Environment:** SQLite3
* **AI/LLM Model Integrations:** OpenAI GPT Engine (via structural API client connections)
* **External Service Workflows:** GitHub REST API v3
* **Data Layouts & Visualization:** Pandas, Plotly / Matplotlib
* **System Testing Suite:** Pytest

---

## 🚀 Setup Instructions

### Prerequisites
* Python 3.10 or higher installed on your operating system.
* A GitHub Personal Access Token (PAT) with repository write permissions.
* An active OpenAI API token key credential.

<<<<<<< HEAD
### 1. Clone the Project Repository
```bash
git clone [https://github.com/Nehareddy123-hub/Backup-verification-simulator1.git](https://github.com/Nehareddt123-hub/Backup-verification-simulator1.git)
cd Backup-verification-simulator1

```
### 2. Configure Local Environment Variables
Create a file named .env in the root folder directory of the workspace and input the following configuration properties:
```env
OPENAI_API_KEY="your_openai_api_key_here"
GITHUB_TOKEN="your_github_personal_access_token_here"
GITHUB_REPO="your_github_username/your_repository_name"

```
### 3. Install Required Library Dependencies
```bash
pip install -r requirements.txt

```
## 🏃 Run Instructions
To kickstart the application platform server locally, run the following script execution in your terminal window:
```bash
streamlit run app.py

```
Once launched, open your web browser and navigate to the address: http://localhost:8501
## 🤖 AI Capability Demonstrated
 * **Agent Loop & External Integration Capability:** The application proves hands-on skills in assembling independent agent automations. Rather than simply logging a system failure passively on screen, the core program runs a complete feedback loop: it evaluates raw infrastructure telemetry context ➡️ recognizes a high-severity operational fault ➡️ reasons over the failure using an LLM ➡️ executes a remote network remediation action by auto-filing tracking tickets on the GitHub API platform.
## 📊 Sample Input and Sample Output
### 1. Happy Path Workflow (Successful Backup Restoration)
 * **Sample Input:** User selects backup_healthy.db from the system index dashboard panel.
 * **Sample Output Metrics:**
   * *Validation State:* SUCCESS
   * *Users Found:* 100 rows
   * *Transactions Found:* 500 rows
   * *Integrity Checksum Match:* TRUE
   * *AI Narrative Summary:* "All data checks passed. System records show exact row match verification, confirm structured system layout integrity, and classify the backup target as completely healthy and restorable."
### 2. Anomaly Workflow (Corrupted/Failed Backup Restoration)
 * **Sample Input:** User selects backup_corrupted.db from the system index dashboard panel.
 * **Sample Output Metrics:**
   * *Validation State:* FAILED
   * *Error Captured:* OperationalError: no such table: users
   * *Remediation Step Initiated:* Automated GitHub Rest API call triggered.
   * *AI Narrative Summary:* "CRITICAL INCIDENT ALERT. Database restoration failed due to missing fundamental structural components (users structural reference indices are completely absent). A high-priority tracker issue has been dispatched to engineering."
   * *Generated Live Tracker Ticket:* https://github.com/your_username/your_repository_name/issues/1
## 🧪 Automated Testing Validation
The system includes automated functional unit assertions designed inside **Pytest** to guarantee code framework stability. Run tests with:
```bash
pytest test_app.py -v

```
## 🧠 Assumptions and Limitations
 * **Sandbox Isolation Limits:** The underlying testing sandbox runs calculations in memory or on temporary disk mounts using single-process SQLite file connections. It is not architected for high-concurrency production clustering databases (e.g., live enterprise PostgreSQL clusters).
 * **Data Formatting Specifications:** The automated checking sequence relies on looking for expected entity models (users and transactions metadata fields). If schema developers change system naming conventions without altering the code script, structural anomalies will trigger.
 * **Network Dependency:** The external tracking workflow requires uninterrupted outbound internet access and valid authentication lifecycle updates to ensure smooth real-time messaging with the remote GitHub REST server.
```

```
=======
- **Assumptions**: The system assumes the source database schema is relatively stable and its `sqlite_master` representation fits within the token limits of the LLM. It also assumes the local environment has internet access to reach the Gemini and GitHub APIs.
- **Limitations**: Currently restricted to SQLite databases. Extremely large enterprise databases might take a long time to restore to the local sandbox environment. While the AI's dynamically generated SQL queries are executed in an isolated sandbox database, executing AI-generated SQL always carries theoretical injection risks if the LLM hallucinates destructive commands (though mitigated entirely by the sandboxed file copy architecture).

## Demo Video Link
[Watch Backup Verification Simulator Demo](https://drive.google.com/file/d/1SpUh4oJrUSeFMU1WbGIwB0evZMR9-sS8/view?usp=drivesdk)
>>>>>>> 8f8e9ae6d3a64d69cdcb2697c043aba3aa99a759
>>>>>>>

## Resumes
[Nehareddy](https://drive.google.com/file/d/1X3aZCDc1kjDdoN2Mb6HCdkjKJq6wTOIa/view?usp=drivesdk)
[Meenakshi](https://drive.google.com/file/d/11KQbctSrG4xHzOSWjICCslbWCiDQh1U5/view?usp=drivesdk)
[Laksmi Bhavana](https://drive.google.com/file/d/1RJbs5Sv4KFplErq3mIvAY3mhxKUgW6SI/view?usp=drivesdk)
