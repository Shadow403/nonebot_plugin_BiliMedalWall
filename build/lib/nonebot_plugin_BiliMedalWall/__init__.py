# @python  : 3.11.0
# @Time    : 2023/11/03
# @Author  : Shadow403
# @Version : 0.1.0
# @Email   : admin@shadow403.cn
# @Software: Visual Studio Code

from .api import biliAPI
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters.onebot.v11.permission import GROUP_OWNER, GROUP_ADMIN

__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_BiliMedalWall",
    description="查询B站用户粉丝牌等级信息",
    usage="https://github.com/Shadow403/nonebot_plugin_BiliMedalWall#食用方法",
    type="application",
    homepage="https://github.com/Shadow403/nonebot_plugin_BiliMedalWall",
    supported_adapters={"~onebot.v11"},
    extra={},
)

biliAPI = biliAPI()

queryUserMedal = on_command("/buser", aliases = {"/b查"}, block = False, priority = 1)# , permission = GROUP_OWNER | GROUP_ADMIN | SUPERUSER

@queryUserMedal.handle()
async def queryUserMedal_handel(Initial: Message = CommandArg()):
    initialText = Initial.extract_plain_text()
    if (initialText.isdigit()):
        r = biliAPI.userMedalInfo(initialText)
        await queryUserMedal.send(MessageSegment.image(file=r))
    else:
        await queryUserMedal.send(message="UID应为纯数字")