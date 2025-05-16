# Module 2-Week 5 – API Practice

This project uses the free Wizard World API to explore how to pull and display data using Python and pandas.

I created two simple scripts:

elixir.py – pulls a list of magical elixirs  
houses.py – pulls info about the four wizarding houses

Each script makes a request to the API, turns the JSON into a pandas DataFrame, and prints a clean table.

## How to Run

1. Clone or download this repo
2. Open the folder in VS Code
3. Make sure pandas is installed: pip install pandas
4. Run either file:

python elixir.py  
python houses.py


## API Source

All data comes from the [Wizard World API](https://wizard-world-api.herokuapp.com/swagger/index.html).
This is a free, public API. No key is required.

I wanted to compare traits across houses or look at which elixirs are the most complex based on difficulty and ingredients. This could lead to visualizations in a future project.