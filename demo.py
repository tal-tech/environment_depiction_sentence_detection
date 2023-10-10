import sys
from module.description import Description

if __name__ == "__main__":
    desc = Description()
    state, description = desc.init()
    print(state, description)
    if state < 0:
        sys.exit(0)

    sentence_list = [
        
        '她闭着眼睛，绝美的脸庞显露出痛苦的神情', # 神态
    ]
    state, desc_info = desc.get_all_descriptions(sentence_list)
    if desc_info['num'] == 1:
        print("是环境描写")
    else:
        print("不是环境描写")
    
    # print(desc_info)
