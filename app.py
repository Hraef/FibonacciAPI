from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI()

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@app.get("/fibonacci/{n}")
async def get_fibonacci(n: int) -> Dict[str, int]:
    try:
        result = fibonacci(n)
        return {"n": n, "fibonacci": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)