def lambda_handler(event, context):
    name = event['name']
    age = event['age']
    city = event['city']
    greeting = f"Hello {name}, you are {age} years old and live in {city}!"
    return {
        'message': greeting
    }
