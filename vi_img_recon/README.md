# OpenNEURO
## [Visual image reconstruction](https://openneuro.org/datasets/ds000255/versions/00002)

uploaded by Franklin Feingold on 2018-03-29 - over 2 years ago
神谷先生(京大)
#### Task
人間の被験者が12×12枚のちらつきパッチのコントラストベースの画像を見る

画像閲覧には2種類のタスク

(1)ランダム画像表示
(2)図形画像(幾何学的形状またはアルファベット文字)表示の2種類の画像表示

画像提示は各画像の提示の間に休憩を挟んだブロックデザインを使用

ランダム画像のパッチ提示では、画像は6秒間提示され、その後6秒間の休息が与えらた

図形画像の提示では、画像は12秒間提示され、その後12秒間の休息が与えられた

ランダム画像表示のデータを用いて復号化モデルの学習を行い、学習したモデルを図画像表示のデータを用いて評価