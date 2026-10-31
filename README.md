## D2CodingNF

[D2Coding](https://github.com/naver/d2-coding-font) 1.4.0에 [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) 아이콘을 넣은 글꼴입니다.

* 한글과 한자는 원본처럼 2칸, 아이콘은 1칸 폭입니다.
* 고정폭 표시와 평균 글자폭을 원본 값으로 유지해서, GDI 방식 클라이언트에서도 한글 자간이 벌어지지 않습니다.
* `cv01`(또는 `ss01`) 기능을 켜면 0이 점 0으로 바뀝니다.

### 파일

* Regular: `D2CodingNF-Ver1.4.0-20261003.ttf`
* Bold: `D2CodingNF-Bold-Ver1.4.0-20261003.ttf`

### 빌드

* `original/`의 D2Coding 원본을 패치해서 `output/`에 결과를 만듭니다. 배포 파일은 그 결과를 루트에 둔 것입니다.
* `patcher.py`는 [Nerd Fonts의 font-patcher](https://github.com/ryanoasis/nerd-fonts/blob/master/font-patcher)를 원본 글폭을 유지하도록 고친 것입니다.
* `postprocess.py`는 FontForge가 바꾼 고정폭 표시(`post.isFixedPitch`)와 평균 글자폭(`OS/2.xAvgCharWidth`)을 원본 값으로 되돌리고, Bold를 `D2CodingNF` 패밀리로 묶습니다.

```bash
apt install fontforge python3-fonttools
```

```bash
fontforge -script patcher.py "original/D2Coding-Ver1.4.0-20261003.ttf" --windows --complete --careful --postprocess ./postprocess.py --removeligatures --adjust-line-height --glyphdir "glyphs/" --outputdir "output/" --extension "ttf" --quiet --no-progressbars --use-single-width-glyphs
fontforge -script patcher.py "original/D2CodingBold-Ver1.4.0-20261003.ttf" --windows --complete --careful --postprocess ./postprocess.py --removeligatures --adjust-line-height --glyphdir "glyphs/" --outputdir "output/" --extension "ttf" --quiet --no-progressbars --use-single-width-glyphs
```

### 라이선스

D2Coding은 [SIL Open Font License 1.1](OFL.txt)을 따릅니다.
