# FbDumpFile

`FbDumpFile` is a Python-based open-source tool designed to recursively extract follower data from a specified target Facebook user profile and save it directly into a formatted local text file.

---

## Process Overview

Below is a visual representation of how the tool navigates, fetches GraphQL data, and recursively extracts follower lists:

![FbDumpFile Workflow](watermarked_img_10463910493886622648.jpg)

---

## Features

- **Automated Data Scraping:** Extracts follower names and unique identifiers (UIDs).
- **Recursive Processing:** Optionally traverses downstream followers to collect extended network lists.
- **Custom Output Format:** Exports data cleanly formatted as `UID|Name`.
- **GraphQL Session Handling:** Automates session extraction (`fb_dtsg`, `lsd`, `jazoest`) directly from request responses.

---

## Output Format

Extracted data is appended line-by-line to your target output file using the following structure:

```text
100012345678901|John Doe
100098765432109|Jane Smith
```

---

## Requirements

- **Python 3.x**
- `requests` library

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/FbDumpFile.git
   cd FbDumpFile
   ```

2. **Install Dependencies**
   ```bash
   pip install requests
   ```

---

## Usage

1. **Run the Script**
   ```bash
   python main.py
   ```

2. **Provide the Prompted Details**
   - **Target UID or Username:** The initial profile identifier to scrape.
   - **Facebook Cookie:** A valid standard session cookie from your browser session.
   - **File Name:** Output filename (e.g., `followers.txt`).

> **Note:** Ensure your session cookie remains active during execution. Always adhere to platform terms of service and rate limit practices when working with web APIs.