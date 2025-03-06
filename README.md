# BigBotChester
Um bot que acompanha comentários/posts da GGG

Sobre:
Bot feito com a intenção de postar toda informação nova comentada ou postada por membros da equipe GGG

Como funciona:
Essa aplicação busca através do gggtracker novos comentários e posts realizados pela GGG e realiza a postagem no twitter através da API.

Como utilizar:

Você pode baixar os arquivos e alterar conforme necessário. Ao executar o arquivo é necessário entrar na aba de configurações e definir os campos de banco de dados e da API do twitter.
Caso deseje utilizar sem banco de dados, será necessário alterar no código para retirar os requisitos do mesmo.
Se desejar utilizar o banco de dados, pode-se alterar a query através do arquivo tweet.py, ou criar a tabela com as mesmas características já configuradas.

Segue query para criação da tabela do banco de dados MySQL usada de base:

CREATE TABLE BBCPOSTS(BBCIDPST INT AUTO_INCREMENT PRIMARY KEY,BBCLKPST VARCHAR(200),BBCNMSTF VARCHAR(50),BBCPOSTD VARCHAR(4),BBCDTPST TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,BBCPOSTT VARCHAR(150));

Qualquer alteração que gere nova release, terá o executável sem banco de dados.


Essa aplicação não tem nenhuma filiação com GGGtracker.
