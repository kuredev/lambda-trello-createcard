# 概要
チェックリスト付きのTrelloのカードを生成する

# 使い方
- data.yaml.sampleをdata.yamlにリネームし、各キーやチェックリスト等を記載する
-- チェックリストに記載される名前はTrelloのユーザ名となる
-- 各キーは http://qiita.com/kure/items/04503b1082c9fb81fccf 等にTipあり
- 環境変数ENV（PROD or DEV）でプロダクション環境と開発環境を切り替え可能
- Lambdaにアップロード、ハンドラは「index.lambda_handler」
- 必要なライブラリは適宜pipでインストールすること
- Python 2.7で確認


