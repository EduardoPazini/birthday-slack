# slack-birthday


## Dependencies

- Python 3.6
- Pip

## Setup

You will need to config a .env.example file with the environment variables. Here i'm using three: TOKEN (slack token authentication), CHANNEL (slack channel id) and SLACK_URL (slack url with the action i want).

After that, run:

	cp .env.example .env

To finish the setup:

	pip install requirements.txt

## Studies

	./ngrok http 3000