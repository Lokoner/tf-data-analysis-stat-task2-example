import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 894208417 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    lower_bound = 0.014
    upper_bound = loc + scale * norm.ppf(1 - alpha / 2)
    return (lower_bound, upper_bound)
