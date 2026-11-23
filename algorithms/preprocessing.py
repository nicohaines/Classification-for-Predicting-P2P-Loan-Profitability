import hashlib

import numpy as np
from sklearn.model_selection import StratifiedKFold

DATA_PATH = "../dataset/50-50undersampled.csv"  # built by DataVisualization.ipynb
TEST_SIZE = 0.20
RANDOM_STATE = 42
N_FOLDS = 5


def make_kfold():
    """The 5 CV folds every model uses (same seed -> same folds in every notebook)."""
    return StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=RANDOM_STATE)


def split_fingerprint(X_train, X_test, y_train):
    """Short ID for the test rows + CV folds. If two notebooks print the same
    fingerprint, they tested on the exact same rows and used the exact same folds."""
    test_id = hashlib.md5(np.asarray(X_test.index, dtype=np.int64).tobytes()).hexdigest()[:10]
    train_index = np.asarray(X_train.index, dtype=np.int64)
    fold_rows = np.concatenate([train_index[val] for _, val in make_kfold().split(X_train, y_train)])
    fold_id = hashlib.md5(fold_rows.tobytes()).hexdigest()[:10]
    return f"test={test_id} folds={fold_id}"

IMPUTE_COLS = [
    "num_tl_120dpd_2m",
    "mo_sin_old_il_acct",
    "emp_length",
    "pct_tl_nvr_dlq",
    "tot_cur_bal",
    "num_accts_ever_120_pd",
    "tot_hi_cred_lim",
    "num_tl_op_past_12m",
    "num_tl_90g_dpd_24m",
    "num_tl_30dpd",
    "num_rev_tl_bal_gt_0",
    "num_rev_accts",
    "num_op_rev_tl",
    "num_il_tl",
    "num_bc_tl",
    "total_rev_hi_lim",
    "num_actv_rev_tl",
    "num_actv_bc_tl",
    "total_il_high_credit_limit",
    "avg_cur_bal",
    "mo_sin_rcnt_tl",
    "mo_sin_rcnt_rev_tl_op",
    "mo_sin_old_rev_tl_op",
    "tot_coll_amt",
    "bc_util",
    "percent_bc_gt_75",
    "bc_open_to_buy",
    "num_bc_sats",
    "num_sats",
    "acc_open_past_24mths",
    "total_bal_ex_mort",
    "total_bc_limit",
    "mort_acc",
    "revol_util",
    "pub_rec_bankruptcies",
    "dti",
    "inq_last_6mths",
    "collections_12_mths_ex_med",
    "chargeoff_within_12_mths",
    "tax_liens",
]