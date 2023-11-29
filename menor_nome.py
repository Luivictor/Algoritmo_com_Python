#Apos indicar uma lista de nomes, o programa fara uma busca do menor para o maior.
def menor_nome(nomes):
	if not len(nomes) or type(nomes) != list:
		return "Anônimo"
	
	nomeCurto = nomes[0]
	comprimentoDoNomeCurto = len(nomes[0])

	for nome in nomes:
		nome = nome.strip()

		if len(nome) < comprimentoDoNomeCurto:
			comprimentoDoNomeCurto = len(nome)
			nomeCurto = nome

	return nomeCurto.capitalize()

#Esse é um script automatizado de testes
def test_nomeMaisCurto():
	nomes = ['maria', 'josé', 'PAULO', 'Catarina']
	assert menor_nome(nomes) == "José"

def test_nomesComEspacos():
	nomes = ['maria', ' josé  ', '  PAULO', 'Catarina  ']
	assert menor_nome(nomes) == "José"

def test_nomesComMaiusculasEMinusculas():
	nomes = ['Bárbara', 'JOSÉ  ', 'Bill']
	assert menor_nome(nomes) == "José"

def test_nomesComOMesmoComprimento():
	nomes = ['zé', ' lu', 'fê']
	assert menor_nome(nomes) == "Zé"

def test_listaDeNomesVazia():
	nomes = []
	assert menor_nome(nomes) == "Anônimo"

def test_listaDeNomesInvalida():
	nomes = "carlos"
	assert menor_nome(nomes) == "Anônimo"