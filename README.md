# CP3 - Python
## Colocando Classes no projeto CRM
Durante as aulas de python, criamos um projeto CRM. Na última aula, aplicamos os conceitos de POO (Programação Orientada a Objetos) nos arquivos model (modelo de lead) e repo (backend). 
Nesse repositório, para a entrega da CP3, foi colocadocado o conceito de POO no arquivo stages.


O arquivo model contém uma estrutura de classes onde a informação **stages** das leads são definidas automaticamente a cada lead criado. 
A cada lead formado, o índice da lista aumenta em um, assim o stage é sempre definido diferente do anterior. Quando o índice chegar ao tamanho da lista, ele reinicia.

## Explicando o código de model

1- Foi usado um contador que serviria de índice na lista DEFAULT_STAGES, e esse contador foi salvo em um JSON (status_cont.json) para não reiniciar toda vez que adicionarmos uma lead; <br>
2- Utilizamos o método str para retornar uma string; <br>
3- Utilizamos @classmethod (método da classe) para criar um método que referencia a própria classe ao invés de um objeto, e com esse decorador, criamos as funções carregar_contador e salvar_contador.

No arquivo app.py, importamos o arquivo stages, transformamos em string e o utilizamos como parâmetro para a classe lead importada do model.




