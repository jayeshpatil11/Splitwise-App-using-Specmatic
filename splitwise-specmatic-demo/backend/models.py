from pydantic import BaseModel
from typing import List

class CreateGroupRequest(BaseModel):
    name: str

class GroupResponse(BaseModel):
    groupId: int
    name: str

class AddExpenseRequest(BaseModel):
    groupId: int
    amount: float
    paidBy: int

class ExpenseResponse(BaseModel):
    expenseId: int
    status: str

class Expense(BaseModel):
    expenseId: int
    groupId: int
    amount: float
    paidBy: int

class BalanceResponse(BaseModel):
    userId: int
    totalOwed: float
    totalReceivable: float

class SettlementRequest(BaseModel):
    payerId: int
    receiverId: int
    amount: float

class SettlementResponse(BaseModel):
    settlementId: int
    status: str