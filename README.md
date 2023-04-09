# Coding Interview (TOY) Assistant

*NOTE: please don't actually use this in your coding interviews. IMO the best way to prepare for a coding interview is still 
the old way, i.e.: really understand your data structures and algorithms, as well as the programming language and tech 
stack of your choice (or those required by your potential employer, of course).*

This is a super simple app that allows you to ask questions about a coding interview question verbally, and have ChatGPT 
send you back the answer. As usual, with [LangChain](https://langchain.com/), the core of the app is just a few lines of
Python code. I spent the vast majority of the time fighting with the HTML/CSS/JS. (Of course they were ChatGPT-generated,
but I had to tinker with them a bit more to make them look a bit more decent.)

## Pre-requisites
### OpenAI API Key
You need to have an OpenAI API key. You can get one [here](https://platform.openai.com/account/api-keys).

Set it as an environment variable called `OPENAI_API_KEY`.

### Python & Dependencies
I'm using Python 3.9.

[pyenv](https://github.com/pyenv/pyenv) and the [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) plugin are 
highly recommended to keep your Python versions and environments cleanly separated.

Once you have them installed and have the virtual environment activated, then install the dependencies:

```bash
pip install -r requirements.txt
```
