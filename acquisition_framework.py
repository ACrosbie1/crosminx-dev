# CrosMinX Dev Corp — Acquisition Framework
# Standard Zero Out of Pocket Property Acquisition Structure
# Applied to every Croshire Estates Corp deal

ACQUISITION_FRAMEWORK = {
    "name": "Croshire Estates Corp Standard Acquisition Structure",
    "version": "1.0",
    "description": "Zero Out of Pocket Framework - Use property equity to fund acquisition",
    
    "steps": [
        {
            "step": 1,
            "title": "Negotiate Purchase Price Below Market",
            "target": "10-15% below asking price",
            "why": "Lower purchase price creates larger equity gap"
        },
        {
            "step": 2,
            "title": "Force Appraisal Above Purchase Price",
            "target": "Market value above negotiated price",
            "why": "Gap between purchase and appraised value is working capital"
        },
        {
            "step": 3,
            "title": "Loan Based on Appraised Value Not Purchase Price",
            "target": "75% LTV of appraised value",
            "why": "Larger loan covers more costs at closing"
        },
        {
            "step": 4,
            "title": "Negotiate Seller Concessions",
            "target": "3-6% seller credits",
            "why": "Covers appraisal, points, inspection, title, closing costs"
        },
        {
            "step": 5,
            "title": "Roll Everything Into Closing",
            "target": "All costs financed",
            "why": "Zero out of pocket at closing"
        },
        {
            "step": 6,
            "title": "Inter-Corporate Bridge for Gap",
            "target": "Sister corporation advances remaining gap",
            "why": "No personal capital ever touches the deal"
        },
        {
            "step": 7,
            "title": "Rental Income Services Debt",
            "target": "DSCR minimum 1.20",
            "why": "Property pays for itself"
        },
        {
            "step": 8,
            "title": "Equity Builds - Repeat",
            "target": "Refinance to fund next acquisition",
            "why": "Each deal funds the next one"
        }
    ],
    
    "questions_for_lender": [
        "Can we base LTV on appraised value rather than purchase price?",
        "Can appraisal fee be rolled into closing costs?",
        "Can points be financed into the loan?",
        "What seller concession percentage do you allow?",
        "Can repair reserve be included in the loan amount?"
    ],
    
    "corporate_identity_rules": {
        "borrower": "Croshire Estates Corp",
        "guarantor": "CrosMinX Corp",
        "bridge_if_needed": "Crosbies Hot Sauce Corp",
        "no_personal_name": True,
        "no_personal_capital": True,
        "correspondence_email": "info@croshireestates.com",
        "phone": "+1 (215) 436-8268"
    },
    
    "velocity_reference": {
        "email_subject_format": "{loan_number} | CROSHIRE",
        "ae": "John Neufer",
        "ae_email": "jneufer@velocitymortgage.com",
        "ae_phone": "253-719-9385",
        "product": "FlexTerm",
        "max_ltv": 0.75,
        "min_dscr": 1.20,
        "timeline": "30-40 days to fund"
    }
}
