from fastapi import APIRouter

router = APIRouter()

MODULES = [
    {"id": 1, "title": "What is the Uganda Securities Exchange?", "level": "beginner",
     "description": "An introduction to Uganda's stock market, how it works, and why it matters."},
    {"id": 2, "title": "Understanding Stocks and Shares", "level": "beginner",
     "description": "Learn what shares are, how they're bought and sold, and what owning a share means."},
    {"id": 3, "title": "What is a Dividend?", "level": "beginner",
     "description": "Understand how companies pay investors from their profits."},
    {"id": 4, "title": "Reading a Company's Financial Statement", "level": "intermediate",
     "description": "Learn to interpret balance sheets, income statements, and cash flow reports."},
    {"id": 5, "title": "Portfolio Diversification and Risk", "level": "intermediate",
     "description": "Why spreading investments across sectors reduces risk."},
    {"id": 6, "title": "Bonds and Fixed Income", "level": "advanced",
     "description": "Understand government and corporate bonds as an investment class."},
]

@router.get("/modules")
def get_modules():
    return MODULES

@router.get("/modules/{module_id}")
def get_module(module_id: int):
    return next((m for m in MODULES if m["id"] == module_id), None)
