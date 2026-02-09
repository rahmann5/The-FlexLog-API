# FlexLog Workout API 🏋️‍♂️

FlexLog is a high-performance RESTful API built with **FastAPI** designed for athletes and fitness enthusiasts to track their progress. It allows users to log exercises, view their workout history, and instantly identify their Personal Records (PRs).

## 🚀 Key Features
* **Strict Data Validation:** Leverages **Pydantic** models to ensure all logged data (reps, sets, weight) is accurate and type-safe.
* **Dynamic PR Finder:** A dedicated endpoint to scan workout history and retrieve the maximum weight lifted for any specific exercise.
* **Efficient Logic:** Case-insensitive search and robust error handling for missing data.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Validation:** [Pydantic](https://docs.pydantic.dev/)
* **Server:** [Uvicorn](https://www.uvicorn.org/)

## 📥 Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/rahmann5/flexlog-workout-api.git](https://github.com/rahmann5/flexlog-workout-api.git)
cd flexlog-workout-api
```
### 2. Set up a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn
```
### 4. Run the API
```bash
uvicorn main:app --reload
```
The API will be live at `http://127.0.0.1:8000`.

### 🛣️ API Endpoints
| Method | Endpoint | Description |
|----------|----------|----------|
| `GET`  | `/`  | Health check and service status. |
| `POST`  | `/log-exercise`  | Log an exercise (JSON body required).  |
| `POST`  | `/log-exercises`  | Log a list of exercises (JSON body required).  |
| `GET`  | `/pr/{name}`  | Retrieve the Personal Record for a specific lift.  |
| `GET`  | `/stats`  | Retrieves the total volume of the recorded exercises |
| `GET`  | `/history`  |Retrieves all logged exercises  |

### 🧪 Example Usage (PR Finder)
To find your best Squats, send a `GET request to: http://127.0.0.1:8000/pr/squats`
#### Response:
```bash
{
  "exercise": "Squat",
  "personal record weight": 15.0,
  "full details": {
    "name": "Squat",
    "sets": 7,
    "reps": 5,
    "weight": 15.0,
    "comment": "Daily exercise streak"
  }
}
```


