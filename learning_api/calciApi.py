from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator API", version="1.0.0")


class CalculationRequest(BaseModel):
	operation: Literal["add", "subtract", "multiply", "divide"]
	operand1: float
	operand2: float


@app.get("/")
def health_check():
	return {"message": "Calculator API is running"}


@app.post("/calculate")
def calculate(request: CalculationRequest):
	a, b = request.operand1, request.operand2

	if request.operation == "add":
		result = a + b
	elif request.operation == "subtract":
		result = a - b
	elif request.operation == "multiply":
		result = a * b
	else:  # divide
		if b == 0:
			raise HTTPException(status_code=400, detail="Cannot divide by zero")
		result = a / b

	return {"operation": request.operation, "result": result}
