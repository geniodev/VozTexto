# VozTexto
![](https://github.com/geniodev/VozTexto/blob/main/speech.png?raw=true)</br>
&nbsp;
*Voz para Texto, Texto para Voz Usando Google Speech*</br>
&nbsp;
Biblioteca para interação de Voz para Texto ou de Texto para Voz</br>

&nbsp;
&nbsp;

*Índices*
&nbsp;
- <a href="https://github.com/geniodev/VozTexto#voztexto" target="_self">Inicio</a>
- <a href='https://github.com/geniodev/VozTexto#bibliotecas-instalar' target='_self'>Bibliotecas Install</a>
- <a href='https://github.com/geniodev/VozTexto#documenta%C3%A7%C3%A3o---f%C3%B3rmulas' target='_self'>Documentação</a>
  - <a href='https://github.com/geniodev/VozTexto#remove-acentos-das-strings-inseridas-no-txt' target='_self'>Remove acentos das strings inseridas no 'txt'</a>
    - <a href='txt' target='_self'>remover_acentos(txt)</a>
  - <a href='https://github.com/geniodev/VozTexto#ouvi-a-fala-de-voz-e-retorna-o-texto-sem-acentos' target='_self'>Ouvi a fala de voz e retorna o texto sem acentos</a>
    - <a href='' target='_self'>ListenWorkd()</a>
  - <a href='https://github.com/geniodev/VozTexto#fala-a-hora-atual-e-minutos' target='_self'>Fala a hora Atual e minutos</a>
    - <a href='' target='_self'>Falarhora()</a>
  - <a href='https://github.com/geniodev/VozTexto#voz-para-texto' target='_self'>Voz para Texto</a>
    - <a href='' target='_self'>OuvirFala()</a>
  - <a href='https://github.com/geniodev/VozTexto#texto-para-voz' target='_self'>Texto para Voz</a>
    - <a href='falaragora' target='_self'>falag(falaragora)</a>





&nbsp;
&nbsp;
<h1 id="install">Bibliotecas Instalar</h1></br>

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install gTTS
pip install playsound
```

*Padrões, mas caso não tenha, deve instalar*
```bash
pip install DateTime
pip install unicodedata
```
*Somente para versão 3.5/3.6, sem ele os audios não funcionam, é necessário instalar esta biblioteca abaixo.*
```bash
pip install PyAudio
```
&nbsp;
# Documentação - Fórmulas:</br>

#### Remove acentos das strings inseridas no 'txt'
> `remover_acentos(txt)`

#### Ouvi a fala de voz e retorna o texto sem acentos
> `ListenWorkd()`

#### Fala a hora Atual e minutos
> `Falarhora()`

#### Voz para Texto
Ouvi a Fala e retorna o que foi dito em textos sem acentos e em letras minúsculas
> `OuvirFala()`

#### Texto para Voz
###### Cria uma fala usando texto digitado.
###### falaragora: Texto a ser falado STR
> `falag(falaragora)`


<h1>Heading level 1</h1>

- Alguma coisa
  - teste []()
    - teste





**Índices**

[TOCM]

[TOC]



&nbsp;
&nbsp;
Desenvolvedor: RA (Ricardo Andrade)
Versão: 3.0.0 Final
