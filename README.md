<img src="https://static.vecteezy.com/system/resources/thumbnails/015/280/601/small_2x/hand-drawn-genes-and-dna-illustration-png.png" alt="Gene illustration" align="right" style="width: 250px;">
  
# Computational Intelligence For Optimization
<p>This repository is dedicated solely for study purposes. It utilizes the Charles library, which was developed during the CIFO practical classes at the NOVA Information Management School as part of the Data Science & Advanced Analytics master's program.</p>

## 📂 Structure 

```
.
├── ...
├── analytics/               
│   ├── images/              # lineplots, boxplots etc
│   └── evaluation.ipnyb     # evalutaion from results
├── charles/                 # the charles library
├── data/                    # the dataset
├── results/                 # results for the dataset in csv
|── fitness.py               # the fitness implementation 
|── mutation.py              # custom mutations algorithms
|── representation.py        # encode and decode functions 
|── run.py                   # build combinations, run, saves into results 
|── selection.py             # custom selection algorithms 
|── xo.py                    # custom xo algorithms 
└── ...
```

## 🏃‍♂️ How to run 

1. Choose the total runs, generations, population size, and if you want to run with elitism in line #79
2. Select a path to save the csv with the results in line #82
3. Run with `python3 run.py`
