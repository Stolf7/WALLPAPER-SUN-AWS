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
</body>
</html>
