# DistributedServerCache
[Operational Research] University project of distributed server caching using Pham's bee algorithm

# Running
```
python main.py [-h] [-i I] [-o O] [-n N] [-m M] [-e E] [-nep NEP] [-nsp NSP]
               [-ngh NGH] [-max MAX] [-s S]

optional arguments:
  -h, --help                 display help
  -i I, -input_file I        input file path
  -o O, -output_file O       output file path
  -n N, -bees N              number of bees
  -m M, -good_solutions M     number of good solutions
  -e E, -elite_solutions E     number of elite solutions
  -nep NEP                   number of solutions in elite neighbourhood
  -nsp NSP                    number of solutions in good solutions' neighbourhood
  -ngh NGH                    neighbourhood radius
  -max MAX, -iterations MAX     number of iterations
  -s S, -save_solution S     save solution to the output file? (true/false)
```

# Example output
```
>python main.py -i files/me_at_the_zoo.in -max 500
{0: [99, 1, 65, 19, 46, 16, 82, 5, 10], 1: [31, 1, 10, 6, 0, 5, 99, 16], 2: [48, 23, 62, 16, 4], 3: [0, 2, 16, 27, 10, 5, 4], 4: [10, 17, 0, 3, 81], 5: [37, 32, 8, 16, 10, 81,
4], 6: [44, 0, 5, 4, 24, 16], 7: [5, 54, 1, 21, 27], 8: [21, 3, 4, 10, 13, 16], 9: [97, 1, 5, 10, 8, 16, 4]}
-----------------------------
Algorithm took: 21.93 s
-----------------------------
Achieved after iteration: 102
-----------------------------
Saved time: 411.33 s (score: 411332.74558721465)
```
