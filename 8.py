A = matrix ( RR, 4, [0.45, 0.55, 0 , 0,                   # umbrella
                     0.20, 0.60, 0.20, 0,                     # travel 
                     0, 0, 0.75, 0.25,                       # Seattle
                     0.5, 0, 0, 0.5     ])                   # rainy

emission_symbols = [ 'Seattle', 'travel', 'stay at home', 'rainy']

B = matrix ( RR, 4, 4, [ 0.6, 0.2, 0.2, 0,            # travel 
                         0, 0, 0.75, 0.25,           # Seattle
                         0, 0, 0.5, 0.5,            # rainy
                         0, 0.45, 0.55,0])         # umbrella
                         
initial = [0, 1, 0, 0]

model = hmm.DiscreteHiddenMarkovModel (A, B, initial, emission_symbols)
