from fastapi import FastAPI
from pydantic import BaseModel, Field

class Check(BaseModel):
    name:str=Field(min_length=1,max_length=80)
    latency_ms:float=Field(ge=0,le=60000)
    available:bool

app=FastAPI(title='OpsStatus',version='1.0.0')
@app.get('/health')
def health():return {'status':'ok'}
@app.get('/ready')
def ready():return {'status':'ready'}
@app.post('/v1/summary')
def summary(checks:list[Check]):
    total=len(checks); healthy=sum(c.available for c in checks)
    return {'total':total,'healthy':healthy,'unavailable':total-healthy,'availability_pct':round(100*healthy/total,2) if total else None,'mean_latency_ms':round(sum(c.latency_ms for c in checks)/total,2) if total else None}
