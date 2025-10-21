from flask import Flask, render_template, request, redirect, url_for
from app.source import Worker, RcpLog, WorkerNotFound


app = Flask(__name__)


@app.get("/")
def input():
    return render_template("scan.html")
    

@app.post("/scan")
async def scan():
    card = request.form.get("code")
    try:
        worker = await Worker.fetch(int(card))
    except (WorkerNotFound, ValueError):
        return render_template("error.html")
    else:
        return render_template("worker.html", worker=worker)

@app.post("/go") 
async def go():
    worker = request.form.get("worker_id")
    await RcpLog.create(worker).write()
    return redirect("/")
