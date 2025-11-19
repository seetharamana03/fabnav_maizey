import numpy as np
import pandas as pd

in_progress = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTcFEHlemJJS6S0lzFuMHlSkv17_Wh3k_3PKJKrMpuHF7PJtDfcYKLvZCg_40iOGWL-plkHC82iRGc4/pub?gid=678653982&single=true&output=csv"
in_progress_df = pd.read_csv(in_progress)


def test_script():
    print("This is a test script")
    value = in_progress_df.iloc[2, 0]
    print(value)

if __name__ == "__main__":
    test_script()

#What’s the best way to machine a pocket for a bearing in aluminum?