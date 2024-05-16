from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import plotly.express as px


soccer_df = pd.read_csv("https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/fundamentals/football_players.csv",low_memory=False)
cols = ['Age', 'Overall', 'Acceleration', 'Aggression',
       'Agility', 'Balance', 'Ball control', 'Composure', 'Crossing', 'Curve',
       'Dribbling', 'Finishing', 'Free kick accuracy', 'GK diving',
       'GK handling', 'GK kicking', 'GK positioning', 'GK reflexes',
       'Heading accuracy', 'Interceptions', 'Jumping', 'Long passing',
       'Long shots', 'Marking', 'Penalties', 'Positioning', 'Reactions',
       'Short passing', 'Shot power', 'Sliding tackle', 'Sprint speed',
       'Stamina', 'Standing tackle', 'Strength', 'Vision', 'Volleys']

soccer_df[cols] = soccer_df[cols].apply(pd.to_numeric, errors='coerce', axis=1)

# Scatter plot using Plotly
fig = px.scatter(soccer_df, x='Strength', y='Vision', color='Overall', hover_name='Name',
                 title='Interactive Scatter Plot of Strength and Vision vs Overall Rating',
                 labels={'Strength': 'Strength Rating', 'Vision': 'Vision Rating', 'Overall': 'Overall Rating'})

# Show the interactive plot


app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home_page():
    
    return render_template('home.html',graphJSON =fig.show())



if __name__== "__main__":
    app.run(debug=True)