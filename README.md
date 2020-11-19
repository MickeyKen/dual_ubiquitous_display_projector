#### 画像を上下で反転させる
    $ convert -flip input.jpg output.jpg

#### 画像を左右で反転させる
    $ convert -flop input.jpg output.jpg


#### 動画を左右上下で反転させる
    $ ffmpeg -i input.mov -vf hflip,vflip output.mov
