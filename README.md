
# spam_detection
## Purpose
The aim of this project is to recognize spam users among decidim.

### How does it work:
A decision tree classifier has been trained to assign a probability to every user of a decidim database.
## Getting Started
### Requirements
- Python >= 3.8
- pip >= 21.x.x
### Note:

This project can be executed only by decidim admins, the data has to be passed by the HTTP method: request


## Deployment

To deploy this project run:

```bash
  pip install -r requiremts.txt
  python app.py
```

If you would like to retrain the model with your own data run:
```bash
  python trainer.py
``` 
The newly created .csv doc has to contain a flag column named "is_spam", where 0 = not a spam, and 1 = is spam. 