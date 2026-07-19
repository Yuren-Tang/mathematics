# Erratum — color-pair witnesses in the stacked-triangulation strictness example

**Programme:** `AffineCDC — Research Lead`  
**Status:** immediate correction to `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`  
**Scope:** the displayed witness table in Section 6 only; the triangulation, two colorings, and all theorem statements remain unchanged

The complete proper six-coloring is

\[
\begin{array}{c|rrrrrrrrrrrr}
v&0&1&2&3&4&5&6&7&8&9&10&11\\
\hline
\kappa_6(v)&3&1&0&5&2&4&2&3&3&1&1&5.
\end{array}
\]

The following source edges witness all fifteen unordered pairs of the six colors:

\[
\begin{array}{c|c@{\qquad}c|c@{\qquad}c|c}
\text{color pair}&\text{edge}&\text{color pair}&\text{edge}&\text{color pair}&\text{edge}\\
\hline
01&1\!-
2&02&2\!-
4&03&0\!-
2\\
04&2\!-
5&05&2\!-
3&12&1\!-
4\\
13&0\!-
1&14&1\!-
5&15&1\!-
3\\
23&0\!-
6&24&4\!-
5&25&3\!-
4\\
34&5\!-
7&35&0\!-
3&45&5\!-
11
\end{array}
\]

For example, edge `1-2` joins colors `1` and `0`, edge `5-11` joins colors `4` and `5`, and similarly for the other rows. Hence the color-adjacency quotient is exactly `K_6`.

The malformed witness display in Section 6 of the parent packet is superseded by this table. No other statement is changed.
