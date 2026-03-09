import pstats

p = pstats.Stats("j_nopil.stats")
p.sort_stats("cumulative")
p.print_stats()
p.print_callers()
p.print_callees()
