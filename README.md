## Reserva de Carros

Projeto de exemplo para demonstrar uma API de reserva de carros utilizando FastAPI e MongoDB.

## Configuração do Ambiente

Certifique-se de ter o Python e o MongoDB instalados em seu sistema.

pip install -r requirements.txt

## Configuração do MongoDB

Certifique-se de que o MongoDB esteja em execução em `mongodb://localhost:27017/`.

## Executando o Projeto

Para iniciar o servidor da API, execute o seguinte comando:

python run.py

O servidor estará disponível em `http://localhost:8000`.

## Rotas da API

- POST /cars/: Cria um novo carro com informações como placa, modelo, chassi e proprietário.

- GET /cars/: Lista todos os carros disponíveis.

- GET /cars/{car_id}: Obtém informações detalhadas sobre um carro específico.

- PUT /cars/{car_id}: Atualiza informações de um carro específico.

- PUT /cars/{car_id}/reserve: Reserva um carro.

- GET /cars/{car_id}/check-reservation: Verifica se um carro está reservado.

## Exemplo de Requisição

Para criar um carro, faça uma solicitação POST com um corpo JSON contendo os detalhes do carro:

**{
  "make": "Toyota",
  "model": "Camry",
  "year": 2022,
  "is_reserved": false,
  "plate": "ABC123",
  "chassis": "1234567890",
  "owner": "João da Silva"
}
**
## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e solicitações de pull (pull requests) para aprimorar o projeto.

## Licença

Este projeto criado para fixação de conceitos, você pode melhora-lo de acordo com suas necessidades.
