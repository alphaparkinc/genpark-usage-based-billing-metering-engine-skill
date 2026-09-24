import json, sys
from client import UsageBasedBillingMeteringEngineClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "usage-based-billing-metering-engine", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "meter_and_calculate_invoice", "description": "Ingests real-time usage events, applies tiered pricing, and calculates precise usage-based billing invoices with credit offsets."}]}}
    elif method == "tools/call":
        client = UsageBasedBillingMeteringEngineClient()
        res = client.meter_and_calculate_invoice()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = UsageBasedBillingMeteringEngineClient()
        print(json.dumps(client.meter_and_calculate_invoice(), indent=2))
