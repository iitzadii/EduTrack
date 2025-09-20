# EduTrack — Student Performance Monitoring System

**EduTrack** is a lightweight desktop application built with **CustomTkinter** for managing student records. Teachers can create CSV record files, add student marks via a form, and view/edit records. Students can view records (via file selection). The app is designed as a single-page application (SPA) for the main UI, while some actions (like adding records) open a focused popup window.

---

## Features
- Teacher & Student login screens.
- Teacher can create new CSV record files (pre-populated with headers).
- Teacher can add student records (marks) to a selected CSV file via a popup form.
- View records in a readable table with scrollbars.
- Simple and consistent UI styling using CustomTkinter.

---

### Password (Teacher Login)
The default **teacher password** for testing is: **aditya**

You can **change the password** by editing the source code in the following section:

```python
# ------------------- Page 2: Teacher Password -------------------
```
**Note:** For security, avoid committing real passwords to a public repository. You can also replace the hard-coded password with an environment variable to keep it secure.

---

## Demo / Screenshots
-*Login page*

<img width="493" height="450" alt="image" src="https://github.com/user-attachments/assets/09e024d4-5748-464b-b607-09d91c1a0ec5" />

- *Teacher login*
  
<img width="489" height="465" alt="image" src="https://github.com/user-attachments/assets/978d6bae-e952-42f1-a9b4-95237397ca9e" />

- *Student login*

<img width="494" height="459" alt="image" src="https://github.com/user-attachments/assets/75e2e8b6-8f57-4cf6-8d71-db871720c7e6" />

- *Add records*

<img width="639" height="762" alt="image" src="https://github.com/user-attachments/assets/32adec38-4872-4e0b-a17c-636f644814c3" />

- *OTher ScreenShorts*

<img width="499" height="448" alt="image" src="https://github.com/user-attachments/assets/c2fc1a0d-d572-49ba-b1e8-213b96bd8fda" />
<img width="979" height="522" alt="image" src="https://github.com/user-attachments/assets/4057d14c-041d-4890-ab5d-85e99f271140" />

---

## Requirements
- Python 3.8+  
- `customtkinter`  
- (standard library) `csv`, `os`, `tkinter`, `ttk`

## Install requirements (if needed):
*pip install customtkinter*

