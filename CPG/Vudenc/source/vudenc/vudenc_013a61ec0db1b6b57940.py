async def _get(test_client, path):...
app = main.create_app()
app.on_startup.append(_clean_tables)
client = await test_client(app)
resp = await client.get(path)
text = await resp.text()
return text
