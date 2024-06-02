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
`python3 run.py --runs 10 --gens 10 --pop_size=10 --elitism true --save_to ./results/test.csv`

## 💻 Available algorithms
The selection, crossover, and mutation algorithms implemented either by charles or not are:


| Selection          | Crossover        | Mutation   |
|--------------------|------------------|------------|
| Ranking Selection    | Two Point Crossover       | Swap Mutation       |
| Tournament Selection | Single Point Crossover    | Inversion Mutation  |
| FP Selection         | Uniform Crossover         | Scramble Mutation   |
