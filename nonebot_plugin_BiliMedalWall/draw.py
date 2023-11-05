# @python  : 3.11.0
# @Time    : 2023/11/03
# @Author  : Shadow403
# @Version : 0.1.0
# @Email   : admin@shadow403.cn
# @Software: Visual Studio Code

from io import BytesIO
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager

resource_dir = Path(__file__).parent / "resources"

font_manager.fontManager.addfont(f"{resource_dir}\\fonts\\LXGWWenKaiGB-Regular.ttf")
plt.rcParams['font.sans-serif']="LXGW WenKai GB"

def toBase64(image):
    buff = BytesIO()
    image.savefig(buff, format="png", bbox_inches='tight')
    img_str = buff.getvalue()
    return img_str

def baseDraw(listData):
    statusCode = listData[0]
    if (statusCode == 0):
        dataTexts = listData[1][4]
        medalCount = len(dataTexts)
        plt.figure(dpi=300)
        ax_1 = plt.subplot(221)
        ax_1.axis('off')
        ax_1.text(0.01, 1.01, f"""UID: {str(listData[1][1])}\n等级: {str(listData[1][2])}\n总数: {str(medalCount)}\n昵称: {str(listData[1][0])}""")
        ax_1.table(
                cellText=dataTexts,
                cellLoc="left",
                colWidths=[0.3, 0.15],
                colLabels=["粉丝牌","等级"],
                colColours=["#e41a1c","#377eb8"],
                rowLoc="left",
                loc="upper left"
            )
        return toBase64(plt)

    elif (statusCode == -1):
        fontStyle = dict(color='r')
        plt.figure(dpi=300)
        ax_N1 = plt.subplot(221)
        ax_N1.axis('off')
        ax_N1.text(0, 0.7, f"""UID: {str(listData[1][1])}\n等级: {str(listData[1][2])}\n总数: 未知\n昵称: {str(listData[1][0])}""")
        ax_N1.text(0, 0.3, "该用户未拥有任何粉丝牌或未打开展示", fontdict=fontStyle)
        return toBase64(plt)

    else:
        fontStyle = dict(fontsize=20, color='r')
        plt.figure(dpi=300)
        ax_E1 = plt.subplot(221)
        ax_E1.axis('off')
        ax_E1.text(0.35, 0.7, "错误", fontdict=fontStyle)
        ax_E1.text(0.25, 0.3, "远程服务器错误\n请稍后再试~")
        return toBase64(plt)
