class Contexto:
  def __enter__(self):
    print("Abrindo conexao com o banco de dados")
    return self

  def __exit__(self):
    print("Fechando conexao com o banco de dados")
    return self

with Contexto() as cs:
  print("Exetucando o banco de dados!")