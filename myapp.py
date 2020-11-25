import streamlit as st
import pandas as pd
from joblib import load
import altair as alt

st.set_page_config(layout="wide")

st.write("""
# Predicting CS:GO FTW

""")

col1, col2, col3 = st.beta_columns((1,1,2))

team_dict = {'Counter-Terrorists': 1, 'Terrorists': 0}
yes_no_dict = {'YES': 1, 'NO': 0}
round_type_dic = {'PISTOL_ROUND': 0, 'ECO': 1, 'MEDIUM': 2, 'FULL': 3}
round_type_dic_decode = {0: 'PISTOL_ROUND', 1: 'ECO', 2: 'MEDIUM', 3: 'FULL'}

map_played = col1.selectbox('Select Map', ('de_cache', 'de_dust2', 'de_inferno', 'de_mirage', 'de_nuke', 'de_overpass', 'de_train'))

team = col2.selectbox('Select your team', ('Counter-Terrorists', 'Terrorists'))

def user_input_features():


    round = col1.number_input('Round', value=1)
    winner = team_dict[col1.selectbox('Who win the round?', ('Counter-Terrorists', 'Terrorists'))]
    bomb_planted = yes_no_dict[col1.selectbox('Was the bomb planted?', ('YES', 'NO'))]
    round_type = round_type_dic[col1.selectbox('Select enemy\'s round type', ('PISTOL_ROUND', 'ECO', 'MEDIUM', 'FULL'))]


    ct_alive = col2.number_input('CT players alive previous round', value=0, min_value=0, max_value=5)
    t_alive = col2.number_input('T players alive previous round', value=0, min_value=0, max_value=5)
    ct_cons_wins = col2.number_input('CT consecutive wins', value=0, min_value=0)
    t_cons_wins = col2.number_input('T consecutive wins', value=0, min_value=0)

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
input_df.loc[0, map_played] = 1

if team == 'Counter-Terrorists':
    enemy_team = 'Terrorist'
    model = load('models/db_t_nxt_rnd_type.joblib')
elif team == 'Terrorists':
    enemy_team = 'Counter-Terrorist'
    model = load('models/db_ct_nxt_rnd_type.joblib')

prediction_encoded = model.predict(input_df)[0]
pred_proba = model.predict_proba(input_df)[0][:-1]
pred_proba_df = pd.DataFrame(pred_proba).T
pred_proba_df.columns = ['PISTOL_ROUND', 'ECO', 'MEDIUM', 'FULL']

col3.write(f' ')
col3.write(f'Next round type of {enemy_team} team will be:`%s`' % round_type_dic_decode[prediction_encoded])


source = pd.DataFrame({
    'Round type': pred_proba_df.columns,
    'Probability': pred_proba_df.iloc[0]})

category_names = list(pred_proba_df.columns)

c = alt.Chart(source).mark_bar().encode(
    x=alt.X('Round type', sort=category_names , axis=alt.Axis(title='', labelAngle=0)),
    y=alt.Y('Probability', scale=alt.Scale(domain=[0,1]), axis=alt.Axis(title='', labelAngle=0))).interactive()
col3.altair_chart(c, use_container_width=True)

col3.write(f' ')
col3.write(f'Next round winner... In progress')
