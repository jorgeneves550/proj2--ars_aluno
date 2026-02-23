
> Open this page at [https://jorgeneves550.github.io/proj2_ars_aluno/](https://jorgeneves550.github.io/proj2_ars_aluno/)


## Descrição do Projeto:
Este projeto consiste num sistema de resposta de audiência usando um Micro:bit para o professor e um Micro:bit
para cada aluno. O sistema funciona da seguinte forma: Sempre que um aluno quer intervir prime o botão A do
seu Micro:bit, esta ação ilumina o led da matriz de leds do professor correspondente a esse Micro:bit. Se o aluno
clicar no botão B anula a ação anterior. Simultaneamente ambas as ações mostram um ícone na matriz de leds do
Micro:bit do aluno sinalizando a ação correspondente (premir o botão A ou o botão B). O professor tem também a
possibilidade de selecionar um aluno aleatoriamente agitando o seu Micro:bit. Esta ação gera um número aleatório
que é enviado para os Micro:bit. O Micro:bit do aluno igual ao número gerado emite um som e mostra uma
imagem intermitente na matriz de led durante alguns instantes.

## Material utilizado
1 Micro:Bit + pilha para o professor
1 Micro:bit + pilha para cada aluno
Não existem ligações físicas entre os Micro:bit.
A transmissão é feita por rádio frequência.
Todos os microbit têm de estar na mesma frequência.

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/jorgeneves550/proj2_ars_aluno** and import

## Edit this project

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/jorgeneves550/proj2_ars_aluno** and click import

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
