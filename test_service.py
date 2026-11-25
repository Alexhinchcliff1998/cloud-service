from fastapi.testclient import TestClient
from service import app
c=TestClient(app)
def test_health():assert c.get('/health').json()=={'status':'ok'}
def test_summary():
    r=c.post('/v1/summary',json=[{'name':'api','available':True,'latency_ms':10},{'name':'db','available':False,'latency_ms':30}]);assert r.json()['availability_pct']==50;assert r.json()['mean_latency_ms']==20
def test_empty_and_invalid():
    assert c.post('/v1/summary',json=[]).json()['availability_pct'] is None
    assert c.post('/v1/summary',json=[{'name':'api','available':True,'latency_ms':-1}]).status_code==422
