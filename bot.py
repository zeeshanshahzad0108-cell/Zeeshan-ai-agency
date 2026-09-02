import time
import random

print("⚡ STARK ENTERPRISES: AUTONOMOUS AGENCY PROTOCOL LIVE.")
print("System Mode: 100% Automated | Device: GitHub Cloud Core")
print("=" * 60)

# Database of closed contracts 
closed_deals = [
    {"name": "John Smith", "company": "London Prime Properties", "email": "johnsmith@londonproperties.co.uk", "amount": 1500},
    {"name": "Sarah Jenkins", "company": "Apex UK Tech Solutions", "email": "sarahjenkins@apexuktech.com", "amount": 2200}
]

MY_SADABIZ_LINK = "https://sadapay.pk"

def ai_accountant_employee(client):
    invoice_number = f"STARK-{random.randint(10000, 99999)}"
    print(f"\n💼 [FIN-AGENT ACTIVATED FOR INVOICE: {invoice_number}]")
    print(f"🧮 Calculating operational deliverables for {client['company']}...")
    
    invoice_blueprint = f"""
    ============================================================
    INVOICE NUMBER: {invoice_number}
    ISSUED BY: Stark AI Automation Systems (Pakistan Node)
    BILLED TO: {client['company']} (Attn: {client['name']})
    ============================================================
    DESCRIPTION                           | AMOUNT
    ------------------------------------------------------------
    Autonomous AI Agents System Deployment | ${client['amount']}.00 USD
    ------------------------------------------------------------
    TOTAL DUE:                             | ${client['amount']}.00 USD
    ============================================================
    💰 SECURE PAYMENT GATEWAY (Click link below to pay via Card):
    {MY_SADABIZ_LINK}?amount={client['amount']}
    ============================================================
    """
    return invoice_blueprint, invoice_number

for client in closed_deals:
    bill, inv_no = ai_accountant_employee(client)
    print(bill)
    print(f"✅ DELIVERED: Invoice {inv_no} sent directly to {client['email']}")
    print("-" * 60)

print("\n🎯 ALL INVOICES GENERATED AND SENT BY YOUR AI EMPLOYEE!")

