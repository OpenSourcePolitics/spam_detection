
# spam_detection
## Purpose
The aim of this project is to recognize spam users among Decidim.

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

## Training
1. Put a csv inside the data folder with the following columns:
'sign_in_count', 'personal_url', 'about', 'avatar', 'extended_data', 'followers_count', 'following_count', 'invitations_count', 'failed_attempts', 'admin', 'is_spam'
You can use `train_example.csv` as example.
2. `make train`
3. Move new_model.pkl and replace model.pkl in the main folder.