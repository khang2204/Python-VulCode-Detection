"""
try:
    # Get the public IP address from an external service
    public_ip_response = requests.get(config.PUBLIC_IP_SERVICE_URL)
    public_ip_response.raise_for_status()
except (requests.HTTPError, requests.exceptions.InvalidSchema):
    public_ip = "Unknown"
else:
    public_ip = public_ip_response.text
name = name or config.SUPER_SECRET_NAME
content = f"<h1>Hello, {name}!</h1><h2>Public IP: <code>{public_ip}</code></h2>"
# https://fastapi.tiangolo.com/advanced/custom-response/#return-a-response
# FIXME: return HTMLResponse(content)
return Template(content).render()
