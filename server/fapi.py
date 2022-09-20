from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from starlette.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

zaseki_dic = [ { "seatNumber":"A1", "status": True },{ "seatNumber":"A2", "status": True },{ "seatNumber":"A3", "status": True },{ "seatNumber":"A4", "status": True },{ "seatNumber":"A5", "status": True },{ "seatNumber":"A6", "status": True }]

df = pd.DataFrame(data={"studentID": ["010101", "020202", "030303", "040404"],"name": ["英子","美井子","椎子","日男"], "seatID": ["", "", "", ""]})

@app.get("/")
def hello(name: str=""):
    return {"message": "hello "+name}

@app.get("/kuuseki")
async def root():
    return zaseki_dic

@app.get("/syougou")
def idmatch(sID: str=""):
    matched = df[df["studentID"] == sID]
    print(matched)
    if len(matched):
        return {"name": list(matched["name"])[0], "studentID": list(matched["studentID"])[0]}
    else:
        res = JSONResponse(content={"studentID": sID, "message": "不正なカードID"}, status_code=401)
        return res

class LockBody(BaseModel):
    studentID: str
    seatID: str

@app.put("/seatlock")
async def seatlock(lb: LockBody):
    for i,zaseki in enumerate(zaseki_dic):
        if zaseki["seatNumber"] == lb.seatID:
            zaseki_dic[i]["status"] = not zaseki["status"]
            if not zaseki_dic[i]["status"]:
                df.loc[df[df["studentID"] == lb.studentID].index,"seatID"] = lb.seatID
            else:
                df.loc[df[df["studentID"] == lb.studentID].index,"seatID"] = ""
            return {"seatID": lb.seatID, "status": zaseki_dic[i]["status"], "result": "ok"}
    res = JSONResponse(content={"message": "不正な座席番号"}, status_code=401)
    return res

@app.get("/search")
async def search(name: str=""):
    matched = df[df["name"] == name]
    print(matched)
    if len(matched) and not (list(matched["seatID"])[0] == ""):
        return {"name": name, "seatID": list(matched["seatID"])[0]}
    elif len(matched):
        res = JSONResponse(content={"message": "その名前の学生は出席していません"}, status_code=401)
        return res
    else:
        res = JSONResponse(content={"message": "その名前の学生はいません"}, status_code=401)
        return res

@app.get("/syutoku")
async def syutoku(name: str=""):
    matched = df[df["name"] == name]
    if len(matched):
        return {"studentID": list(matched["studentID"])[0], "seatID": list(matched["seatID"])[0]}
    else:
        res = JSONResponse(content={"message": "その学生はいません"}, status_code=401)
        return res

if __name__ == "__main__":
  uvicorn.run("fapi:app", host="0.0.0.0", port=8000, reload=True)
