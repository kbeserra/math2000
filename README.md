# MATH 2000
## Lecture Notes

### Description:
This repository contains my lecture notes teaching the introduction to mathematics and proof writing class at the University of North Texas, Math 2000.
This project also acts as an at-scale example of a practice of document preparation I am calling recursive LaTeX.  

### Recursive LaTeX
If you explore this project you will notice that the content of this document is in many files.
Each file Tex file in this project, with exception of the top-most document.tex file, starts with the command `\guard`.
The `\guard` command acts as just as a [#include guard](https://en.wikipedia.org/wiki/Include_guard) in the C programming language.
Placing `\guard` at the top of a file allows that file to be `\input`-ed many times into a document, but rendered precisely once and at its first `\input`.

The intention of the `\guard` command is to allow the content of a document to be fragmented *atoms*, where an atom is a file starting with the `\guard` command containing a single idea.
Each of these *atoms* are responsible to `\input` the minimum *atoms* necessary to make sense of the idea being presented.

For instances, a definition for an even integer aught to include an `\input` for the definition of an integer.
Further, an even integer might, depending on the level of pedantry of the document, also `\input` a definition for the integer 2, as well as the definition for the integer multiplication.

*Atoms* should never include unnecessary `\inputs`.

For instances, a definition for an even integer should never `\input` an *atom* which makes use of the definition of a real number, as that is certainly outside the minimal scope of an even integer. 
