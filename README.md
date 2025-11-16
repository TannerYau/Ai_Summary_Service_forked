**Instructions to use:**
```
Create a venv:
python -m venv .venv

After download:
select the venv interpreter
To actitivate in the terminal:
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt
```

> The service will take a json with the following attributes and the content array will be an array of json to summarize. 

**To send information:**
Use the Api end point: "/api/ai_summary_service"

Format for JSON in POST request:
```json
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
```

**To recieve information**
Store the json as it's sent back as a response object
> example with react
```react
  .then((res) => res.json()) // Convert response to JSON
  .then((data) => {
    console.log(data);
    // You can now use the data in your component state
  })
```

**Data format returned**
```json
{
    "additional_info_requested": "yes",
    "source_content_chars": 304,
    "summary_length_requested": "medium",
    "summary_text": "**Summary:**\nFrieren: Beyond Journey's End is a Japanese manga series crafted by writer Kanehito Yamada and illustrator Tsukasa Abe. The narrative centers on Frieren, an elven mage, as she embarks on a significant journey. Her primary objective is to reunite with her former comrade, Himmel. A defining characteristic of the story is its expansive timeline, which is profoundly influenced by Frieren's exceptionally long elven lifespan. This unique perspective means that years, which hold immense significance for shorter-lived races, often feel brief and ephemeral to her. This concept of time shapes her experiences, relationships, and the overall progression of the series.\n\n**Additional Information:**\nBeyond its manga origins, *Frieren: Beyond Journey's End* has achieved widespread critical acclaim and popularity, notably through its highly successful anime adaptation. Produced by Studio Madhouse, the anime brought the series' poignant themes of time, memory, grief, and the beauty of everyday moments to a global audience, further solidifying its status as a beloved fantasy work."
}
```