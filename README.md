# BigBotChester
Um bot que acompanha comentários/posts da GGG

Sobre:
Bot feito com a intenção de postar toda informação nova comentada ou postada por membros da equipe GGG

Como funciona:
Essa aplicação busca através do gggtracker novos comentários e posts realizados pela GGG e realiza a postagem no twitter através da API.

Como utilizar:

Você pode baixar os arquivos e alterar conforme necessário. Ao executar o arquivo é necessário entrar na aba de configurações e definir os campos de banco de dados e da API do twitter.
Caso deseje utilizar sem banco de dados, será necessário alterar no código para retirar os requesitos do mesmo.
Se desejar utilizar o banco de dados, pode-se alterar a query através do arquivo tweet.py, ou criar a tabela com as mesmas características já configuradas.

BBCIDPST - ID
BBCLKPST - Link
BBCNMSTF - autor
BBCPOSTD - indicador de postagem
BBCDTPST - data
BBCPOSTT - título

Qualquer alteração que gere nova release, terá o executável sem banco de dados.


Essa aplicação não tem nenhuma filiação com GGGtracker.
