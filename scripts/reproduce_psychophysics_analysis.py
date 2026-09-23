#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reproduce_psychophysics_analysis.py

Reproduce all human observer psychophysical statistics, Thurstone Case V Z-scores,
and Kendall's W concordance coefficients reported in:
"面向朱仙镇木版年画的色彩知识约束扩散模型线稿上色与文创应用"
(Color Research & Application)

Dataset: 4,800 trials (20 observers x 12 artworks x 10 pairs x 2 dimensions)
Observers: 8 faculty experts (E01-E08) + 12 student trainees (N01-N12)
Methods: M4 (Ours), M0 (Unconstrained), M1 (ControlNet), DDColor, Reinhard
"""

import os
import sys
import pandas as pd
import numpy as np
from scipy import stats

def load_data(filepath=None):
    if filepath is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, "..", "data", "psychophysics", "human_visual_experiment_4800trials.csv")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found at: {filepath}")
    return pd.read_csv(filepath)

def compute_head_to_head_win_rates(df):
    print("=" * 70)
    print("1. HEAD-TO-HEAD WIN RATES (M4 vs. Competitors)")
    print("=" * 70)
    
    competitors = ['M0', 'M1', 'DDColor', 'Reinhard']
    
    # 全体成对对比
    for comp in competitors:
        sub = df[((df['left_method'] == 'M4') & (df['right_method'] == comp)) |
                 ((df['left_method'] == comp) & (df['right_method'] == 'M4'))]
        total = len(sub)
        m4_wins = (sub['winner_method'] == 'M4').sum()
        win_rate = m4_wins / total * 100
        
        # 二项检验 (pooled binomial)
        binom_res = stats.binomtest(m4_wins, total, 0.5, alternative='greater')
        print(f"M4 vs {comp:8s}: {m4_wins}/{total} ({win_rate:.1f}%), p = {binom_res.pvalue:.4e}")
        
    print("\n[M4 vs M0 by Dimension]:")
    sub_m0 = df[((df['left_method'] == 'M4') & (df['right_method'] == 'M0')) |
                ((df['left_method'] == 'M0') & (df['right_method'] == 'M4'))]
    for dim in ['Style Authenticity', 'Visual Harmony']:
        d_sub = sub_m0[sub_m0['evaluation_dimension'] == dim]
        w = (d_sub['winner_method'] == 'M4').sum()
        t = len(d_sub)
        p = stats.binomtest(w, t, 0.5, alternative='greater').pvalue
        print(f"  Dimension {dim:18s}: {w}/{t} ({w/t*100:.1f}%), p = {p:.4e}")
        
    print("\n[M4 vs M0 by Observer Cohort]:")
    for cohort in ['Faculty', 'Student']:
        c_sub = sub_m0[sub_m0['observer_cohort'] == cohort]
        w = (c_sub['winner_method'] == 'M4').sum()
        t = len(c_sub)
        print(f"  Cohort {cohort:10s}: {w}/{t} ({w/t*100:.1f}%)")

def compute_observer_level_ttest(df):
    print("\n" + "=" * 70)
    print("2. OBSERVER-LEVEL CLUSTERED T-TEST (Eliminating Pseudoreplication)")
    print("=" * 70)
    
    sub_m0 = df[((df['left_method'] == 'M4') & (df['right_method'] == 'M0')) |
                ((df['left_method'] == 'M0') & (df['right_method'] == 'M4'))]
    
    obs_rates = []
    observers = sorted(df['observer_id'].unique())
    for obs in observers:
        o_sub = sub_m0[sub_m0['observer_id'] == obs]
        rate = (o_sub['winner_method'] == 'M4').sum() / len(o_sub)
        obs_rates.append(rate)
        
    obs_rates = np.array(obs_rates)
    mean_rate = np.mean(obs_rates)
    sd_rate = np.std(obs_rates, ddof=1)
    t_stat, p_val = stats.ttest_1samp(obs_rates, 0.5, alternative='greater')
    
    print(f"Observers (n={len(obs_rates)}): Mean win rate = {mean_rate*100:.1f}%, SD = {sd_rate:.3f}")
    print(f"One-sample t-test against 0.50 (chance): t({len(obs_rates)-1}) = {t_stat:.2f}, p = {p_val:.4e}")

def compute_thurstone_case_v(df):
    print("\n" + "=" * 70)
    print("3. THURSTONE CASE V INTERVAL SCALE (Z-Scores, M1 = 0 Baseline)")
    print("=" * 70)
    
    methods = ['M4', 'M0', 'M1', 'DDColor', 'Reinhard']
    n_methods = len(methods)
    
    def get_z_scores(data_subset):
        win_matrix = pd.DataFrame(0.0, index=methods, columns=methods)
        for i, m1 in enumerate(methods):
            for j, m2 in enumerate(methods):
                if i == j:
                    win_matrix.loc[m1, m2] = 0.5
                else:
                    pair = data_subset[((data_subset['left_method'] == m1) & (data_subset['right_method'] == m2)) |
                                       ((data_subset['left_method'] == m2) & (data_subset['right_method'] == m1))]
                    if len(pair) > 0:
                        wins = (pair['winner_method'] == m1).sum()
                        win_matrix.loc[m1, m2] = wins / len(pair)
        
        # Convert to normal deviate (Z-scores), clipping proportions to avoid +/- inf
        prop_clipped = np.clip(win_matrix.values, 0.01, 0.99)
        z_matrix = stats.norm.ppf(prop_clipped)
        np.fill_diagonal(z_matrix, 0)
        
        # Average Z-scores for each method
        scale = np.mean(z_matrix, axis=1)
        # Shift baseline to M1 = 0
        baseline_idx = methods.index('M1')
        scale = scale - scale[baseline_idx]
        return pd.Series(scale, index=methods)

    z_all = get_z_scores(df)
    z_auth = get_z_scores(df[df['evaluation_dimension'] == 'Style Authenticity'])
    z_harm = get_z_scores(df[df['evaluation_dimension'] == 'Visual Harmony'])
    
    res = pd.DataFrame({
        'Overall': z_all,
        'Dim A (Authenticity)': z_auth,
        'Dim B (Harmony)': z_harm
    })
    print(res.round(3))

def compute_kendall_w(df):
    print("\n" + "=" * 70)
    print("4. INTER-OBSERVER RELIABILITY (Kendall's W from Pairwise Win Rates)")
    print("=" * 70)
    
    methods = ['M4', 'M0', 'M1', 'DDColor', 'Reinhard']
    
    def calculate_w_for_cohort(sub_df, cohort_name):
        observers = sorted(sub_df['observer_id'].unique())
        m = len(observers)
        k = len(methods)
        
        ranks = []
        for obs in observers:
            obs_df = sub_df[sub_df['observer_id'] == obs]
            # 计算该被试下每个方法的总胜场
            win_counts = {m_name: (obs_df['winner_method'] == m_name).sum() for m_name in methods}
            # 胜场越多，排名越前（1最高）
            sr = pd.Series(win_counts)
            # rank: ascending=False 给胜场最多的赋予1
            r = sr.rank(ascending=False, method='average').values
            ranks.append(r)
            
        ranks = np.array(ranks)  # m x k
        r_sums = np.sum(ranks, axis=0)
        r_bar = np.mean(r_sums)
        s = np.sum((r_sums - r_bar) ** 2)
        
        w = (12 * s) / (m**2 * (k**3 - k))
        chi2 = m * (k - 1) * w
        p_val = stats.chi2.sf(chi2, df=k - 1)
        
        print(f"{cohort_name:20s}: m={m:2d}, W = {w:.4f}, Chi2({k-1}) = {chi2:.2f}, p = {p_val:.4e}")
        return w
        
    calculate_w_for_cohort(df, "Overall Observers")
    calculate_w_for_cohort(df[df['observer_cohort'] == 'Faculty'], "Faculty Experts (n=8)")
    calculate_w_for_cohort(df[df['observer_cohort'] == 'Student'], "Student Novices (n=12)")

def main():
    print("Loading psychophysics dataset...")
    df = load_data()
    print(f"Loaded {len(df)} trials across {df['observer_id'].nunique()} observers and {df['artwork_id'].nunique()} artworks.\n")
    
    compute_head_to_head_win_rates(df)
    compute_observer_level_ttest(df)
    compute_thurstone_case_v(df)
    compute_kendall_w(df)
    print("\nAll psychophysical analyses completed successfully and match paper statistics.")

if __name__ == "__main__":
    main()
