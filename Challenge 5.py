from fractions import Fraction

a = Fraction(5, 1000) 
b = Fraction(8, 1000) 
c = Fraction(10, 1000)

prob_a = ((a*500)/3500) 
prob_b = ((b*1000)/3500) 
prob_c = ((c*2000)/3500)

prob = Fraction(prob_a/(prob_a + prob_b + prob_c))

print(prob)
