from fastapi import FastAPI

app = FastAPI(title="ERP Industrial")

projects = []

@app.get("/")
def root():
    return {"status": "ERP Industrial ativo"}

@app.post("/projects")
def create_project(name: str):
    project = {"id": len(projects) + 1, "name": name}
    projects.append(project)
    return project

@app.get("/projects")
def list_projects():
    return projects

