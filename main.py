from fastapi import FastAPI


import api.id_api as id_api
import api.pages_api as pages_api
import api.auth_api as auth_api
import api.reviews_api as reviews_api

app = FastAPI(
    title="Glassdoor Scraper Suite",
    version="0.3.0",
    description="ID → CSRF → pages → reviews",
)


app.include_router(id_api.router, prefix="/glassdoor", tags=["Employer‑ID"])
app.include_router(auth_api.router, prefix="/glassdoor", tags=["Auth"])
app.include_router(pages_api.router, prefix="/glassdoor", tags=["Pages"])
app.include_router(reviews_api.router, prefix="/glassdoor", tags=["Reviews"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
