from scipy.stats import randint, uniform

LIGHTGBM_PARAM = {
    "n_estimators":randint(100,500),
    'max_depth': randint(5,50),
    'learning_rate': uniform(0.01,0.2),
    'num_leaves': randint(20,100),
    'boosting_type':['gdbt', 'dart','goss']

}

RANDOM_SEARCH_PARAM = {
    'n_iter':10,
    'cv': 5,
    'n_jobs': -1,
    'verbose':2,
    'random_state': 42,
    'scoring': 'accuracy'
}
