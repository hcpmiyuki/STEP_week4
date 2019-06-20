# STEP_week4
## Please run "git clone https://github.com/hcpmiyuki/STEP_week4.git"

## HW1
+ Run "python3 sns_links/breadth_first_search.py" or "python3 sns_links/depth_first_search.py" and input your nickname! Then you can detect the number of steps from you to jacob(shima-san).

## HW2
+ Please download some pickle_files from https://drive.google.com/file/d/1SarCevf6IZUQex0ETBHLPxzLdmKR3cu8/view?usp=sharing.
+ And put them in "wikipedia_links".
+ Finally, run "python3 wikipedia_links/wiki_game.py".

### Rule
+ this is a game that you should try to make steps from start_word to end_word: A <= steps <= B.
+ ...英語がとても苦手なので日本語で説明します。これはstart_wordからend_wordまでのステップ数が範囲内に収まるようにするゲームです。
+ 範囲というのは最初は0以上1000000以下でそれ以降は＜前のターンのステップ数＞以上＜前のターンのステップ数*10＞以下となります。
+ 初めのターンではstart_wordはランダムに選ばれてend_wordは自分で入力します。次のターンでは前のターンでend_wordだったものがstart_wordになり、またend_wordを入力します。(しりとりみたいな感じです)
+ 処理に時間がかかりますが、気長にお待ちください:)
