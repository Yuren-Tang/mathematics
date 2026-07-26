# E306 formal analytic trust boundaries

Two scope-split conditional formal interfaces must not be conflated.

The immutable `v0.0.3` release uses the exact Rosser–Schoenfeld leaf axioms
`rosser_schoenfeld_cor3` (1962, Corollary 3) and
`rosser_schoenfeld_thm5` (1962, Theorem 5).  Lean checks the reduction under
those inputs; it does not prove the classical analytic estimates.

The detached `codex/pushlinter@e55ef359...` line instead assumes the structural
interfaces `pnt_dyadic_prime_density` and
`mertens_dyadic_window_mass`.  It is retained conditional formalization, not a
formalization of PNT or Mertens and not a replacement release.  Scales below
`k=5` are outside the first axiom; the second supplies only an eventual
existential threshold.  Primitive provider theorems and any required finite
small-scale closure remain gaps.
