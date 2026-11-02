# HireAI – AI-Powered Job & Candidate Management System

HireAI is a full-stack recruitment platform designed to simplify the hiring process by connecting job seekers and recruiters. It enables candidates to discover job opportunities, apply for positions, upload resumes, and track applications, while recruiters can manage job postings, review applicants, and evaluate resume relevance using AI-based text similarity.

## Features

### Candidate Features
- User registration and login.
- Browse and search available job opportunities.
- View job descriptions, required skills, location, and salary details.
- Apply for jobs with a cover letter.
- Upload PDF resumes.
- Track application status.
- View resume-to-job similarity scores when available.

### Recruiter Features
- Recruiter authentication.
- Create and manage job postings.
- View applicants for posted jobs.
- Review candidate applications.
- Rank applicants using available resume similarity scores.
- Update application statuses, including Reviewing, Shortlisted, Rejected, and Hired.

### AI-Powered Resume Matching
- Extract text from uploaded PDF resumes using PyPDF.
- Process resume and job-description text using TF-IDF.
- Calculate text similarity using Cosine Similarity.
- Identify matching keywords between candidate resumes and job requirements.
- Generate a numerical resume-to-job similarity score.

**Note:** The similarity score measures textual relevance. It is not a prediction of hiring success or candidate suitability.

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | Next.js, React.js, JavaScript |
| Styling | Tailwind CSS |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Password Hashing | Argon2 |
| Machine Learning | Scikit-learn |
| Text Processing | TF-IDF |
| Similarity Algorithm | Cosine Similarity |
| PDF Processing | PyPDF |
| API Documentation | Swagger UI |
| Version Control | Git, GitHub |

## System Architecture

```text
             CANDIDATE / RECRUITER
                       |
                       v
             NEXT.JS FRONTEND
          React + JavaScript + Tailwind
                       |
                       v
                FASTAPI BACKEND
                 REST APIs
                       |
           +-----------+-----------+
           |           |           |
           v           v           v
      AUTHENTICATION  JOBS     APPLICATIONS
        JWT/Argon2      |           |
           |           |           |
           +-----------+-----------+
                       |
                       v
                POSTGRESQL DB
                       |
                       v
               RESUME PROCESSING
                     PyPDF
                       |
                       v
                 TF-IDF VECTORS
                       |
                       v
              COSINE SIMILARITY
                       |
                       v
              RESUME MATCH SCORE
```

## Project Structure

```text
HireAI/
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── login/
│   │   │   ├── register/
│   │   │   ├── jobs/
│   │   │   ├── candidate/
│   │   │   │   ├── dashboard/
│   │   │   │   └── applications/
│   │   │   ├── recruiter/
│   │   │   │   └── dashboard/
│   │   │   ├── layout.js
│   │   │   └── page.js
│   │   ├── components/
│   │   └── lib/
│   │       └── api.js
│   ├── public/
│   ├── .env.local
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── jobs.py
│   │   │   ├── applications.py
│   │   │   ├── resumes.py
│   │   │   └── matching.py
│   │   ├── services/
│   │   │   ├── resume_parser.py
│   │   │   └── resume_matcher.py
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
│   ├── uploads/
│   │   └── resumes/
│   ├── .env
│   └── requirements.txt
│
└── README.md
```

*The structure above is illustrative. Adjust filenames and folders to match the actual repository.*

## Prerequisites

Install the following before running the project:

- Python 3.10 or compatible version supported by your dependencies.
- Node.js and npm.
- PostgreSQL.
- Git.
- Visual Studio Code (recommended).

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sani483/HireAI.git
cd HireAI
```

### 2. Backend setup

Navigate to the backend directory:

```powershell
cd backend
```

Create a virtual environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

### 3. Configure backend environment variables

Create a `.env` file inside the backend directory.

Example configuration:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5433/hireai
SECRET_KEY=YOUR_SECURE_SECRET_KEY
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace the placeholder values with your actual local configuration. Never commit real secrets to GitHub.

### 4. Database setup

Create a PostgreSQL database named:

```sql
CREATE DATABASE hireai;
```

Ensure that the database connection settings match your backend environment configuration.

Create the required tables using the project's existing database initialization or migration mechanism.

### 5. Run the backend

From the backend directory:

```powershell
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Frontend setup

Open a separate terminal and navigate to the frontend:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Create or update `.env.local`:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

Start the frontend development server:

```powershell
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

Keep both frontend and backend development servers running while using the application.

## API Modules

The backend is organized around the following API modules:

| Module | Responsibility |
|---|---|
| Authentication | Registration, login, current-user access |
| Jobs | Create, list, and retrieve job postings |
| Applications | Apply for jobs and manage application statuses |
| Resumes | Upload and process PDF resumes |
| Matching | Calculate resume-to-job similarity scores |

For the actual request methods, paths, and schemas, refer to the interactive Swagger documentation at `/docs`.

## Security Considerations

- JWT-based authentication for protected API operations.
- Argon2 password hashing.
- Role-based authorization for candidate and recruiter operations.
- Application ownership checks.
- Resume upload validation and file-size restrictions.
- Environment variables for sensitive configuration.
- Private handling of uploaded resumes.

Production deployment requires additional security verification, secure resume storage, and appropriate secret management.

## Future Enhancements

- Advanced semantic resume matching using transformer-based language models.
- Improved candidate recommendation system.
- Recruiter and candidate notification system.
- Email notifications for application updates.
- Resume parsing for scanned PDFs using OCR.
- Advanced recruiter analytics and hiring reports.
- Interview scheduling and management.
- Production deployment with cloud infrastructure.

## Development Status

HireAI is under active development.

Core backend functionality and frontend page implementations have been developed. Final integration verification, testing, security review, responsive UI verification, and production deployment remain part of the completion process.

## Author

**Sani Vishwakarma**

GitHub: [Sani483](https://github.com/Sani483)

## License

This project is developed for educational and portfolio purposes. Add an appropriate open-source license if you intend to distribute it publicly.
