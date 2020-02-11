from lib.Statement import Statement

def test_make_headers():
  assert Statement.make_headers() == 'date || credit || debit || balance \n'