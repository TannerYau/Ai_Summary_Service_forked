Create a venv:
python -m venv .venv

After download:
select the venv interpreter
To actitivate in the terminal:
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Format for JSON:
{
  "summary_length": "medium",
  "additional_info": "yes",
  "content": [
    { 
      "text": "Frieren: Beyond Journey's End is a Japanese manga series written by Kanehito Yamada and illustrated by Tsukasa Abe. It follows Frieren, an elven mage on a journey to reunite with her former comrade Himmel."
    },
    // You can add more text blocks here if needed
    {
      "text": "The story takes place over a long time, as Frieren's elven lifespan makes years seem ephemeral."
    }
  ]
}

The service will take a json with the following attributes and the content array will be an array of json to summarize. 