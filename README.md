# WALLPAPER-SUN-AWS

Programa esta na brach master


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallpaper Upload System</title>
</head>
<body>
    <h1>Wallpaper Upload System</h1>

    <p>Este projeto permite que usuários enviem imagens para um armazenamento de objetos na nuvem (Amazon S3) e visualizem as imagens enviadas em uma galeria simples. A aplicação é construída com o framework Flask, utiliza AWS S3 para armazenamento de imagens, e DynamoDB para registro de logs de uploads.</p>

    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Flask:</strong> Framework web utilizado para criar a aplicação.</li>
        <li><strong>AWS S3:</strong> Serviço de armazenamento de objetos na nuvem para armazenar as imagens enviadas.</li>
        <li><strong>AWS IAM:</strong> Gerenciamento de permissões e segurança para o acesso ao S3.</li>
        <li><strong>DynamoDB:</strong> Banco de dados NoSQL da AWS para registrar logs dos uploads.</li>
        <li><strong>HTML e CSS:</strong> Para a construção da interface de usuário.</li>
    </ul>

    <h2>Funcionalidades</h2>
    <ul>
        <li><strong>Upload de Imagens:</strong> O usuário pode enviar imagens através de um formulário para o servidor, que as armazena no AWS S3.</li>
        <li><strong>Exibição de Galeria:</strong> O usuário pode visualizar todas as imagens enviadas através de uma galeria gerada dinamicamente a partir do S3.</li>
        <li><strong>Logs de Upload:</strong> Informações sobre os uploads, como nome da imagem, URL e data de upload, são registradas em uma tabela no DynamoDB.</li>
    </ul>

    <h2>Como Usar</h2>
    <h3>Requisitos</h3>
    <ul>
        <li>Python 3.x</li>
        <li>Flask</li>
        <li>Boto3 (AWS SDK para Python)</li>
        <li>Conta AWS com acesso a S3 e DynamoDB</li>
    </ul>

    <h3>Instalação</h3>
    <ol>
        <li>Clone o repositório:
            <pre><code>git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio</code></pre>
        </li>
        <li>Instale as dependências:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Configure as credenciais da AWS (se necessário) em seu ambiente:
            <pre><code>aws configure</code></pre>
        </li>
        <li>Crie um bucket no <strong>Amazon S3</strong> com as permissões necessárias para upload e acesso público às imagens.</li>
        <li>Crie uma tabela no <strong>DynamoDB</strong> para registrar os logs de upload.</li>
    </ol>

    <h3>Executando o Projeto</h3>
    <ol>
        <li>Execute o aplicativo Flask:
            <pre><code>python application.py</code></pre>
        </li>
        <li>Acesse a aplicação no navegador:
            <ul>
                <li>Página inicial: <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a></li>
                <li>Galeria de imagens: <a href="http://127.0.0.1:5000/gallery">http://127.0.0.1:5000/gallery</a></li>
            </ul>
        </li>
    </ol>

    <h2>Estrutura do Projeto</h2>
    <ul>
        <li><strong>application.py:</strong> Código principal da aplicação Flask.</li>
        <li><strong>templates/:</strong> Diretório com os arquivos HTML.</li>
        <li><strong>static/:</strong> Arquivos estáticos (CSS, JS, etc.).</li>
        <li><strong>requirements.txt:</strong> Dependências do projeto.</li>
    </ul>

    <h2>Desafios e Considerações</h2>
    <ul>
        <li>A configuração do <strong>AWS IAM</strong> para garantir que as permissões para upload e visualização de imagens sejam seguras.</li>
        <li>A otimização do uso do <strong>DynamoDB</strong> para armazenar logs de uploads.</li>
    </ul>

    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a <a href="LICENSE">MIT License</a>.</p>
</body>
</html>
