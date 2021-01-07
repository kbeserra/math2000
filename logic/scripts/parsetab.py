
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDORIMPLIESIFFrightUNOTAND IFF IMPLIES LPAREN NOT OR RPAREN VALexpression : VALexpression : NOT expression %prec UNOTexpression : expression OR expressionexpression : expression AND expressionexpression : expression IMPLIES expressionexpression : expression IFF expressionexpression : LPAREN expression RPAREN'
    
_lr_action_items = {'VAL':([0,3,4,5,6,7,8,],[2,2,2,2,2,2,2,]),'NOT':([0,3,4,5,6,7,8,],[3,3,3,3,3,3,3,]),'LPAREN':([0,3,4,5,6,7,8,],[4,4,4,4,4,4,4,]),'$end':([1,2,9,11,12,13,14,15,],[0,-1,-2,-3,-4,-5,-6,-7,]),'OR':([1,2,9,10,11,12,13,14,15,],[5,-1,-2,5,-3,-4,-5,-6,-7,]),'AND':([1,2,9,10,11,12,13,14,15,],[6,-1,-2,6,-3,-4,-5,-6,-7,]),'IMPLIES':([1,2,9,10,11,12,13,14,15,],[7,-1,-2,7,-3,-4,-5,-6,-7,]),'IFF':([1,2,9,10,11,12,13,14,15,],[8,-1,-2,8,-3,-4,-5,-6,-7,]),'RPAREN':([2,9,10,11,12,13,14,15,],[-1,-2,15,-3,-4,-5,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,5,6,7,8,],[1,9,10,11,12,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> VAL','expression',1,'p_expression_val','generateTruthTable.py',48),
  ('expression -> NOT expression','expression',2,'p_expression_not','generateTruthTable.py',54),
  ('expression -> expression OR expression','expression',3,'p_expression_or','generateTruthTable.py',59),
  ('expression -> expression AND expression','expression',3,'p_expression_and','generateTruthTable.py',65),
  ('expression -> expression IMPLIES expression','expression',3,'p_expression_IMPLIES','generateTruthTable.py',71),
  ('expression -> expression IFF expression','expression',3,'p_expression_IFF','generateTruthTable.py',77),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_factor_expr','generateTruthTable.py',84),
]
