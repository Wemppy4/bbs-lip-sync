<div align="right">
  
[RU](https://github.com/Wemppy4/bbs-lip-sync#RU)
|
[EN](https://github.com/Wemppy4/bbs-lip-sync#EN)

</div>

<div align="center">
  
# Lip sync for BBS

</div>
<div align="center">
Автоматический лип синк для BBS / Automatic lip sync for BBS 

<span></span>
</div>

![logo](https://github.com/Wemppy4/bbs-lip-sync/blob/assets/image.png)

<div id="RU"></div>

------------

![RU](https://github.com/Wemppy4/bbs-lip-sync/blob/ed17924fb47fa6957c0ee0695f5088106e0da9fa/wemoikenru.png)

**[Видео туториал](https://www.youtube.com/watch?v=jwFRUr9OyUI), спасибо за это @dinspal**

## Первые шаги

### Mouth или Mouth RIG?

`Mouth` - Моделька, которая накладывается на лицо персонажа. Для анимации рта используются разные текстуры.

`Mouth RIG` - Полноценный риг рта, где можно двигать зубы язык и так далее. С помощью нее можно делать плавную анимацию рта но при этом этот вариант не настолько универсальный.

### Как сделать свои формы рта?

Если вы используете `Mouth` то просто нарисуйте свои текстурки с такими же именами как стандартные изображения

Если вы используете риг, вам нужно создать позы с названиями как в позах `Mouth RIG` и после этого файл `poses.json` в папке с моделью, переместить в папку скрипта

### Как использовать Mouth и Mouth RIG?
Сначала переместите папку `Mouth` или `Mouth RIG` в каталог моделей BBS.

#### Mouth
Если на вашем скине есть рот, уберите его. Скопируйте одно из изображений рта, и нарисуйте там свой вариант. Если рта нет изначально, пропустите этот шаг.
Прикрепите модель к кости `Head` вашего рига персонажа

#### Mouth RIG
Откройте `texture.png` в папке с ригом рта, и вместо существующего рта нарисуйте свой. Если на вашем скине нет рта, сотрите эти пиксели.

![mouth rig](https://github.com/Wemppy4/bbs-lip-sync/blob/e4c1f94f67cc57c1bb4de155b3d924b2ba63fb9a/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-02%20174351.png)

## Установка Python и зависемостей
Для начала вам нужно установить Python. [Ссылка](https://www.python.org/)

**Убедитесь что вы нажали вот эти галочки**

![python](https://github.com/Wemppy4/bbs-lip-sync/blob/assets/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-02-17%20155744.png)

Далее, вам нужно установить ffmpeg, но если вы используете BBS мод, то скорее всего он у вас уже установлен.

**Убедитесь что ffmpeg есть в переменной окружения PATH** 
[Как это сделать](https://chatgpt.com/share/67b34ff9-5f24-800b-9588-e677f17eb334)

Далее, установите нужные библиотеки. Для этого напишите в коносоль поочерёдно следующие строки:

`pip install vosk`

`pip install wave`

`pip install configparser`

Если вы **НЕ** используете Windows, вам нужно будет установить еще tkinter

## Скачивание моделей VOSK
Скачайте модельку на [этом сайте](https://alphacephei.com/vosk/models)

Рекомендую скачивать small модельки. Обычная версия у меня даже не подгурзилась из-за своего веса.

Разархивируйте папку из архива и переместите ее в удобное вам место

> Скрипт подерживает только русский и английский язык

## Настройка скрипта
Перейдите обратно в папку с скриптом, и запустите `config.ini` нажав `ПКМ -> Редактировать`

Давайте посмотрим параметры в конфиге:
- **model_path** - Путь к модели. Если модель лежит в той же папке что и скрипт, просто напишите имя скрипта
- **mouth_shapes_path** - Путь к изображениям рта. Если вы хотите использовать пиксельную версию, оставьте параметр по умолчанию.
- **output_path** - Путь куда будет сохранятся выходной `.json` файл. (Для удобства можете написать папку пресетов кейфреймов BBS)

## Использование скрипта

После того как вы сделали все предыдущие шаги, время сделать самое вкусное!

Запустите `start.bat` если вы используете `Mouth`
Запустите `start_smooth.gbat` если вы используете `Mouth RIG` или свой риг рта.

Если вы используете `Mouth`, через некоторое время у вас попросят написать название базовой формы рта. Напишите название изображение (без .png)
> Базовая фортма рта - изображение, которое будет использоваться во время того как персонаж молчит.

Если на вашем скине нет рта, напишите `empty`
Если на вашем скине нет рта и вы используете HD текстурки, напишите `Normal` или `empty`

После того, как окно закрылось, в выходной папке должен появиться`.json` файл

## Использование .json файла в BBS

Последнее, что вам нужно сделать.

Зайдите в свой фильм в BBS, наведитесь мышкой на любой дорожку кейфреймов и нажмите `ПКМ`. Дальше нажмите на икноку пресетов. У вас откроется менюшка в которой ван нужно нажать на иконку папки справа. После этого закройте эту менюшку.

В папку которая у вас открылась, переместите свой `.json` файл.

Для `Mouth`. Наведитесь на дорожку `texture` вашей **модели рта**, убедитесь что ваш курсор находится на тике где начинается ваше аудио. Нажмите `ПКМ` и нажмите на кнопку пресетов. Выберите пресет который вы только что перенесли.

Для `Mouth RIG`. Наведитесь на дорожку `pose` вашей **модели рта**, убедитесь что ваш курсор находится на тике где начинается ваше аудио. Нажмите `ПКМ` и нажмите на кнопку пресетов. Выберите пресет который вы только что перенесли.

Рекомендую удалять`.json` файлы которые вы уже использовали

## Отдельная благодарность

Благодарю великодушный DeepSeek и ChatGPT, которые помогли мне в создании данного скрипта.

Благодарю добродушного МакХорса, который создал BBS мод!

<div id="EN"></div>

------------

![EN](https://github.com/Wemppy4/bbs-lip-sync/blob/ed17924fb47fa6957c0ee0695f5088106e0da9fa/wemoiken.png)

The translation may not be accurate in some places. I do not speak English, so I translate via DeepL.

## First steps

### Mouth or Mouth RIG?

`Mouth` - A model that is superimposed on a character's face. Different textures are used to animate the mouth.

`Mouth RIG` - A full-fledged mouth rig where you can move the teeth tongue and so on. It can be used to make smooth mouth animation but this option is not that versatile.

### How do I make my own mouth shapes?

If you are using `Mouth` then just draw your own textures with the same names as the standard images

If you are using a rig, you need to create poses with names like `Mouth RIG` poses and then move the `poses.json` file in the model folder to the script folder.

### How to use Mouth and Mouth RIG?
First, move the `Mouth` or `Mouth RIG` folder to the BBS model directory.

#### Mouth
If your skin has a mouth on it, remove it. Copy one of the mouth images, and draw your own version there. If there is no mouth originally, skip this step.
Attach the model to the `Head' bone of your character's rig

#### Mouth RIG.
Open `texture.png` in the folder with the mouth rig, and draw your own mouth in place of the existing mouth. If your skin doesn't have a mouth, erase those pixels.

![mouth rig](https://github.com/Wemppy4/bbs-lip-sync/blob/e4c1f94f67cc57c1bb4de155b3d924b2ba63fb9a/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-02%20174351.png)

## Installing Python and dependencies
First you need to install Python. [Link](https://www.python.org/).

**Make sure you click these checkboxes**

![python](https://github.com/Wemppy4/bbs-lip-sync/blob/assets/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-02-17%20155744.png)

Next, you need to install ffmpeg, but if you are using the BBS mod, you probably already have it installed.

**Make sure ffmpeg is in the PATH environment variable** 
[How you can do this](https://chatgpt.com/share/67b34ff9-5f24-800b-9588-e677f17eb334)

Next, install the libraries you need. To do this, write the following lines alternately in conosol:

`pip install vosk`

`pip install wave`

`pip install configparser`

If you are **NOT** using Windows, you will need to install tkinter as well

## Download VOSK models
Download a model from [this site](https://alphacephei.com/vosk/models).

I recommend downloading small models. I didn't even get the regular version because of its weight.

Unzip the folder from the archive and move it to a convenient place for you.

> Script supports only Russian and English language

## Customise the script
Go back to the folder with the script, and run `config.ini` by pressing `CM -> Edit`.

Let`s look at the parameters in the config:
- **model_path** - The path to the model. If the model is in the same folder as the script, just write the name of the script
- **mouth_shapes_path** - Path to the mouth images. If you want to use the pixel version, leave the default.
- **output_path** - Path where the output `.json` file will be saved. (For convenience you can write a folder of BBS keyframe presets).

## Using the script

After you've done all the previous steps, it's time to do the most delicious thing!

Run `start.bat` if you are using `Mouth`.
Run `start_smooth.gbat` if you are using `Mouth RIG` or your mouth rig.

If you are using `Mouth`, after a while you will be asked to write the name of the base mouth shape. Write the name of the image (no .png)
> The base mouth form is the image that will be used while the character is silent.

If your skin doesn't have a mouth, write `empty`
If your skin does not have a mouth and you are using HD textures, write `Normal` or `empty`.

After the window has closed, there should be a `.json` file in the output folder.

## Using a .json file in a BBS

The last thing you need to do.

Go to your movie in BBS, hover your mouse over any keyframe track and press `KM`. Next, click on the presets icon. This will open a menu where you need to click on the folder icon on the right. After that close this menu.

In the folder you have opened, move your `.json` file.

For `Mouth`. Hover over the `texture` track of your **model mouth**, make sure your cursor is on the tick where your audio starts. Press `KMouth` and click on the presets button. Select the preset you just transferred.

For `Mouth RIG`. Hover over the `pose` track of your **mouth model**, make sure your cursor is on the tick where your audio starts. Press `PM` and click on the presets button. Select the preset you just transferred.

I recommend deleting `.json` files that you have already used

## Special thanks

Thank you to the generous DeepSeek and ChatGPT who helped me in creating this script.

Thanks to good-natured McHorse who created the BBS mod!
