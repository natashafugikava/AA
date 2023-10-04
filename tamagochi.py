import streamlit as st

class Tamagochi:
  def __init__(self,nome):
    self.nome = nome
    self.fome = 100
    self.saude = 100
    self.idade = 0

  def set_nome(self, nome):
    self.nome = nome

  def set_fome(self, fome):
    self.fome = fome

  def set_saude(self, saude):
    self.saude = saude

  def set_idade(self, idade):
    self.idade = idade

jogo=False

st.title('Jogo do bichinho virtual da Natasha!')
while not jogo:
  nome = st.text_input('Escolha o nome do seu bichinho:')
  bicho = Tamagochi(nome)
  jogo=True

st.text(bicho.nome)

