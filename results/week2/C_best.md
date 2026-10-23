# Best Phase C variant per family (fixed 0.05, false alarms <= 0.06)

- rescue: mlp_rescue timely 2, false alarms 0.009
- rescue: combined_rescue timely 4, false alarms 0.120
- rescue: mlp_rescue_cusum timely 4, false alarms 0.015
- rescue: combined_rescue_cusum timely 4, false alarms 0.024
- rescue: CHOSEN mlp_rescue_cusum
- memory: gru timely 12, false alarms 0.090
- memory: conv timely 8, false alarms 0.117
- memory: gru_cusum timely 11, false alarms 0.077
- memory: conv_cusum timely 12, false alarms 0.078
- memory: CHOSEN gru_cusum (none within the false-alarm limit)
