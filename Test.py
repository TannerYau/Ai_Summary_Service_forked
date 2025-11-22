# Test application to use mircoservice
import requests

# API endpoint for the service
url = 'http://127.0.0.1:5001/api/ai_summary_service'


# Valid Test 1:
example_data = {
  "summary_length": "medium",
  "additional_info": "yes",
  "content": [
    { 
      "text": "Frieren: Beyond Journey's End is a Japanese manga series written by Kanehito Yamada and illustrated by Tsukasa Abe. It follows Frieren, an elven mage on a journey to reunite with her former comrade Himmel."
    },
    {
      "text": "The story takes place over a long time, as Frieren's elven lifespan makes years seem ephemeral."
    }
  ]
}

# sent post req
response = requests.post(url, json=example_data)
print('Status code: ', response.status_code)
print('Reponse JSON:', response.json())

# Invalid Test 2:
example_data = {
  "summary_length": "medium",
  "additional_info": "yes",
}

# sent post req
response = requests.post(url, json=example_data)
print('\n\nStatus code: ', response.status_code)
print('Reponse JSON:', response.json())
