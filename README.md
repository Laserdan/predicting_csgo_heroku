# Predicting CS:GO FTW Web App

<br>

**Victor Lucia**

**Ironhack Madrid 2020 Part-time**

**[Link to Web App](https://predicting-csgo-app.herokuapp.com/)**
##

<br>

The objective of the project is to **predict relevant information** on the fly of ranked matches in the competitive video-game Counter-Strike: Global Offensive (CS:GO), played daily by more than 800.000 players worldwide. With this information the teams can anticipate and coordinate for the next round, creating good strategies either defense or attack, depending on the side they are playing:
- Counter Terrorist (CT): Defense
- Terrorist (T): Attack

Counter-Strike: Global Offensive forms part of the eSports, a growing market that is living his golden years with followers all over the world and moving big amounts of money. Only in tournament prizes, [CS:GO has passed $100M](https://esportsobserver.com/csgo-passes-100m-totalprize-money/)  from his beginning.

![Image](https://raw.githubusercontent.com/Laserdan/Predicting_CSGO_FTW/master/assets/csgo_cup.jpg)

## :computer: Webb App

This is the Web App of my final project made for the Data Analytics Bootcamp at Ironhack.

You can find the core of the project in my repo [Predicting_CSGO_FTW](https://github.com/Laserdan/Predicting_CSGO_FTW)

This repo is used to load the predicting models, and deploy the app to make it available for everybody.


##  :nut_and_bolt: Workflow


From the machine learning predictive models made in the [previous repo](https://github.com/Laserdan/Predicting_CSGO_FTW), we load them to make 2 predictions:
- Probability of the next round type for the enemy team.
- Probability of each team to be the winner of the round.

Thanks to the [streamlit library](https://www.streamlit.io/), we create a dashboard for the input of the data and the output of the predictions.
The player fills the required fields to give the ingest data to the models and them print down the predictions.

To be accesible 24/7 to everybody, the app is hosted in [Heroku](https://www.heroku.com/)


## :mag: How to

The player should fill the fields accordingly with the description:

- <code>Select Map</code>: Select the name of the map where the match takes part.
- <code>Select your team</code>: Select the side the player will be playing: Counter-Terrorist or Terrorist.
- <code>Round</code>: Select the current round the player is playing.
- <code>Who win the round?</code>: Select the team who win the previous round: Counter-Terrorist or Terrorist.
- <code>Was the bomb planted?</code>: Select YES or NOT accordingly if the bomb was planted in the previous round.
- <code>Select enemy's round type</code>: Select from the menu what type of round you consider the enemy team did the previous round. Possibilities: PISTOL_ROUND, ECO, MEDIUM, FULL.
- <code>CT players alive previous round</code>: The number of players from the CT side that remain alive at the end of the previous round.
- <code>T players alive previous round</code>: The number of players from the T side that remain alive at the end of the previous round.
- <code>CT consecutive wins</code>: The number of rounds that the CT side is consecutive winning counting the last round.
- <code>T consecutive wins</code>: The number of rounds that the T side is consecutive winning counting the last round.



## :printer: Output


|round|ct_val_pred|t_val_pred|ct_round_type|t_round_type|ct_nxt_rnd_type_pred|t_nxt_rnd_type_pred|nxt_ct_winner_pred|
|----|----|----|----|----|----|----|----|
|	1|  4078.134589|	3943.272665 |	PISTOL_ROUND|	PISTOL_ROUND |	MEDIUM |	ECO |	0|
|	2|	17819.702711|	6290.616771 |	MEDIUM|	        ECO |	        MEDIUM|     FULL|   0|
|	3| 	7038.468589| 	19600.790638| 	MEDIUM| 	    FULL| 	        ECO| 	    MEDIUM| 1|
| 	4| 	1452.468928| 	22568.098741| 	ECO| 	        MEDIUM|         FULL| 	    FULL| 	0|
| 	5| 	22676.205763| 	24459.855175| 	FULL| 	        FULL| 	        ECO| 	    FULL| 	0|
| ...| 	...| 	        ...| 	        ...| 	        ...| 	        ...| 	    ...| 	...|

Where:
- <code>round</code>: Number of the round analyzed.
- <code>ct_val_pred</code>: **Prediction** of the value of all the equipment the ct side is carrying.
- <code>t_val_pred</code>: **Prediction** of the value of all the equipment the t side is carrying.
- <code>ct_round_type</code>: Type of round of the ct side.
- <code>t_round_type</code>: Type of round of the t side.
- <code>ct_nxt_rnd_type_pred</code>: **Prediction** of the type of round of the ct side for the next round.
- <code>t_nxt_rnd_type_pred</code>: **Prediction** of the type of round of the t side for the next round.
- <code>nxt_ct_winner_pred</code>: **Prediction** of the winner side for the next round: 1 if ct side, 0 if t side.

There are more parameters also relevant that are not included to the output to get it more condensed and clear. You can see them in the [6_output.ipynb notebook](https://github.com/Laserdan/Predicting_CSGO_FTW/blob/master/notebooks/6_output.ipynb).

This will be the output when the code will be implemented in-game.

For the stage we are, we have reached to make the predictions of the data we have with 3 different models:
- Value of the team: 2 regression models.
- Next round type: 2 multiclass classification models. 
- Winner for the next round: 1 classification model.

## :rocket: Next Steps

#### :running: Sort term
The next step is to create a pipeline that returns the predictions when a round is passed manually.

#### :walking: Medium term
Get the round information directly from the game and pass it to the pipeline to get the prediction in real-time.

## :computer: Requirements 

| Technology | Version | Documentation | 
| --- | --- | --- |
| Python | 3.7.3 | [www.python.org](https://www.python.org/doc/) |
| Pandas | 1.1.3 | [pandas.pydata.org](https://pandas.pydata.org/docs/reference/index.html) |
| Pandas-profiling | 2.9.0 | [GitHub repo](https://github.com/pandas-profiling/pandas-profiling) |
| Scikit-Learn | 0.23.1 | [scikit-learn.org](https://scikit-learn.org/stable/user_guide.html) |
| Numpy | 1.19.1 | [numpy.org](https://numpy.org/doc/stable/reference/index.html) |
| LightGBM | 2.3.0 | [lightgbm.readthedocs.io](https://lightgbm.readthedocs.io/en/latest/index.html) |
| Joblib | 0.15.1 | [joblib.readthedocs.io](https://joblib.readthedocs.io/en/latest/) |

## :file_folder: Folder structure
```
└── project
    ├── .gitignore
    ├── requeriments.txt
    ├── README.md
    ├── assets/
    ├── data
    │   ├── processed/
    │   └── results/
    ├── models
    │   ├── ct_team_value.joblib
    │   ├── t_team_value.joblib
    │   ├── ct_nxt_rnd_type.joblib
    │   ├── t_nxt_rnd_type.joblib
    │   └── nxt_ct_winner.joblib
    └── notebooks
        ├── archive/
        ├── 0_join_data.ipynb
        ├── 1_direct_estimation.ipynb
        ├── 2_1_ml_preprocessingdata.ipynb
        ├── 2_1_optimization.ipynb
        ├── 2_2_ml_regressor_original_data.ipynb
        ├── 2_3_ml_regressor_modified_data.ipynb
        ├── 2_4_ml_regressor_lgbm_tuning.ipynb
        ├── 3_1_preprocessing_ml_reg_nxt_rnd_val.ipynb
        ├── 3_2_ml_regressor_next_round_value.ipynb
        ├── 4_1_prepr_ml_clas_nxt_rnd_val.ipynb
        ├── 4_2_algorithm_election_gridsearch_ml_clas_nxt_rnd_val.ipynb
        ├── 4_3_ml_clas_nxt_rnd_val.ipynb
        ├── 5_1_prepr_ml_clas_winner_team.ipynb
        ├── 5_2_algorithm_election_ml_clas_winner_team.ipynb
        └── 6_output.ipynb
```



### :love_letter: Contact info
Mail: victorluciajimenez@gmail.com

LinkedIn: [VictorLucia](https://www.linkedin.com/in/victor-lucia/)

Getting help, getting involved, hire me please.

