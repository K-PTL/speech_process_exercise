#!/usr/bin/env python3

""" 音声情報処理 n本ノック !! """

# Copyright (C) 2020 by Akira TAMAMORI

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Commentary:
# - PySoxを用いた音声情報処理シリーズ
# - stereo から mono に変換

import sox

IN_WAVE_FILE = "stereo.wav"          # ステレオ音声
OUT_WAVE_FILE = "out.wav"           # モノラル音声

# create trasnformer (単一ファイルに対する重ねがけ)
transformer = sox.Transformer()

# ステレオをモノラルに
transformer.convert(n_channels=1)
transformer.build(IN_WAVE_FILE, OUT_WAVE_FILE)
