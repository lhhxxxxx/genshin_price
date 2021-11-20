import json
from hoshino import Service, priv, aiorequests

sv_help = '''
[原神估价 +uid] 查询账号估价
'''.strip()

sv = Service(
    name='原神估价',  # 功能名
    use_priv=priv.NORMAL,  # 使用权限
    manage_priv=priv.ADMIN,  # 管理权限
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle='原神',  # 分组归类
    help_=sv_help  # 帮助说明
)


@sv.on_prefix('原神估价')
async def get_genshin_chara(bot, ev):
    uid = ev.message.extract_plain_text().strip()
    if not uid:
        return
    if uid.startswith('5'):
        server = 'cn_qd01'
    else:
        server = 'cn_gf01'
    result = await (await aiorequests.get(
        'ht'+'tp'+'s://a'+'pi.l' + 'e' + 'l' + 'a' + 'e' + 'r.co'+'m/y'+'s/g' + 'et' + 'P' + 'rice' + 'Res' + 'ult.p' + f'hp?uid={uid}&server={server}&from=normal')).json()
    if result['code'] == 200:
        result = result['result']
        total_intro1 = result['total_intro1']
        total_price = result['total_price']
        total_intro2 = result['total_intro2']
        role_price = result['role_price']
        role_intro = result['role_intro']
        weapon_price = result['weapon_price']
        weapon_intro = result['weapon_intro']
        abyss_price = result['abyss_price']
        abyss_intro1 = result['abyss_intro1']
        abyss_intro2 = result['abyss_intro2']
        msg = f'''{total_intro1}
{total_price}

{total_intro2}

{role_price}
{role_intro}

{weapon_price}
{weapon_intro}

{abyss_price}
{abyss_intro1}
{abyss_intro2}'''
        await bot.send(ev, msg, at_sender=True)
    else:
        await bot.send(ev, result['result'], at_sender=True)
