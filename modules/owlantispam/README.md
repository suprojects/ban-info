# owlantispam API Python Wrapper
# Basic Usage
```python
import owlantispam
token = "A_LONG_TOKEN_HERE"
client = owlantispam.Client(token)
ban = client.get_ban(777000)
print(ban.reason)
```
