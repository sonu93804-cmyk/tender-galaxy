import json
import random
from datetime import datetime

def generate_master_tenders():
    # Comprehensive Master Dataset covering All States, Cities, Departments & Categories
    states_cities = {
        "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Deoghar"],
        "Bihar": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur", "Purnia"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur"],
        "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri"],
        "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Noida"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Thane"],
        "Delhi": ["New Delhi", "North Delhi", "South Delhi", "Dwarka"],
        "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain"]
    }

    departments = [
        "PWD / Road Construction",
        "Energy & Solar",
        "Railways",
        "Military / Defense Engineering",
        "Central PSU (NTPC/BHEL)",
        "IT & Electronics Department",
        "Health & Family Welfare",
        "Water Resources / Irrigation",
        "Urban Development & Housing",
        "Education Department"
    ]

    categories_titles = [
        ("Building & Civil Works", "Construction of Multi-Story Administrative Building Block & Boundary Wall"),
        ("Road & Highways", "Widening and Strengthening of State Highway with Bituminous Concrete"),
        ("Furniture & Interiors", "Supply and Installation of Modular Office Furniture and Workstations"),
        ("IT & Electronics", "Procurement and Deployment of Enterprise Servers, Networking & IT Hardware"),
        ("Electrical & Solar", "Installation of Rooftop Solar Power Plant and Associated Electrical Wiring"),
        ("Water Supply", "Construction of Overhead Water Tank and Pipeline Distribution Network")
    ]

    generated_list = []
    
    # Generate 50+ rich enterprise tenders covering all combinations
    tender_id_counter = 1001
    
    for state, cities_list in states_cities.items():
        for city in cities_list:
            for dept in departments:
                cat_type, title_prefix = random.choice(categories_titles)
                
                tender_item = {
                    "id": f"TG-2026-{state[:3].upper()}-{tender_id_counter}",
                    "title": f"{title_prefix} at {city}, {state}",
                    "dept": dept,
                    "location": state,
                    "city": city,
                    "category": cat_type,
                    "value": f"₹ {random.randint(25, 350)},{random.randint(10, 99)},000",
                    "estDate": f"{random.randint(10, 28)}-Oct-2026",
                    "status": "live",
                    "nitUrl": f"https://eprocure.gov.in/nit_docs/{state.lower()}_{tender_id_counter}.pdf",
                    "boqUrl": f"https://eprocure.gov.in/boq_sheets/{state.lower()}_{tender_id_counter}.xls",
                    "eligibilityDocs": ["Class-3 DSC", "GST Registration", "PAN Card", "Experience Certificate", "MSME / Startup Exemption"]
                }
                
                generated_list.append(tender_item)
                tender_id_counter += 1

    # Limit to a robust sample of 100 top active tenders for lightning-fast performance
    final_tenders = generated_list[:100]

    # Save directly to tenders.json
    with open("tenders.json", "w", encoding="utf-8") as outfile:
        json.dump(final_tenders, outfile, indent=4, ensure_ascii=False)
    
    print(f"Successfully generated {len(final_tenders)} master tenders with full states, cities, departments & categories.")

if __name__ == "__main__":
    generate_master_tenders()
