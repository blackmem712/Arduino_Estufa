## Sobre

Este projeto é uma aplicação web desenvolvida com Django, que utiliza Tailwind CSS para estilização e Chart.js para visualizações gráficas, e Python para manipulação do microcontrolador arduino. O projeto inclui um script Python chamado `sensors.py`,
que deve ser executado para coletar dados de sensores do arduino, e também buscar dados de uma api de estação metereológica.


## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- Python 3.x
- Git
- Virtualenv (opcional, mas recomendado)
- Mysql ou outro banco de dados compatível com Django
- Visual Studio Code
- Node.js
- Ide do Arduino
- 
## Configuração do Arduino

Para que o Arduino possa se comunicar com o Django, é necessário configurar o protocolo Firmata.

1. **Instale o Arduino IDE:**

    Baixe e instale o Arduino IDE a partir do [site oficial](https://www.arduino.cc/en/software).

2. **Configure o Arduino com o protocolo Firmata:**

    1. Abra o Arduino IDE.
    2. Vá para **Sketch > Include Library > Manage Libraries**.
    3. Pesquise por "Firmata" e instale a biblioteca "Firmata".
    4. Com a biblioteca Firmata instalada, vá para **File > Examples > Firmata > StandardFirmata**.
    5. Selecione a porta correta do Arduino em **Tools > Port**.
    6. Selecione a placa correta em **Tools > Board**.
    7. Carregue o código no Arduino clicando no botão de upload (seta para a direita).

    Agora o Arduino está pronto para se comunicar com o Django através do protocolo Firmata.

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie um ambiente virtual:**

    ```bash
    python3 -m venv venv
    ```

3. **Ative o ambiente virtual:**

    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```
1. **Instale o MySQL:**

   Se você ainda não tem o MySQL instalado, siga as instruções na [documentação oficial do MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/).

2. **Acesse o MySQL como administrador:**

    ```bash
    mysql -u root -p
    ```

3. **Crie o banco de dados e o usuário:**

    No terminal do MySQL, execute os seguintes comandos:

    ```sql
    CREATE DATABASE nome_do_banco;
    CREATE USER 'seu_usuario'@'localhost' IDENTIFIED BY 'sua_senha';
    GRANT ALL PRIVILEGES ON nome_do_banco.* TO 'seu_usuario'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;
    ```

4. **Configure o banco de dados no Django:**

    No arquivo `settings.py`, adicione a configuração do banco de dados MySQL:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nome_do_banco',
            'USER': 'seu_usuario',
            'PASSWORD': 'sua_senha',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```



2. **Configure o banco de dados no Django:**

    No arquivo `settings.py`, adicione a configuração do banco de dados:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nome_do_banco',
            'USER': 'seu_usuario',
            'PASSWORD': 'sua_senha',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

3. **Aplique as migrações:**

    ```bash
    python manage.py migrate
    ```

## Uso

1. **Inicie o servidor de desenvolvimento do Django:**

    ```bash
    python manage.py runserver
    ```

    O servidor estará disponível em `http://127.0.0.1:8000/estufa`.


## Executando o Script `sensors.py`

1. **Execute o script `sensors.py` para coletar dados de sensores:**

    ```bash
    python sensors.py
    ```
## Configuração do Arduino

Para que o Arduino possa se comunicar com o Django, é necessário configurar o protocolo Firmata.

1. **Instale o Arduino IDE:**

    Baixe e instale o Arduino IDE a partir do [site oficial](https://www.arduino.cc/en/software).

2. **Configure o Arduino com o protocolo Firmata:**

    1. Abra o Arduino IDE.
    2. Vá para **Sketch > Include Library > Manage Libraries**.
    3. Pesquise por "Firmata" e instale a biblioteca "Firmata".
    4. Com a biblioteca Firmata instalada, vá para **File > Examples > Firmata > StandardFirmata**.
    5. Selecione a porta correta do Arduino em **Tools > Port**.
    6. Selecione a placa correta em **Tools > Board**.
    7. Carregue o código no Arduino clicando no botão de upload (seta para a direita).

    Agora o Arduino está pronto para se comunicar com o Django através do protocolo Firmata.

## Ferramentas Adicionais

Este projeto utiliza:

- **Tailwind CSS:** Para estilização do frontend. Certifique-se de compilar os estilos após modificar os arquivos CSS.
- **Chart.js:** Para visualizações gráficas dinâmicas. As configurações estão no frontend, e os gráficos são renderizados com base nos dados fornecidos pelo backend.

