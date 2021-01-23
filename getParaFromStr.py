'''
Author: LawsonAbs
Date: 2021-01-12 16:48:21
LastEditTime: 2021-01-23 20:55:06
FilePath: /tools/getParaFromStr.py
'''

import sys
"""
功能：分割字符串，得到想要的形式
01.生成vscode中可以直接使用的参数
--cuda --dropout 0.5 --epochs 200 --input_directory ./data --scorer ./ --output_embedding customnpz-o_id_embedding_conve_embeddings.npz --train semcor --val semeval2007 --lr 0.0001 --predict_on_unseen --save ./saved_models/model.pt

那么生成的结果就是："--cuda", "--dropout", "0.5", "--epochs", "200", "--input_directory", "./data", "--scorer", "./", "--output_embedding", "customnpz-o_id_embedding_conve_embeddings.npz", "--train", "semcor", "--val", "semeval2007", "--lr", "0.0001", "--predict_on_unseen", "--save", "./saved_models/model.pt",
"""

res = ""
if len(sys.argv) < 2:
    print("参数不足")
else: # 拼接所有的参数成为一个str
    for i in range(1,len(sys.argv)): # 使用双引号串起来  
        res+='\"'
        res+= sys.argv[i]
        res+='\", '
    print(res)