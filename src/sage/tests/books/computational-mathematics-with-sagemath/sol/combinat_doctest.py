"""
This file (./sol/combinat_doctest.sage) was *autogenerated* from ./sol/combinat.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./sol/combinat_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./sol/combinat.tex, line 15::

  sage: Suits = FiniteEnumeratedSet(
  ....:            ["Hearts", "Diamonds", "Spades", "Clubs"])
  sage: Values  = FiniteEnumeratedSet([2, 3, 4, 5, 6, 7, 8, 9, 10,
  ....:                                "Jack", "Queen", "King", "Ace"])
  sage: FourOfaKind = cartesian_product([Arrangements(Values,2), Suits])

Sage example in ./sol/combinat.tex, line 34::

  sage: FourOfaKind.list()
  [([2, 3], 'Hearts'),
   ([2, 3], 'Diamonds'),
  ...
   (['Ace', 'King'], 'Clubs')]

Sage example in ./sol/combinat.tex, line 51::

  sage: FourOfaKind.cardinality()
  624

Sage example in ./sol/combinat.tex, line 66::

  sage: Cards = cartesian_product([Values, Suits])
  sage: Hands = Subsets(Cards, 5)
  sage: FourOfaKind.cardinality() / Hands.cardinality()
  1/4165

Sage example in ./sol/combinat.tex, line 86::

  sage: StraightFlush = cartesian_product([range(1, 11), Suits])
  sage: StraightFlush.cardinality()
  40

Sage example in ./sol/combinat.tex, line 98::

  sage: AllFlush = cartesian_product([Subsets(Values,5),Suits])
  sage: AllFlush.cardinality() - StraightFlush.cardinality()
  5108

Sage example in ./sol/combinat.tex, line 113::

  sage: _ / Hands.cardinality()
  1277/649740
  sage: float(_)
  0.001965401545233478

Sage example in ./sol/combinat.tex, line 153::

  sage: Word(['a','b','b','a','a','b','a']).evaluation_dict()
  {'a': 4, 'b': 3}

Sage example in ./sol/combinat.tex, line 170::

  sage: def is_full_hand(hand):
  ....:     suits = Word([value for (value, suit) in hand])
  ....:     repetitions = sorted(suits.evaluation_dict().values())
  ....:     return repetitions == [2,3]
  sage: is_full_hand({(5, 'Diamonds'), (6, 'Diamonds'), (6, 'Hearts'),
  ....:               (5, 'Spades'), (1, 'Spades')})
  False
  sage: is_full_hand({(3, 'Clubs'), (3, 'Spades'), (3, 'Hearts'),
  ....:               (2, 'Clubs'), (2, 'Spades')})
  True

Sage example in ./sol/combinat.tex, line 200::

  sage: def estimate_proportion(S, predicate, n):
  ....:     count = 0
  ....:     for i in range(n):
  ....:         if predicate(S.random_element()):
  ....:             count += 1
  ....:     return count/n

Sage example in ./sol/combinat.tex, line 212::

  sage: float(estimate_proportion(Hands, is_full_hand, 10000)) # random
  0.0014

Sage example in ./sol/combinat.tex, line 229::

  sage: FullHands = cartesian_product([Arrangements(Values, 2),
  ....:     Subsets(Suits, 3), Subsets(Suits, 2)])

Sage example in ./sol/combinat.tex, line 242::

  sage: [sorted(v) for v in FullHands.first()]
  [[2, 3], ['Diamonds', 'Hearts', 'Spades'], ['Diamonds', 'Hearts']]

Sage example in ./sol/combinat.tex, line 252::

  sage: float(FullHands.cardinality() / Hands.cardinality())
  0.0014405762304921968

Sage example in ./sol/combinat.tex, line 312::

  sage: C = Compositions(5,length=3)
  sage: C.cardinality
  <bound method ..._cardinality_from_iterator ...>

Sage example in ./sol/combinat.tex, line 322::

  sage: IntegerVectors(5,3).list()
  [[5, 0, 0], [4, 1, 0], [4, 0, 1], [3, 2, 0], [3, 1, 1], [3, 0, 2],
   ...
   [0, 4, 1], [0, 3, 2], [0, 2, 3], [0, 1, 4], [0, 0, 5]]

Sage example in ./sol/combinat.tex, line 328::

  sage: OrderedSetPartitions(3).cardinality()
  13
  sage: OrderedSetPartitions(3).list()
  [[{1}, {2}, {3}], [{1}, {3}, {2}], [{2}, {1}, {3}], [{3}, {1}, {2}],
   ...
   [{1, 2}, {3}], [{1, 3}, {2}], [{2, 3}, {1}], [{1, 2, 3}]]
  sage: OrderedSetPartitions(3,2).random_element()    # random
  [{1, 3}, {2}]

Sage example in ./sol/combinat.tex, line 338::

  sage: StandardTableaux([3,2]).cardinality()
  5
  sage: StandardTableaux([3,2]).an_element()
  [[1, 3, 5], [2, 4]]

Sage example in ./sol/combinat.tex, line 350::

  sage: list(AlternatingSignMatrices(1))
  [[1]]
  sage: list(AlternatingSignMatrices(2))
  [
  [1 0]  [0 1]
  [0 1], [1 0]
  ]

Sage example in ./sol/combinat.tex, line 361::

  sage: list(AlternatingSignMatrices(3))
  [
  [1 0 0]  [0 1 0]  [1 0 0]  [ 0  1  0]  [0 0 1]  [0 1 0]  [0 0 1]
  [0 1 0]  [1 0 0]  [0 0 1]  [ 1 -1  1]  [1 0 0]  [0 0 1]  [0 1 0]
  [0 0 1], [0 0 1], [0 1 0], [ 0  1  0], [0 1 0], [1 0 0], [1 0 0]
  ]

Sage example in ./sol/combinat.tex, line 383::

  sage: GF(2)^5
  Vector space of dimension 5 over Finite Field of size 2
  sage: _.cardinality()
  32

Sage example in ./sol/combinat.tex, line 400::

  sage: (2^3-2^0)*(2^3-2^1)*(2^3-2^2)
  168

Sage example in ./sol/combinat.tex, line 406::

  sage: GL(3,2)
  General Linear Group of degree 3 over Finite Field of size 2
  sage: _.cardinality()
  168

Sage example in ./sol/combinat.tex, line 423::

  sage: from sage.combinat.q_analogues import q_factorial
  sage: q = 2; n = 3
  sage: q^(n*(n-1)/2) * (q-1)^n * q_factorial(n,q)
  168
  sage: q = 3; n = 5
  sage: GL(n, q).cardinality()
  475566474240
  sage: q^(n*(n-1)/2) * (q-1)^n * q_factorial(n,q)
  475566474240

Sage example in ./sol/combinat.tex, line 537::

  sage: def C(n):
  ....:     if n == 1:
  ....:         yield BinaryTree()
  ....:     elif n > 1:
  ....:         for k in range(1,n):
  ....:             for t1 in C(k):
  ....:                 for t2 in C(n-k):
  ....:                     yield BinaryTree([t1,t2])

Sage example in ./sol/combinat.tex, line 549::

  sage: list(C(1))
  [.]
  sage: list(C(2))
  [[., .]]
  sage: list(C(3))
  [[., [., .]],
   [[., .], .]]
  sage: list(C(4))
  [[., [., [., .]]],
   [., [[., .], .]],
   [[., .], [., .]],
   [[., [., .]], .],
   [[[., .], .], .]]

Sage example in ./sol/combinat.tex, line 566::

  sage: [len(list(C(n))) for n in range(9)]
  [0, 1, 1, 2, 5, 14, 42, 132, 429]

"""
