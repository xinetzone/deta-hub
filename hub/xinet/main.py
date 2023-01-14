from fastapi import FastAPI, Request


app = FastAPI()

@app.get("/")
async def root():    
    return {"message": "Hello World"}

# a POST route for our webhook events
@app.post("/")
def webhook_handler(req: Request):
    # verify signature if needed
    # add logic to handle the request
    return "ok"
