# Team Phase Classifier - World Cup 2022

Tests whether real match event data confirms common tactical narratives (positional play, low block counter-attacking, possession control) rather than relying on commentary alone.

## Matches analyzed
- Argentina vs France (Final): positional play
- Japan vs Spain: low block / counter-attack
- Croatia vs Brazil: possession control

## What it does
- Pulls every match event (passes, shots, tackles, etc.) with pitch coordinates from StatsBomb open data
- Classifies each team action into one of six phases based on pitch location and game context: Build-up, Progression, Final Third, Transition, High Press, Defending
- Calculates the percentage of each team's actions falling into each phase
- Visualizes results as a stacked bar chart comparing all three teams, plus a pitch heatmap of Argentina's pass origin zones

## Key findings
| Team | Notable pattern |
|---|---|
| Argentina | 26.1% Progression, 24.5% Transition, patient buildup, quick to break |
| Japan | 39% Defending, sat deep against Spain, relied on counters |
| Croatia | 36.3% Progression, highest of the three, midfield-control identity |

## Why it matters
Confirms that tactical concepts like shape-shifting, positional play, and pressing intensity are measurable in real event data, not just visible through match commentary.

## Outputs
- `phase_distribution.png`: 3-team phase comparison chart
- `argentina_zonal_map.png`: pass origin heatmap on pitch

## Tech used
Python, pandas, matplotlib, StatsBomb open data (via statsbombpy)

## Data source
[StatsBomb Open Data](https://github.com/statsbomb/open-data)
