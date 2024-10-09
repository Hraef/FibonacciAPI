from fastapi import FastAPI, HTTPException
from typing import Dict

# Create instance of FastAPI class
app = FastAPI()

# Function to calculate the Nth Fibonacci number 
def fibonacci(n: int) -> int:
    # checks if number is a negative number and sends an error
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Return n if it is 0 or 1, as these are the base cases in the Fibonacci sequence
    elif n <= 1:
        return n
    else:
        # Iterates to calulate the Fibonacci number when n > 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            # Updates values. Here this is where the Fibonacci number is the sum of the previous 2
            a, b = b, a + b 
        return b

# GET endpoint for the Fibonacci API. This takes a integer (n) as a paramater
@app.get("/fibonacci/{n}")
async def get_fibonacci(n: int) -> Dict[str, int]:
    # Calls the fibonacci function with the provided number (n) and returns the result. If there is an input error the catch will send an error message
    try:
        result = fibonacci(n)
        return {"n": n, "fibonacci": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Runs the FastAPI using Uvicorn with a set host and port number.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)