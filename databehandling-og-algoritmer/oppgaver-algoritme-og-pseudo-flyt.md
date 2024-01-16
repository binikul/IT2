# Oppgave 1
3

# Oppgave 2
3

# Oppgave 3
3

# Oppgave 4
3

# Oppgave 5
4

# Oppgace 6
1 og 3

# Oppgave 7
Bilde i mappe

# Oppgave 8
FUNCTION trekanttall (n)
  SET tn TO n * (n+1)/2
  RETURN tn
ENDFUNCTION

FUNCTION beregn_totalsum()
  SET totalsum TO 0
  FOR i FROM 1 TO 10
    SET trekant_verdi TO trekanttall(i)
    SET totalsum TO totalsum + trekant_verdi
  END FOR
  RETURN totalsum
END FUNCTION