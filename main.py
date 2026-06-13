"""
CrosMinX Dev Corp — Main Application
FastAPI Backend powering the CrosMinX Empire automation platform
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="CrosMinX Dev Corp API",
    description="Automation and App Development Platform for the CrosMinX Empire",
    version="1.0.0",
    contact={
        "name": "CrosMinX Dev Corp",
        "email": "info@croshireestates.com",
        "url": "https://croshireestates.com"
    }
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# HEALTH CHECK
# ============================================

@app.get("/")
def root():
    return {
        "status": "online",
        "empire": "CrosMinX Dev Corp",
        "version": "1.0.0",
        "services": [
            "Deal Pipeline Tracker",
            "Client Qualification Portal",
            "ARF Referral Tracking",
            "Velocity Loan Status",
            "Agent Commission Calculator",
            "Property Portfolio Manager"
        ]
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

# ============================================
# DEAL PIPELINE
# ============================================

@app.get("/pipeline")
def get_pipeline():
    return {
        "assets": [
            {
                "id": 1,
                "address": "103 Mercer Mill Rd, Landenberg PA 19350",
                "type": "4-Unit Multi-Family",
                "value": 550000,
                "loan": 412500,
                "ltv": 0.75,
                "status": "Special Review - Velocity",
                "loan_number": "6723351921",
                "dscr": 1.56,
                "rental_income": 4900
            },
            {
                "id": 2,
                "address": "213 Cross Rd, Gilbertsville PA 19525",
                "type": "Corporate HQ + Residence + Rental",
                "value": 855000,
                "loan": 641250,
                "ltv": 0.75,
                "status": "Pending Submission",
                "loan_number": None,
                "dscr": None,
                "rental_income": 3500
            },
            {
                "id": 3,
                "address": "1300 N French St, Wilmington DE",
                "type": "8-Unit Multi-Family",
                "value": 1250000,
                "loan": 937500,
                "ltv": 0.75,
                "status": "Stage 2 - Pending",
                "loan_number": None,
                "dscr": None,
                "rental_income": 10000
            }
        ]
    }

# ============================================
# CORPORATIONS
# ============================================

@app.get("/corporations")
def get_corporations():
    return {
        "entities": [
            {
                "name": "CrosMinX Corp",
                "role": "Solar Crypto Mining - Primary Guarantor",
                "filed": "2025-07-29",
                "state": "Pennsylvania"
            },
            {
                "name": "CrosMinX Trading Corp",
                "role": "Algorithmic Trading",
                "filed": "2025-10-14",
                "state": "Pennsylvania"
            },
            {
                "name": "Crosbies Hot Sauce Corp",
                "role": "Food & Beverage - Active Bank Account",
                "filed": "2025-11-13",
                "state": "Pennsylvania"
            },
            {
                "name": "Croshire Estates Corp",
                "role": "Property Management - Primary Borrower",
                "filed": "2025-11-30",
                "state": "Pennsylvania"
            }
        ]
    }

# ============================================
# REVENUE MODEL
# ============================================

@app.get("/revenue")
def get_revenue_model():
    return {
        "target_monthly": 200000,
        "current_monthly": 0,
        "sources": [
            {
                "source": "ARF Referral Commissions",
                "rate": "8% per funded deal",
                "target": "8,000 - 4,000/month"
            },
            {
                "source": "Velocity Broker Commissions",
                "rate": "1-2% per closed loan",
                "target": ",000 - 5,000/month"
            },
            {
                "source": "Croshire Consulting Intake",
                "rate": ",950 per client",
                "target": ",850 - 1,700/month"
            },
            {
                "source": "CrosMinX Dev Corp Services",
                "rate": "Custom pricing",
                "target": "TBD"
            }
        ],
        "agent_expansion": {
            "phase_1": {"agents": 2, "monthly": 40000, "timeline": "Month 1-2"},
            "phase_2": {"agents": 5, "monthly": 100000, "timeline": "Month 3-4"},
            "phase_3": {"agents": 10, "monthly": 200000, "timeline": "Month 5-6"},
            "scale": {"agents": 20, "monthly": 400000, "timeline": "Month 9-12"}
        }
    }

# ============================================
# RUN
# ============================================

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
