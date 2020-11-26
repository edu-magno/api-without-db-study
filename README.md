# C1 - Agendamento

## Passos realizados

* Aplicação desenvolvida com a finalidade de organizar agendamentos de alunos.
* Foi utilizado Blueprints para fazer as rotas
* Optei por utilizar o mesmo Blueprint, quando a unica diferença era o metódo passado, utilizando um exemplo da documentação do Flask.
* Foi realizado testes unitários em todas as funções utilizadas dentro das rotas


## Endpoints



### GET /appointments

> retorna os agendamentos cadastrados.

response:

```json
[
  {
    "_growth": "Agora o aluno já entendeu que sistemas de equações podem ser representado por matrizes",
    "class-number": "3",
    "date": "Wed Sep 09 2020 17:00:00 GMT-0300 (-03)",
    "difficulty": "Não consegue entender como escalonar matrizes",
    "id": "1",
    "name": "Harry potter",
    "school-subjects": "Matemática"
  },
  {
    "_growth": "Agora o aluno já entendeu que sistemas de equações podem ser representado por matrizes",
    "class-number": "3",
    "date": "Wed Sep 09 2020 10:00:00 GMT-0300 (-03)",
    "difficulty": "Não consegue entender como escalonar matrizes",
    "id": "5",
    "name": "Son Goku",
    "school-subjects": "Matemática"
  }
]

```

### POST /appointment

> cadastra um novo agendamento, caso o horário esteja disponível e esteja entre as 08h até as 23h.

body:

```json
    {
	"date": "Wed Sep 09 2020 14:52:13 GMT-0300 (-03)",
	"name": "Son Goku",
	"school-subjects": "Matemática",
	"difficulty": "Não consegue entender como escalonar matrizes",
	"class-number": 3,
	"_growth": "Agora o aluno já entendeu que sistemas de equações podem ser representado por matrizes"
    }

```

response:

```json
{
  "_growth": "Agora o aluno já entendeu que sistemas de equações podem ser representado por matrizes",
  "class-number": 3,
  "date": "Wed Sep 09 2020 14:00:00 GMT-0300 (-03)",
  "difficulty": "Não consegue entender como escalonar matrizes",
  "id": 8,
  "name": "Son Goku",
  "school-subjects": "Matemática"
}

```

> caso não seja possivel ser feito o agendamento

response :

```json
{
  "message": "O horário já está ocupado, tente outro horário entre 08:00-23:00"
}

```


### GET /appointments/available_times_on_the_day?date=<dia que quer buscar>

> retorna todos os horários disponíveis no dia passado no parâmetro date no endpoint.

formatado da data:

    ```
        dia | mes | ano
        ex: 09092020

    ```

response:

```json
{
  "available-times": [
    "08:00:00",
    "09:00:00",
    "11:00:00",
    "12:00:00",
    "15:00:00",
    "16:00:00",
    "18:00:00",
    "19:00:00",
    "20:00:00",
    "21:00:00",
    "22:00:00",
    "23:00:00"
  ]
}

```

### PATCH /appointment/<id do agendamento>

> modifica um agendamento já existente. No caso de mudança de datas, só vai ser feito a modificação se o horário desejado esteja disponível.

exemplo de uso:

```
/appointment/8

```

body:

```json
{
    "date": "Wed Sep 09 2020 15:52:13 GMT-0300 (-03)"
}

```

response:

```json
{
  "_growth": "Agora o aluno já entendeu que sistemas de equações podem ser representado por matrizes",
  "class-number": "3",
  "date": "Wed Sep 09 2020 15:00:00 GMT-0300 (-03)",
  "difficulty": "Não consegue entender como escalonar matrizes",
  "id": "8",
  "name": "Son Goku",
  "school-subjects": "Matemática"
}
```

caso o horário esteja ocupado:

```json
{
  "message": "O horário já está ocupado, tente outro horário entre 08:00-23:00."
}

```

caso o horário seja menor que 08h ou maior que 23h:

```json
{
  "message": "O horário está indisponível, os horários disponíveis são das 08:00 até as 23:00."
}

```

caso o agendamento não exista:

```json
{
  "message": "O agendamento não existe."
}

```

### DELETE /appointment/<id do agendamento>

> remove o agendamento selecionado.

response:

```json
{
  "sucess": "agendamento excluido!"
}
```

caso o agendamento não exista:

```json
{
  "error": "o agendamento não existe, tente novamente."
}

```



## Passos futuros

* Refatorar algumas partes do código onde, pode ser reaproveitado.
* Implementar banco de dados no lugar do arquivo csv.