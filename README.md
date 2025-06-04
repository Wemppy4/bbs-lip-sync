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

![logo](https://github.com/Wemppy4/bbs-lip-sync/blob/43b6e58f26a4dcc741542f3eef17057840005314/auo%20lip%20sync%201.2.png)

<div id="RU"></div>

------------

![RU](https://github.com/Wemppy4/bbs-lip-sync/blob/ed17924fb47fa6957c0ee0695f5088106e0da9fa/wemoikenru.png)

**[Видео туториал](https://www.youtube.com/watch?v=jwFRUr9OyUI), спасибо за это @dinspal**
> Видео было записано для старой версии, поэтому возможны неточности

## Первые шаги

### Как использовать Mouth и Mouth RIG?
В папке `bbs_models/` есть риги, которые совместимы с авто липсинком. Переместите нужный риг в каталог моделей BBS.

### Mouth или Mouth RIG?

`Mouth` - Моделька, которая накладывается на лицо персонажа. Для анимации рта используются разные текстуры.

`Mouth RIG` - Полноценный риг рта, где можно двигать зубы язык и так далее. С помощью нее можно делать плавную анимацию рта но при этом этот вариант не настолько универсальный. Для анимации рта используются разные позы.

### Как сделать свои формы рта?

Если вы используете `Mouth` то просто нарисуйте свои текстурки с такими же именами как стандартные изображения

Если вы используете риг, вам нужно создать позы с названиями как в позах `Mouth RIG` и после этого файл `poses.json` в папке с моделью, переместить в папку `json_files/`

### Настройка рига под вашего персонажа
#### Mouth 
Если на вашем скине есть рот, уберите его. Скопируйте одно из изображений рта, и нарисуйте там свой вариант. Если рта нет изначально, пропустите этот шаг.
Прикрепите модель к кости `Head` вашего рига персонажа

#### Mouth RIG
Откройте `texture.png` в папке с ригом рта, и вместо существующего рта нарисуйте свой. Если на вашем скине нет рта, сотрите эти пиксели.

![mouth rig](https://github.com/Wemppy4/bbs-lip-sync/blob/d8d3db6b76af12108f864e7dc5d3bfeac0905084/mouth%20rig%20texture%20(1.2).png)

## Установка Python и зависемостей
Для начала вам нужно установить Python. [Ссылка](https://www.python.org/)

**Убедитесь что вы нажали вот эти галочки**

![python](https://github.com/Wemppy4/bbs-lip-sync/blob/assets/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-02-17%20155744.png)

Далее, вам нужно установить ffmpeg, но если вы используете BBS мод, то скорее всего он у вас уже установлен.

**Убедитесь что ffmpeg есть в переменной окружения PATH** 
[Как это сделать](https://chatgpt.com/share/67b34ff9-5f24-800b-9588-e677f17eb334)

Далее, установите нужные библиотеки. Для этого напишите в консоль поочерёдно следующие строки:

`pip install vosk`

`pip install wave`

`pip install configparser`

Если вы **НЕ** используете Windows, вам нужно будет установить еще `tkinter`

## Скачивание моделей VOSK
Скачайте модельку на [этом сайте](https://alphacephei.com/vosk/models)

Рекомендую скачивать small модельки. Обычная версия у меня даже не подгурзилась из-за своего веса.

Разархивируйте папку из архива и переместите ее в `vosk_models/`

> Скрипт поддерживает только те языки, для которых есть карта губ в `json_files/maps/`

## Настройка скрипта
Перейдите обратно в папку со скриптом, и запустите `config.ini`

Давайте посмотрим параметры в конфиге:
- **model_path** - Путь к модели Vosk
- **mouth_shapes_path** - Путь к изображениям рта. Если вы хотите использовать пиксельную версию, оставьте параметр по умолчанию
- **output_path** - Путь куда будет сохранятся выходной `.json` файл. (Для удобства можете написать папку пресетов кейфреймов BBS. Не забудьте `/` в конце)
- **language** - Язык, должен называться так же как карта губ для него в `json_files/maps/` (ru, en, ua и т.д.)

## Использование скрипта

После того как вы сделали все предыдущие шаги, время сделать самое вкусное!

Запустите `start.bat` если вам нужны кейфреймы для **текстуры** (`Mouth`)

Запустите `start_smooth.bat` если вам нужны кейфремы для **позы** (`Mouth RIG`)

Если вы используете `Mouth`, через некоторое время у вас попросят написать название базовой формы рта. Напишите название изображение (без .png)
> Базовая фортма рта - изображение, которое будет использоваться во время того как персонаж молчит.

Если на вашем скине нет рта, напишите `empty`
Если на вашем скине нет рта и вы используете HD текстурки, напишите `Normal` или `empty`

После того, как окно закрылось, в выходной папке должен появиться`.json` файл

## Использование .json файла в BBS

Последнее, что вам нужно сделать.

Зайдите в свой фильм в BBS, наведитесь мышкой на любой дорожку кейфреймов и нажмите `ПКМ`. Дальше нажмите на икноку пресетов. У вас откроется менюшка в которой вам нужно нажать на иконку папки справа. После этого закройте эту менюшку.

В папку которая у вас открылась, переместите свой `.json` файл.

Наведитесь на нужную дорожку кейфреймов (**texture** или **pose**). Убедитесь что ваш курсор находится на тике где начинается ваше аудио. Нажмите `ПКМ` и нажмите на кнопку пресетов. Выберите пресет который вы только что перенесли.

> Рекомендую удалять`.json` файлы которые вы уже использовали

## Дополнительная информация

Вы можете добавлять поддержку других языков. Для этого в папке `json_files/maps/` создайте новый `.json` файл, где напишите какая форма рта будет использоваться под **каждую** букву в вашем языке

## Отдельная благодарность

Благодарю великодушный DeepSeek и ChatGPT, которые помогли мне в создании данного скрипта.

Благодарю добродушного [МакХорса](https://github.com/mchorse), который создал BBS мод!


<div id="EN"></div>

------------

![EN](https://github.com/Wemppy4/bbs-lip-sync/blob/ed17924fb47fa6957c0ee0695f5088106e0da9fa/wemoiken.png)

## Getting Started

### How to use Mouth and Mouth RIG?
Inside the `bbs_models/` folder, you’ll find rigs compatible with auto lip sync. Move the desired rig into your BBS models directory.

### Mouth or Mouth RIG?

`Mouth` – A model applied on the character's face. Different textures are used for mouth animation.

`Mouth RIG` – A full mouth rig where you can move the teeth, tongue, etc. It allows smooth animation, but it’s less universal. Poses are used for animation here.

### How to create your own mouth shapes?

If you are using `Mouth`, just draw your own textures with the same names as the default images.

If you are using a rig, you need to create poses with the same names as in the `Mouth RIG` poses and then move the `poses.json` file into the `json_files/` folder.

### Adjusting the rig to your character
#### Mouth 
If your skin has a mouth, remove it. Copy one of the mouth images and draw your own variant. If there's no mouth initially, skip this step.  
Attach the model to the `Head` bone of your character's rig.

#### Mouth RIG
Open `texture.png` in the mouth rig folder, and draw your own mouth over the existing one. If your skin doesn’t have a mouth, erase those pixels.

![mouth rig](https://github.com/Wemppy4/bbs-lip-sync/blob/d8d3db6b76af12108f864e7dc5d3bfeac0905084/mouth%20rig%20texture%20(1.2).png)

## Installing Python and Dependencies
First, install Python from [this link](https://www.python.org/)

**Make sure you check these boxes**

![python](https://github.com/Wemppy4/bbs-lip-sync/blob/assets/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-02-17%20155744.png)

Next, install `ffmpeg`, but if you're using the BBS mod, it is likely already installed.

**Make sure `ffmpeg` is in your PATH environment variable**  
[How to do this](https://chatgpt.com/share/67b34ff9-5f24-800b-9588-e677f17eb334)

Now, install the necessary libraries. Type the following commands one by one in your terminal:

`pip install vosk`

`pip install wave`

`pip install configparser`

If you are **NOT** using Windows, you also need to install `tkinter`

## Downloading VOSK Models
Download a model from [this website](https://alphacephei.com/vosk/models)

I recommend downloading the small models. The regular version didn’t even load for me due to its size.

Unzip the downloaded folder and move it to `vosk_models/`

> The script supports only those languages that have a mouth map in `json_files/maps/`

## Script Configuration
Go back to the folder with the script and open `config.ini`

Let’s look at the config parameters:
- **model_path** – Path to the Vosk model
- **mouth_shapes_path** – Path to mouth images. If you want to use the pixel version, leave the default path
- **output_path** – Path where the output `.json` file will be saved (for convenience, you can use the BBS keyframe presets folder; don’t forget the trailing `/`)
- **language** – Language name, must match the name of the mouth map in `json_files/maps/` (ru, en, ua, etc.)

## Using the Script

After completing the previous steps, it's time for the main part!

Run `start.bat` if you need keyframes for **textures** (`Mouth`)

Run `start_smooth.bat` if you need keyframes for **poses** (`Mouth RIG`)

If you’re using `Mouth`, after a while, you'll be asked to enter the name of the base mouth shape. Enter the image name (without `.png`)
> Base mouth shape – the image used when the character is silent.

If your skin has no mouth, type `empty`  
If your skin has no mouth and you're using HD textures, type `Normal` or `empty`

Once the window closes, a `.json` file should appear in the output folder.

## Using the `.json` File in BBS

The final step.

Open your movie in BBS, hover over any keyframe track and right-click. Then click the preset icon. A menu will open – click the folder icon on the right. Then close the menu.

In the opened folder, move your `.json` file.

Hover over the desired keyframe track (**texture** or **pose**). Make sure your cursor is on the tick where the audio starts. Right-click and press the preset button. Select the preset you just added.

> I recommend deleting `.json` files you’ve already used

## Additional Information

You can add support for other languages. To do this, create a new `.json` file in `json_files/maps/` and specify which mouth shape corresponds to **each** letter in your language.

## Special Thanks

Thanks to the generous DeepSeek and ChatGPT who helped me create this script.

Special thanks to the kind [McHorse](https://github.com/mchorse) who created the BBS mod!
