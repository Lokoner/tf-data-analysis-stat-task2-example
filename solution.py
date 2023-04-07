import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 894208417 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    left = 0.014 + (norm.ppf(alpha / 2) + 1) * (loc - 0.014) / scale
    right = 0.014 + (norm.ppf(1 - alpha / 2) + 1) * (loc - 0.014) / scale
    return left, right
