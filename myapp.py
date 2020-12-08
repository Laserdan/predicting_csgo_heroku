import streamlit as st
import pandas as pd
from joblib import load
import altair as alt

st.set_page_config(layout="centered")  # To make the app full wide

# Header
st.write("""
# Predicting CS:GO FTW
""")

# Distribute the page into 3 columns
col1, col2 = st.beta_columns(2)

# Define the dicts for the encode-decode
team_dict = {'Counter-Terrorists': 1, 'Terrorists': 0}
team_dict_decode = {1: 'Counter-Terrorists', 0: 'Terrorists'}
yes_no_dict = {'YES': 1, 'NO': 0}
round_type_dic = {'PISTOL_ROUND': 0, 'ECO': 1, 'MEDIUM': 2, 'FULL': 3}
round_type_dic_decode = {0: 'PISTOL_ROUND', 1: 'ECO', 2: 'MEDIUM', 3: 'FULL'}

# Firsts inputs Map and Team
map_played = col1.selectbox('Select Map',
                            ('de_cache', 'de_dust2', 'de_inferno', 'de_mirage', 'de_nuke', 'de_overpass', 'de_train'))
team = col2.selectbox('Select your team', ('Counter-Terrorists', 'Terrorists'))


def user_input_features():
    # Inputs for the predictor model
    # Column 1
    round = col1.number_input('Round', value=1, min_value=1)
    winner = team_dict[col1.selectbox('Who win the round?', ('Counter-Terrorists', 'Terrorists'))]
    bomb_planted = yes_no_dict[col1.selectbox('Was the bomb planted?', ('YES', 'NO'))]
    round_type = round_type_dic[col1.selectbox('Select enemy\'s round type', ('PISTOL_ROUND', 'ECO', 'MEDIUM', 'FULL'))]

    # Column 2
    ct_alive = col2.number_input('CT players alive previous round', value=0, min_value=0, max_value=5)
    t_alive = col2.number_input('T players alive previous round', value=0, min_value=0, max_value=5)
    ct_cons_wins = col2.number_input('CT consecutive wins', value=0, min_value=0)
    t_cons_wins = col2.number_input('T consecutive wins', value=0, min_value=0)

    # Store the input data
    data = {'file': 0,
            'round': round,
            'ct_alive': ct_alive,
            't_alive': t_alive,
            'ct_winner': winner,
            'bomb_planted': bomb_planted,
            'ct_cons_wins': ct_cons_wins,
            't_cons_wins': t_cons_wins,
            'round_type': round_type,
            'de_cache': 0, 'de_cbble': 0, 'de_dust2': 0, 'de_inferno': 0,
            'de_mirage': 0, 'de_nuke': 0, 'de_overpass': 0, 'de_train': 0}
    features = pd.DataFrame(data, index=[0])
    return features


input_df = user_input_features()
input_df.loc[0, map_played] = 1  # Add the map to the input dataframe. Manual One Hot Encoding.

# Load predictor model depending on the team selected
if team == 'Counter-Terrorists':
    enemy_team = 'Terrorist'
    model = load('models/db_t_nxt_rnd_type.joblib')
elif team == 'Terrorists':
    enemy_team = 'Counter-Terrorist'
    model = load('models/db_ct_nxt_rnd_type.joblib')

# Make predictions and prediction probabilites
prediction_encoded = model.predict(input_df)[0]
pred_proba = model.predict_proba(input_df)[0][:-1]
pred_proba_df = pd.DataFrame(pred_proba).T
pred_proba_df.columns = ['PISTOL_ROUND', 'ECO', 'MEDIUM', 'FULL']
next_round_type = round_type_dic_decode[prediction_encoded]

# Get the results for Round Type Prediction
col1.write(f' ')
col1.write(f'Next round type of {enemy_team} team will be:`%s`' % next_round_type)

# Altair for the plot Probabilities
# Define the source
source = pd.DataFrame({'Round type': pred_proba_df.columns,
                       'Probability': pred_proba_df.iloc[0]})

category_names = list(pred_proba_df.columns)  # To order the labels as we want, not alphabetically

# Define the chart
c = alt.Chart(source).mark_bar().encode(
    x=alt.X('Round type', sort=category_names, axis=alt.Axis(title='', labelAngle=0)),
    y=alt.Y('Probability', scale=alt.Scale(domain=[0, 1]), axis=alt.Axis(title='', labelAngle=0))).interactive()
# Plot the chart
col1.altair_chart(c, use_container_width=True)

# Add the prediction of round type to make the prediction of the winner team
input_df['nxt_rnd_type'] = prediction_encoded

# Load predictor model depending on the team selected
if team == 'Counter-Terrorists':
    enemy_team = 'Terrorist'
    model_winner = load('models/db_t_winner_team.joblib')
elif team == 'Terrorists':
    enemy_team = 'Counter-Terrorist'
    model_winner = load('models/db_ct_winner_team.joblib')

# Make predictions and prediction probabilites
pred_winner_encoded = model_winner.predict(input_df)[0]
pred_winner_proba = model_winner.predict_proba(input_df)[0]
pred_winner_proba_df = pd.DataFrame(pred_winner_proba).T
pred_winner_proba_df.columns = ['Terrorist', 'CounterTerrorist']
next_round_winner = team_dict_decode[pred_winner_encoded]

# Get the results for Winner Prediction
col2.write(f' ')
col2.write(f'Next round winner team will be:`%s`' % next_round_winner)

# Altair for the plot Probabilities
# Define the source
source_winner = pd.DataFrame({'Winner': pred_winner_proba_df.columns,
                              'Probability': pred_winner_proba_df.iloc[0]})

category_names = list(pred_winner_proba_df.columns)  # To order the labels as we want, not alphabetically

# Define the chart
c = alt.Chart(source_winner).mark_bar().encode(
    x=alt.X('Winner', sort=category_names, axis=alt.Axis(title='', labelAngle=0)),
    y=alt.Y('Probability', scale=alt.Scale(domain=[0, 1]), axis=alt.Axis(title='', labelAngle=0))).interactive()
# Plot the chart
col2.altair_chart(c, use_container_width=True)

st.write(f' ')
st.markdown('Created by: Victor Lucia    [linkedin](https://www.linkedin.com/in/victor-lucia/)')
