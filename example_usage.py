import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import UsageBasedBillingMeteringEngineClient

def main():
    client = UsageBasedBillingMeteringEngineClient()
    res = client.meter_and_calculate_invoice()
    print("=== Usage-Based Billing Metering Engine Output ===")
    print(f"Customer: {res['customer_id']} | Plan: {res['plan_name']}")
    print(f"Usage Events Ingested: {res['total_usage_events_ingested']}")
    print(f"\nLine Items:")
    for li in res["line_items"]:
        print(f"  - {li['metric']:12s} | qty={li['total_quantity']:>12,} | cost=${li['calculated_cost_usd']:>9.4f}")
    print(f"\nGross Amount:    ${res['gross_amount_usd']:>10.2f}")
    print(f"Credits Applied: ${res['credits_applied_usd']:>10.2f}")
    print(f"Net Amount Due:  ${res['net_amount_due_usd']:>10.2f}")
    print(f"Avg Cost/1k Tokens: ${res['avg_cost_per_1k_tokens_usd']}")
    print(f"Status: {res['invoice_status']}")

if __name__ == "__main__":
    main()
