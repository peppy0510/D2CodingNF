## D2CodingNF

* [D2Coding](https://github.com/naver/d2-coding-font) 1.4.0에 Nerd Font 아이콘을 넣은 고정폭 글꼴입니다.

    * 한 파일로 GDI(메모장 등)와 DirectWrite(Windows Terminal, Sublime Text 등) 클라이언트 모두에서 한글이 영문의 정확히 2배 폭으로 출력됩니다.
    * 아이콘 하단 쏠림을 줄 높이 조정으로 바로잡았습니다.
    * 0을 점 0으로 바꾸려면 `cv01`(또는 `ss01`) 기능을 켭니다. 예: Windows Terminal `"font": { "features": { "cv01": 1 } }`
    * Windows에서 검증하였습니다.

* 기존 `D2CodingNF`, `D2CodingNFX`를 제거하고 다음의 파일을 설치하면 됩니다. Regular와 Bold는 별도 파일입니다.

    * Regular: `D2CodingNF-Ver1.4.0-20261003.ttf`
    * Bold: `D2CodingNF-Bold-Ver1.4.0-20261003.ttf`
    * 1.3.2의 `D2CodingNFX`는 더 이상 필요하지 않습니다. 쓰던 곳은 `D2CodingNF`로 바꿉니다.

* 직접 제작하기 위해서는 다음과 같이 `patcher.py`와 `postprocess.py`를 사용합니다.

    * [Nerd Font 공식 저장소에 있는 patcher](https://github.com/ryanoasis/nerd-fonts/blob/master/font-patcher)를 바탕으로 원본 글폭(한글, 한자 2칸)을 그대로 두도록 고쳤습니다.
    * `postprocess.py`는 FontForge가 바꾼 고정폭 표시(`post.isFixedPitch`)와 평균 글자폭(`OS/2.xAvgCharWidth`)을 원본 값으로 되돌리고, Bold를 `D2CodingNF` 패밀리로 묶습니다. GDI는 2칸 문자를 평균 글자폭의 2배로 배치하므로 이 값이 틀리면 한글 자간이 벌어집니다.
    * `fontforge`와 `fonttools`가 설치되어 있어야 합니다. WSL에서의 빌드를 권장합니다.
    * Bold는 `D2CodingBold-Ver1.4.0-20261003.ttf`로 같은 명령을 실행합니다.

    ```bash
    apt install fontforge python3-fonttools
    ```

    ```bash
    fontforge -script patcher.py "D2Coding-Ver1.4.0-20261003.ttf" --windows --complete --careful --postprocess ./postprocess.py --removeligatures --adjust-line-height --glyphdir "glyphs/" --outputdir "output/" --extension "ttf" --quiet --no-progressbars --use-single-width-glyphs
    ```

* D2Coding은 [SIL Open Font License 1.1](OFL.txt)을 따릅니다.
