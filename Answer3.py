import json
object = {“a”:{“b”:{“c”:”d”}}}
data = json.loads(object)
output = data[a][b][c]
print(output)
