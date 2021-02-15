import json

def norm(request):
    print(request.get('body'))
    normalized = {value.get("name"): v for value in json.loads(request.get('body'))
                  for
                  k, v in value.items() if 'val' in str(k).lower()}
    print(normalized)
    return normalized

def lambda_handler(event, context):
    return str(norm(event))