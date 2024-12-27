# Animal Crossing Flower Breeding
The game `Animal Crossing` has a flower breeding system.  
This is a simulator to understand how to calculate probability.  
The colors according to the color genes don't reflect on real world.  

# Support flower types
[ ] TULIP  
[ ] HYASINTHS  
[ ] ROSE  
[ ] ANEMONE (WINDFLOWER)  
[ ] FANJI  
[ ] CHRYSANTHEMUM  
[ ] COSMOS  
[v] LILY  

# Example
`RrYyWwSs`(Rose) or `RrYyWw`(else)  
RR : 2  
Rr : 1  
rr : 0  

</br>  

`RRyyWw`=(201)  Red (from Store)
`rryyWW`=(002)  White (from Store)

```
$ python main.py
LILY breeding result of RED(201) X (002)WHITE
=== GENE_RESULT ===
(0, 0, 0):  0  (0, 0, 1):  0  (0, 0, 2):  0
(0, 1, 0):  0  (0, 1, 1):  0  (0, 1, 2):  0
(0, 2, 0):  0  (0, 2, 1):  0  (0, 2, 2):  0
(1, 0, 0):  0  (1, 0, 1): 32  (1, 0, 2): 32
(1, 1, 0):  0  (1, 1, 1):  0  (1, 1, 2):  0
(1, 2, 0):  0  (1, 2, 1):  0  (1, 2, 2):  0
(2, 0, 0):  0  (2, 0, 1):  0  (2, 0, 2):  0
(2, 1, 0):  0  (2, 1, 1):  0  (2, 1, 2):  0
(2, 2, 0):  0  (2, 2, 1):  0  (2, 2, 2):  0
=== COLOR_RESULT ===
      PINK = 1  (50.00%)    !SPECIAL!
     WHITE = 1  (50.00%)    !SPECIAL!
```

## References
[모여봐요 동물의 숲/각종 공략/꽃 교배법/꽃 유전자형](https://namu.wiki/w/%EB%AA%A8%EC%97%AC%EB%B4%90%EC%9A%94%20%EB%8F%99%EB%AC%BC%EC%9D%98%20%EC%88%B2/%EA%B0%81%EC%A2%85%20%EA%B3%B5%EB%9E%B5/%EA%BD%83%20%EA%B5%90%EB%B0%B0%EB%B2%95/%EA%BD%83%20%EC%9C%A0%EC%A0%84%EC%9E%90%ED%98%95#fn-45)
