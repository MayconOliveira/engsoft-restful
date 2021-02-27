# Api CPF Web

## Conceitual

### 1. Defina serviço RESTful.
Um serviço da Web RESTful faz uso explícito de métodos HTTP de 
uma maneira que segue o protocolo definido pela RFC 2616. 
HTTP GET, por exemplo, é definido como um método de produção de dados que se 
destina a ser usado por um cliente aplicativo para recuperar um recurso,
para buscar dados de um servidor Web ou para executar uma consulta com 
a expectativa de que o servidor Web procurará e responderá com um conjunto 
de recursos correspondentes

Um serviço REST pede aos desenvolvedores que usem métodos HTTP explicitamente 
e de uma maneira consistente com a definição do protocolo. 
Este princípio básico de design REST estabelece um mapeamento um para um entre operações de criação, 
leitura, atualização e exclusão (CRUD) e métodos HTTP.

### 2. Liste e explique os quatro principais princípios de serviços RESTful.
Faz uso de métodos HTTP explicitamente, não possui estado, expõe URIs semelhantes à estrutura de diretório,
transfere XML, JavaScript Object Notation (JSON) ou ambos.

### 3. Apresente as diferenças entre serviços SOAP e serviços RESTful.
REST usa formato de mensagem menor e fornece eficiência de custo ao longo do tempo 
e melhor desempenho por causa payload reduzido e das mensagens JSON com as quais faz a comunicação. 

− Curva de aprendizado é reduzida. 
− Suporta comunicação sem estado. 
− É simples de aprender e implementar.
− Eficientemente usa verbos HTTP. 
- Além de JSON (JavaScript Object Notation) também pode usar xml.
− Para segurança, usa padrões HTTP. 
− REST pode ser consumido por qualquer cliente. 
− Fornece os dados disponíveis como recurso. 

Em comparação ao SOAP o REST não cobre todas as variedades de padrões de serviço da web, 
como segurança, transações, diferentes protocolos de transporte, etc.

- Requisitos REST (especialmente GET) não são adequados para grande quantidade de dados.
- Latência nos tempos de processamento de pedidos e uso de largura de banda. 
- REST APIs acabam dependendo dos cabeçalhos para o estado (como para rotear solicitações subsequentes para o mesmo servidor back-end que manipulou a atualização anterior ou para autenticação). 
dependendo da implementação o uso de cabeçalhos é desajeitado e vincula a API ao http como um transporte.

### 4. Na opinião do grupo, qual tipo de serviço é mais fácil e rápido de implementar? Justifique.
REST, devido a popularização do REST nos dias atuais API RESTful se tornou padrão e 
consequentemente a disponibilização de facilitadores, frameworks, bibliotecas e o acesso ao 
conteúdo relacionado a este padrão.

Referências
Alex Rodriguez.: RESTful Web services: The basics. developWorks IBM (2008). 
https://cs.calvin.edu/courses/cs/262/kvlinden/references/rodriguez-restfulWS.pdf.

F Halili, E Ramadani.: Web services: a comparison of soap and rest services, Modern Applied Science (2018). 
https://www.academia.edu/download/55982691/72393-274555-1-PB.pdf.
