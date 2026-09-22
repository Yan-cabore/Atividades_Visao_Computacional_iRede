# Atividades_Visao_Computacional

Repositório com as atividades práticas e projetos desenvolvidos durante o curso de Visão Computacional do Instituto iRede.

## 👤 Autor

**Carlos Yan Matos Ferreira**
Engenharia de Computação — Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE)

## 📖 Sobre o repositório

Este repositório reúne os exercícios, atividades e projetos desenvolvidos ao longo do curso de Visão Computacional oferecido pelo Instituto iRede, cobrindo tópicos como processamento de imagens, detecção de objetos, segmentação e demais técnicas aplicadas de visão computacional.

## 📁 Estrutura

```
.
├── atividades/       # Exercícios e atividades práticas do curso
├── projetos/         # Projetos maiores desenvolvidos ao longo do curso
├── datasets/         # Conjuntos de dados utilizados (ou instruções de download)
└── notebooks/        # Notebooks de estudo e experimentação
```

## 🛠️ Tecnologias

- Python
- OpenCV
- NumPy
- (adicionar demais bibliotecas conforme o curso avançar, ex: YOLO, TensorFlow, PyTorch)

## ▶️ Como executar

```bash
# Clonar o repositório
git clone https://github.com/<seu-usuario>/Atividades_Visao_Computacional.git
cd Atividades_Visao_Computacional

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

## 🧰 vision_utils.py

O repositório conta com um módulo utilitário (`vision_utils.py`), com a classe `Utils`, que centraliza funções reaproveitáveis usadas ao longo das atividades para manipulação e exibição de imagens com OpenCV e Matplotlib. Esse arquivo **será atualizado continuamente** conforme novos métodos forem necessários no decorrer do curso.

Métodos disponíveis atualmente:

- **`ler_imagens(img_list)`** — recebe uma lista de caminhos de imagens e as lê com `cv.imread`, retornando a lista já com os arrays carregados.
- **`converter_bgr(img_list)`** — converte uma lista de imagens do espaço de cor BGR (padrão do OpenCV) para RGB.
- **`criar_figure(fig_name, axes_x, axes_y, fig_size)`** — cria uma figure do Matplotlib com título e grade de eixos (`axes_x` x `axes_y`), aplicando `tight_layout` para um layout mais organizado. Retorna a figure e os axes.
- **`preencher_figure(axe, img_list, cmap=None)`** — preenche uma lista 1D de axes com as imagens correspondentes, usando um colormap opcional (útil para imagens em escala de cinza).
- **`nomear_axes(axe, names)`** — define o título de cada axe com base em uma lista de nomes.
- **`remover_axis(axe)`** — remove os eixos (marcações de linha/coluna) de cada axe da figure, deixando a exibição mais limpa.
- **`adicionar_imagem(axe, img)`** — adiciona uma imagem ao primeiro axe vazio encontrado (verificado via `has_data()`), útil para preencher axes um a um sem sobrescrever os já ocupados.
- **`qtd_gray(imgs)`** — converte cada imagem da lista para escala de cinza e retorna a quantidade de níveis de tom (valores únicos) presentes em cada uma.

## 📌 Status

🚧 Em desenvolvimento — atividades sendo adicionadas conforme o andamento do curso.

## 📄 Licença

Este projeto é de uso acadêmico, desenvolvido como parte do curso de Visão Computacional do Instituto iRede.
