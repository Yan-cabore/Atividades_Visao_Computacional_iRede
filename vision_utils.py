"""Módulo utilitário com funções de apoio para manipulação de imagens
com OpenCV e Matplotlib."""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class VisionUtils:
    """Conjunto de métodos utilitários para leitura, conversão e
    exibição de imagens em figuras do Matplotlib."""

    def ler_imagens(self, img_list: list) -> list:
        """Lê uma lista de caminhos de imagens e as converte em
        arrays (usando cv.imread)."""
        for i in range(len(img_list)):
            img_list[i] = cv.imread(img_list[i])
        return img_list

    def converter_bgr(self, img_list: list) -> list:
        """Converte uma lista de imagens de BGR para RGB."""
        for i in range(len(img_list)):
            img_list[i] = cv.cvtColor(img_list[i], cv.COLOR_BGR2RGB)
        return img_list

    def criar_figure(self, fig_name, axes_x, axes_y, fig_size):
        """Cria uma figure com o título e o layout de eixos
        especificados. Retorna axes 1D ou 2D, a depender de
        axes_x e axes_y."""
        fig, ax = plt.subplots(axes_x, axes_y, figsize=fig_size)
        fig.suptitle(fig_name)
        fig.tight_layout()
        return fig, ax

    def preencher_figure(self, axe, img_list: list, cmap=None):
        """Preenche uma lista 1D de axes com as imagens fornecidas.

        Observação: este método é projetado para axes 1D. Para axes
        2D, é necessário iterar com .flatten() ou acessar axe[i, j].
        """
        for i, ax in enumerate(axe):
            ax.imshow(img_list[i], cmap=cmap)

    def nomear_axes(self, axe, names: list):
        """Nomeia cada um dos axes com o título correspondente."""
        for i, ax in enumerate(axe):
            ax.set_title(names[i])

    def remover_axis(self, axe):
        """Remove os eixos (axis) de cada axe da figure."""
        for a in axe:
            a.axis('off')

    def adicionar_imagem(self, axe, img):
        """Adiciona uma imagem ao primeiro axe vazio encontrado."""
        for ax in axe:
            if not ax.has_data():
                ax.imshow(img)
                break

    def qtd_gray(self, imgs: list) -> list:
        """Conta a quantidade de níveis de cinza únicos em cada
        imagem da lista."""
        imgs_gray = [cv.cvtColor(img, cv.COLOR_RGB2GRAY) for img in imgs]

        qtds = []
        for img_gray in imgs_gray:
            qtds.append(len(np.unique(img_gray)))

        return qtds
