from fastapi import Depends, FastAPI, HTTPException, Header

app=FastAPI()

def verify_user(secrect_pass=Header(..., description="Secrect password to access")):
    if secrect_pass != "mysecrectkey":
        raise HTTPException(status_code=403, detail="Forbidden: Invalid secrect key")
    return "welcome back brother"

@app.get("/security")
def security(passw: str = Depends(verify_user)):
    return {"granted":passw}