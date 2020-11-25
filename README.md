# Predicting CS:GO FTW

<br>

**Victor Lucia**

**Ironhack Madrid 2020 Part-time**
##

<br>

The objective of the project is to **predict relevant information** on the fly of ranked matches in the competitive video-game Counter-Strike: Global Offensive (CS:GO), played daily by more than 800.000 players worldwide. With this information the teams can anticipate and coordinate for the next round, creating good strategies either defense or attack, depending on the side they are playing:
- Counter Terrorist (CT): Defense
- Terrorist (T): Attack

Counter-Strike: Global Offensive forms part of the eSports, a growing market that is living his golden years with followers all over the world and moving big amounts of money. Only in tournament prizes, [CS:GO has passed $100M](https://esportsobserver.com/csgo-passes-100m-totalprize-money/)  from his beginning.

![Image](https://raw.githubusercontent.com/Laserdan/Predicting_CSGO_FTW/master/assets/csgo_cup.jpg)

## :floppy_disk: Data Source

The original data came from a [Kaggle dataset](https://www.kaggle.com/skihikingkevin/csgo-matchmaking-damage), where more than 12.000 matches are tracked. 

An important fact is that matches are not from the in-game matchmaking system. They are from a third-party service called [ESEA](https://play.esea.net/), a competitive environment with experimented players and where professional teams train and compete. This makes that we can consider the reliability of the data, knowing that most of the information will be relevant and usable.

[Here](https://www.kaggle.com/danielmazzone/csgo-data-analysis-and-machine-learning) you can find an exploratory analysis of the data made by Daniel Mazzone


##  :nut_and_bolt: Workflow

### :mag: Obtain the prediction models
From the kaggle datasets:
- <code>esea_master_dmg_clean_demos.csv</code>
- <code>esea_master_grenades_clean_demos.csv</code>
- <code>esea_meta_demos.csv</code>
- <code>esea_master_kills_demos.csv</code>

Obtain the following features through processing ([2_1_ml_preprocessingdata.ipynb](https://github.com/Laserdan/Predicting_CSGO_FTW/blob/master/notebooks/2_1_ml_preprocessingdata.ipynb)):
- file
- round
- weapons value (value from records and fill the missing data with the mean)
- grenades value (value from records)
- players alive previous round
- winner team
- bomb planted previous round
- consecutive wins
- real team value
- round type

![Image](https://raw.githubusercontent.com/Laserdan/Predicting_CSGO_FTW/master/assets/acquisition_table.png)

1. **Regressor models to obtain <code>ct_val_pred</code> and <code>t_val_pred</code> ([2_4_ml_regressor_lgbm_tuning.ipynb](https://github.com/Laserdan/Predicting_CSGO_FTW/blob/master/notebooks/2_4_ml_regressor_lgbm_tuning.ipynb))**

2. **Multiclass classifier models to obtain <code>ct_nxt_rnd_type_pred</code> and <code>t_nxt_rnd_type_pred</code> ([4_3_ml_clas_nxt_rnd_val.ipynb](https://github.com/Laserdan/Predicting_CSGO_FTW/blob/master/notebooks/4_3_ml_clas_nxt_rnd_val.ipynb))**

3. **Classifier model to obtain <code>nxt_ct_winner_pred</code> ([5_2_algorithm_election_ml_clas_winner_team.ipynb](https://github.com/Laserdan/Predicting_CSGO_FTW/blob/master/notebooks/5_2_algorithm_election_ml_clas_winner_team.ipynb))**

### :flags: Pipeline
Pipeline with the models loaded which digest the data from the rounds and return de predictions on the fly.

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

