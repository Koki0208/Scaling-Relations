# ファイルを開いて読み取ります
with open('blockList.txt', 'r') as file:
    lines = file.readlines()

# チェーン全体ののブロック数をカウントする変数
data_count = 0
# Orphan の数をカウントする変数
orphan_count = 0
#ブロック数 *結果の出力に使用
block_height = 1000


# 各行を処理
for line in lines:
    # 空白と改行文字を除外し、':'で区切って必要な情報を取得
    parts = line.replace('\n', '').replace(' ', '').split(':')
    if len(parts) >= 3:  # 今回は特に必要ではないが一応最低限の要素数があることを確認
        chain_type = parts[0]  # チェーンタイプ (OnChainまたはOrphan)
        #orphanブロックのブロック数を更新
        if chain_type == 'Orphan':
            orphan_count += 1
        # チェーン全体のブロック数を更新
        data_count += 1

# フォーク確率を計算
fork_probability = orphan_count / data_count

# 結果を出力
result = f"チェーン全体のブロック数: {block_height}\nOrphan の数: {orphan_count}\nフォーク確率: {fork_probability:.5%}"

# 結果をテキストファイルに保存
#with open('output.txt', 'w') as output_file:
    #output_file.write(result)

# 結果を表示
print(result)
