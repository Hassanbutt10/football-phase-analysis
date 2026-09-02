import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import warnings
warnings.filterwarnings('ignore')

def parse_loc(val):
    if pd.isna(val):
        return (np.nan, np.nan)
    try:
        loc = eval(val) if isinstance(val, str) else val
        return (loc[0], loc[1])
    except Exception:
        return (np.nan, np.nan)

ev = pd.read_csv('events_Argentina.csv')
ev['x'], ev['y'] = zip(*ev['location'].apply(parse_loc))

passes = ev[(ev['team'] == 'Argentina') & (ev['type'] == 'Pass')].dropna(subset=['x', 'y'])

pitch = Pitch(pitch_type='statsbomb', pitch_color='#0d1b2a', line_color='#3a5a7a', linewidth=1.2)
fig, ax = pitch.draw(figsize=(10, 7))
fig.set_facecolor('#0d1b2a')

bin_stat = pitch.bin_statistic(passes['x'], passes['y'], statistic='count', bins=(6, 5))
pitch.heatmap(bin_stat, ax=ax, cmap='YlOrBr', alpha=0.85, edgecolor='#0d1b2a', linewidth=1)

ax.set_title("Argentina — Pass Origin Zones (WC 2022 Final)", color='white', fontsize=14, pad=12)

plt.tight_layout()
plt.savefig('argentina_zonal_map.png', dpi=200, facecolor='#0d1b2a', bbox_inches='tight')
print("Saved argentina_zonal_map.png")