# Lip sync for BBS
Автоматический лип синк для BBS / Automatic lip sync for BBS 

[VT](https://www.virustotal.com/gui/file/e1f087e381339ab8a82b48366162d3dd6bbb85e0bff45b430868eb63a7073e35 "VT")

[RU](https://github.com/Wemppy4/bbs-lip-sync/blob/main/README.md#ru)

[EN](https://github.com/Wemppy4/bbs-lip-sync/blob/main/README.md#en)

## RU
## Первые шаги
Сначала переместите папку Mouth в каталог моделей BBS.

Затем удалите рот со своего скина и нарисуйте его отдельно. Скопируйте одну из форм рта и создайте свой вариант. Если рта нет изначально, пропустите этот шаг.

## Установка Python и зависемостей
Для начала вам нужно установить Python. [Ссылка](https://www.python.org/)

Далее, вам нужно установить ffmpeg, но если вы используете BBS мод, то скорее всего он у вас уже установлен.

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
- **mouth_model_index** - Индекс положения модели рта. [Изображение для большей ясности](https://imgur.com/a/W6VpWB7)

## Использование скрипта

После того как вы сделали все предыдущие шаги, время сделать самое вкусное!
Запустите `start.bat`

Через некоторое время, у вас попросят написать название базовой формы рта. Напишите название изображение (без .png)
> Базовая фортма рта - изображение, которое будет использоваться во время того как персонаж молчит.

Если на вашем скине нет рта, напишите`empty`
Если на вашем скине нет рта и вы используете HD текстурки, напишите`Normal`

После того, как окно закрылось, в выходной папке должен появиться`.json` файл

## Использование .json файла в BBS

Последнее, что вам нужно сделать.

Откройте свой фильм в BBS. Найдите дорожку`texture` **модели рта**. Наведите курсор в место где находиться начало вашего аудио. Кликните ПКМ по этому месту, и нажмите на иконку пресетов. У вас откроется окно с пресетами, справа от него должна быть иконка папки, нажмите на нее и переместите`.json` файл в эту папку. Если в окне пресетов не появился этот файл, закройте это окно и откройте его снова. 

Рекомендую удалять`.json` файлы которые вы уже использовали

## Отдельная благодарность

Благодарю великодушный DeepSeek и ChatGPT, которые помогли мне в создании данного скрипта.

Благодарю добродушного МакХорса, который создал BBS мод!

## EN
The translation may not be accurate in some places. I do not speak English, so I translate via DeepL.

## First Steps
First, move the Mouth folder to the BBS model directory.

Then remove the mouth from your skin and draw it separately. Copy one of the mouth shapes and create your own version. If there is no mouth originally, skip this step.

## Installing Python and dependencies
First you need to install Python. [Link](https://www.python.org/).

Next, you need to install ffmpeg, but if you are using the BBS mod, you probably already have it installed.

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
- **mouth_model_index** - Index of mouth model position. [Image for clarity](https://imgur.com/a/W6VpWB7)

## Using the script

Once you've done all the previous steps, it's time to do the most delicious part!
Run `start.bat`.

After a while, you will be asked to write the name of the base mouth shape. Write the name of the image (no .png)
> The base mouth form is the image that will be used while the character is silent.

If your skin does not have a mouth, write `empty`.
If your skin does not have a mouth and you are using HD textures, write `Normal`.

After the window has closed, you should see a .json file in the output folder.

## Using a .json file in a BBS.

The last thing you need to do.

Open your film in BBS. Find the `texture` track of the **model mouth**. Place your cursor where the beginning of your audio is. Click on that location and click on the presets icon. The presets window will open, to the right of it there should be a folder icon, click on it and move the `.json` file to this folder. If this file does not appear in the presets window, close this window and open it again. 

I recommend deleting `.json` files that you have already used.

## Special thanks

Thank you to the generous DeepSeek and ChatGPT who helped me in creating this script.

Thanks to good-natured McHorse who created the BBS mod!
