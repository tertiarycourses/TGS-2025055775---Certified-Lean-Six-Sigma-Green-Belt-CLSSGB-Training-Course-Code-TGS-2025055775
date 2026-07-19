#!/usr/bin/env python3
"""Lean Six Sigma GREEN BELT teaching content — the concept slides, in DMAIC order.

This module is a thin facade. The actual teaching content lives in one module per
DMAIC phase so each stays readable and independently editable:

    concepts_foundations.py  -> foundations(d)
    concepts_define.py       -> define_phase(d)
    concepts_measure.py      -> measure_phase(d)
    concepts_analyze.py      -> analyze_phase(d)
    concepts_improve.py      -> improve_phase(d)
    concepts_control.py      -> control_phase(d)

Every key concept is explained VISUALLY (diagram, chart, matrix, timeline) rather
than as a wall of bullets, per the house design standard. Teaching diagrams from
the original v21 trainer deck are imported from courseware/assets/diagrams/ so
formulas are reproduced exactly as taught rather than retyped from memory.

Content is grounded in the CSSC "Six Sigma: A Complete Step-by-Step Guide"
(Green Belt = Chapters 1-24) and the original v21 trainer deck.
"""

from concepts_foundations import foundations
from concepts_define import define_phase
from concepts_measure import measure_phase
from concepts_analyze import analyze_phase
from concepts_improve import improve_phase
from concepts_control import control_phase

__all__ = [
    "foundations",
    "define_phase",
    "measure_phase",
    "analyze_phase",
    "improve_phase",
    "control_phase",
]
